#       _ _            _ made at 2020-06-20 17:07:58
#      | (_)          | |
#   ___| |_  ___ _ __ | |_
#  / __| | |/ _ \ '_ \| __|
# | (__| | |  __/ | | | |_
#  \___|_|_|\___|_| |_|\__|

import asyncio, json, websockets, pyperclip, sys
from config import server_host, server_port
curr_ws, stop_queue = None, asyncio.Queue()

async def get():
	global curr_ws; return json.loads(await curr_ws.recv())
async def send(json_data):
	global curr_ws;
	if curr_ws: await curr_ws.send(json.dumps(json_data))
async def stop_buffer_watcher():
	await stop_queue.put('close watcher');
	await asyncio.sleep(0.05)

async def buffer_watcher():
	global curr_ws, stop_queue
	try:
		prev = pyperclip.paste()
		while True:
			await asyncio.sleep(0.2)

			# global queue
			if not stop_queue.empty():
				msg = await stop_queue.get(); stop_queue.task_done()
				break

			# buffer
			curr = pyperclip.paste()
			if prev != curr: await send({'action':'new-buffer','data':curr})
			prev = curr

	except KeyboardInterrupt as e:  print(f'\tkeyboardinterrupt > {str(e)}')
	except Exception as e:          print(f'\tError>>>: {e.msg}')
	print('<< watcher end')
async def ws_sender():
	global curr_ws, stop_queue, host, port
	try:
		# connect to a server
		ws = await websockets.connect(f"ws://{server_host}:{server_port}"); curr_ws = ws;
		first_answer = await get(); msg = first_answer['msg']

		async for result in ws: # read messages, till you catch STOP message
			json_msg = json.loads(result)
			# exit
			if json_msg['action'] == 'exit': break
			if json_msg['action'] == 'text-message': print(f'\t\t{json_msg}')

		if ws: # close other loop + socket
			try:
				await stop_buffer_watcher()
				await ws.close()
			except Exception as e: print('Exception. cant close ws:', e)
		print('\t\tCLient closed!')

	except KeyboardInterrupt as e:
		if ws:
			# close other loop + socket
			await stop_buffer_watcher()
			await send({'action': 'exit'});
			await ws.close()
	except Exception as e:
		if e.errno == -3:
			print(f'!> Fix your config.py; {e}')
			await stop_buffer_watcher()
		if e.errno == 111:
			print(f'!> IP port is bad; {e}')
			await stop_buffer_watcher()
		else:
			print(f'!> GENERAL ERROR: {e}')

	print('<< sender end')

def main():
	global curr_ws
	try:
		print('starting sender and wather');
		loop = asyncio.get_event_loop();
		loop.run_until_complete(asyncio.gather(ws_sender(), buffer_watcher()));
		loop.close();
		print('||| ended')
	except KeyboardInterrupt as e:   asyncio.ensure_future(curr_ws.close())
	except Exception as e:           print('WTF? watch the code', e)

	print('\nbye.')
if __name__ == '__main__': main()