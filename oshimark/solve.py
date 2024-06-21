a = ""
with open("hex.txt", "r") as f:
    a = f.read()
    a = a.split()

u = "f3 a0 85 8e e2 80 8c".split()
u = [int(x, 16) for x in u]
s = len(u)
letters = []
negs = []

chunks = int(len(a)/s)
for i in range(chunks):
    b = a[i*s: s*i+s]
    b = [int(x, 16) for x in b]
    diff = [b[i]-u[i] for i in range(s)]
    letters.append(chr(diff[3]+97))
    negs.append(diff[2])
    #print(diff)

#print(letters)
#print(negs)

# print("".join(letters))

for i in range(chunks):
    # if negs[i] == -1:
    if letters[i] == "p":
        print(f"{letters[i]} {negs[i]}")
    

