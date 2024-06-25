c = "06 1C 2F 38 3F 38 2C 29 09 0A 16 2D 1C 16 2B 31 17 1B 2D 0A 16 0F 18 1C 11"
c = c.split()
c = [int(i, 16) for i in c]
res = ""
key = "jel"
for i in range(len(c)):
    k = key[-3]
    next = c[i]^ord(k)
    key += chr(next)
    res += k
print(res)

# jellyCTF{xorry_not_xorry}


