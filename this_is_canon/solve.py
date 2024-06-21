out = "1000001010010011101111101011101011111010000010100100110000111001110111010000111011100111110100111100100110101111000001110010110110010001100011011001000011001110011101000110101100010110011111111"
flag = ""

class Node:
    # z is 0, o is 1
    def __init__(self, c=None):
        self.c = c
        self.z = None
        self.o = None


trees = {
    '_':"000",
    'e':"001",
    'l':"010",
    'y':'011',
    'j':'1000',
    'o':'1001',
    'r':'1010',
    'a':'10110',
    'c':'10111',
    'd':'11000',
    's':'11001',
    't':'11010',
    'u':'11011',
    'w':'11100',
    'f':'111010',
    'h':'111011',
    'k':'111100',
    'm':'111101',
    '{':'111110',
    '}':'111111'
}

root = Node()
for ch in trees:
    v = trees[ch]
    h = root
    for p in v:
        if p == '1':
            if h.o:
                h = h.o
            else:
                h.o = Node()
                h = h.o
        else:
            if h.z:
                h = h.z
            else:
                h.z = Node()
                h = h.z
    h.c = ch

it = root
for b in out:
    if it.c:
        flag += it.c
        it = root
    if b == '1':
        it = it.o
    else:
        it = it.z

print(flag)
