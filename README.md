# fast-clipboard-sync

<p align="center">
  <img src="https://github.com/nngogol/fast-clipboard-sync/blob/master/1.gif" />
</p>


✓ Usage section included

✓ Ready to use

Use-case: your copy-paste clipboard *TO* other machine: other computer, VM, remote machine.

<!-- Tutorial included -->


# Nice parts

- Don't need to install Additions on VM.
- any hypervisor: qemu, vbox, vmware, WHATEVER.
- any OS:         any operation system.         Try, for example, any GNU/Linux distro.

```
client.py   70 lines
server.py   56 lines
```


# Why this is working?

Because websockets. Learn it and you will get it.

<!-- Watch my explanation -> (...)[youtube link]. -->

# Usage:

DEAD-simple.

```bash
# install before doing anything:
#   ___
#  / _ \
# | | | |
# | | | |
# | |_| |
#  \___/
pip install websockets pyperclip






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

