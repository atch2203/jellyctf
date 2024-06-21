from pwn import *
import time
from ctypes import CDLL

flag = "jellyCTF{mad3_w1th_99_percent_l0v3_and_1_percent_sad_g1rl_t3ars}"

"""
the random is seeded with current time in seconds
"""

passcodeLength = 6
bitmask = (1 << passcodeLength) - 1

libc = CDLL("libc.so.6")

# p = process("./a.out", stdin=PTY, stdout=PTY)
p = remote(host='chals.jellyc.tf', port=6000)

s = int(time.time())
# print(s)

libc.srand(s)
for i in range(10):
  r = libc.rand()
  # print(f"r{i} {r}")
  passcode = r & bitmask
  print(f"passcode{i} {bin(passcode)}")
  print(p.recvuntil(b"passcode"))
  p.sendline(bin(passcode)[2:].encode('utf-8'))

print(p.recvuntil(b"}"))

p.interactive()

