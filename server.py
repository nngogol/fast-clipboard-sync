#  ___  ___ _ ____   _____ _ __ made at 2020-06-20 17:08:01
# / __|/ _ \ '__\ \ / / _ \ '__|
# \__ \  __/ |   \ V /  __/ |
# |___/\___|_|    \_/ \___|_|     async-websocket

''' get ws connection
    on_new_message -> set new clipboard_data'''

import asyncio, json, websockets, pyperclip
from config import server_port

curr_ws = None

async def close_it():
    global curr_ws
    await curr_ws.close()


async def send(json_data):
    global curr_ws
    if curr_ws:
        await curr_ws.send(json.dumps(json_data))


async def on_message(ws, path):
    global curr_ws; curr_ws = ws
    print('> new connection')
    await send({'action': 'text-message', 'msg': 'привет'})

    try:
        async for message in ws:
            data = json.loads(message)

            # on "EXIT"
            if data["action"] == "exit": break
            # on "new-buffer"
            elif data["action"] == "new-buffer":
                print('\tnew-buffer')
                pyperclip.copy(data["data"])
                await send({
                    'action': 'text-message',
                    'msg': 'copied!'
                })

        await ws.close()
    except Exception as e:
        if e.code == 1006:
            print('\tWS is CLOSED by user')
        else:
            print(f'\tError. Report to developer: {e}')
    print('exiting')


def main():
    global curr_ws
    global server_port
    try:
        print('started')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(websockets.serve(on_message, '0.0.0.0', server_port))
        loop.run_forever()

    except KeyboardInterrupt as e:
        if curr_ws:
            async def close_it():
                global curr_ws
                if curr_ws and curr_ws.state.value != 3:
                    await send({'action': 'exit'})
                    await asyncio.sleep(0.05)
                    await curr_ws.close()
            asyncio.get_event_loop().run_until_complete(close_it())
            # asyncio.ensure_future(close_it())
        print('keyboard exiting')

    except Exception as e:
        print(f'WTF? watch the code: {e}')
    print('ended')


if __name__ == '__main__':
    main()
