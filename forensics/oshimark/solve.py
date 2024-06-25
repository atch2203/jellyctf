#with open('desc.txt', 'r') as f:
#    bs = f.read()

#bs.replace('\u200C', '')
#print(bs.encode())

a = ""
with open("hex.txt", "r") as f:
    a = f.read()
a = a.split()
b = a[2::7]
a = a[3::7]
a = [int(a[i],16)-(64+47 if b[i] == '84' else 47) for i in range(len(a))]

print("".join([chr(x) for x in a]))
#print(a)
#a = a.split()
#print(a)
#print(bytes.fromhex("".join(a)).decode())
""""
a = a.split()
a = a[4:-5]
a = [a[i:i+7] for i in range(0, len(a), 7)]
a = [int("".join(i), 16) for i in a]
a = [(i+81)%192 for i in a]
print(a)
print(''.join([chr(i) for i in a]))

u = "f3 a0 85 8e e2 80 8c".split()
u = [int(x, 16) for x in u]
s = len(u)
letters = []
diffs = []

chunks = int(len(a)/s)
for i in range(chunks):
    b = a[i*s: s*i+s]
    b = [int(x, 16) for x in b]
    diff = [b[i]-u[i] for i in range(s)]
    letters.append(chr(diff[3]+97))
    diffs.append(diff[2])

print(letters)
print(diffs)
"""
