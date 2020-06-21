## fast-clipboard-sync

<p align="center">
  <img src="https://github.com/nngogol/fast-clipboard-sync/blob/master/1.gif" />
</p>


I have *Usage section* included + *Ready to use* software

Use-case: your copy-paste clipboard *TO* other machine: other computer, VM, remote machine.

<!-- Tutorial included -->

## Nice parts

- Don't need to install Additions on VM.
- any hypervisor: qemu, vbox, vmware, WHATEVER.
- any OS:         any operation system.         Try, for example, any GNU/Linux distro.
- 3 file for all code

## Why this is working?

Because websockets. Learn it and you will get it.

<!-- Watch my explanation -> (...)[youtube link]. -->

## Usage:

DEAD-simple.

1. install libs
2. set host and port in config.py
3. use this software


### => 1 <=  install libs

**only FOR GNU/Linux** users: `sudo apt-get install xsel xclip` *or, if you want*, `pip install gtk PyQt4`

Main command: `pip install websockets pyperclip`

### => 2 <=  set host and port in config.py

Just do it.

### => 3 <=  use this software

```bash
#  __
# /_ |
#  | |    # server.py file #
#  | |    run this command on your
#  | |    
#  |_|    VM | other machine | whatever
python3 server.py

# ----------------------------------------

#  ___
# |__ \
#    ) |  # client.py file #
#   / /   run this command on your
#  / /_
# |____|  on your pc:
python3 client.py
# Now,         /\
# after running this commnd
# try hit ctrl+c    :)


```

