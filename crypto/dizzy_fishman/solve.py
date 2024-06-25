import time
from Crypto.Util import number
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

"""
goal: decrypt ciphertext.hex()
we can make g=2, so we can crack secret_A and B => get whole secret

"""

def brute_force(base, res, mod):
    b = base
    for i in range(2, 10000+1):
        b = (b*base)%mod
        if b == res: return i

p = 63579193433447636138142180956143903452427972074605894864703396671022456098599
g = 2
pa = 12216650520779549051085807383600007441099464649139735571057936351615978497631
pb = 268435456 # thats crazy

cip = "7c78e0ee6710a27b97cfb37501e02cc0e4f8cf921ecb9a891793622361efaa6cc7618b790239761506f8f83fa49b974ac7618b790239761506f8f83fa49b974a"

sa = brute_force(g, pa, p)
sb = brute_force(g, pb, p)
key = pow(pa, sb, p)

encoded_key = key.to_bytes(32, byteorder='big')
cipher = AES.new(encoded_key, AES.MODE_ECB)

pt = cipher.decrypt(bytes.fromhex(cip))
print(pt) #jellyCTF{SOS_stuck_in_warehouse}