import codecs
def to_base(number, base):
    """Converts a non-negative number to a list of digits in the given base.

    The base must be an integer greater than or equal to 2 and the first digit
    in the list of digits is the most significant one.
    """
    if not number:
        return [0]

    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))

def from_base(digits, base):
    """Converts a list of digits in the given base to an integer.

    The first digit is the most significant and the base is assumed to
    be an integer greater than or equal to 2.
    """
    power = 1
    number = 0
    for digit in reversed(digits):
        number += power * digit
        power *= base
    return number

# o = "VGhhdCB3YXMganVzdCBhIHdhcm0gdXAuIEhlcmUgaXMgdGhlIGFjdHVhbCBmbGFnLCB0aG91Z2ggeW91IG1heSBuZWVkIGEgYmFzZSB0aGF0J3MgJ0EnIGJpdCBsYXJnZXI6CumpquqNrOehueetlPCTibvmmajpkbPmqanqhZ/wk4W16ZG06ZGh5qWi5pmz6ZGj8JSVofCUlaHwlJWh8JOBofCTja3woI2w"

# b = 0xe9a9aaea8dace7a1b9e7ad94f09389bbe699a8e991b3e6a9a9ea859ff09385b5e991b4e991a1e6a5a2e699b3e991a3f09495a1f09495a1f09495a1f09381a1f0938dadf0a08db0
# bs = "e9a9aaea8dace7a1b9e7ad94f09389bbe699a8e991b3e6a9a9ea859ff09385b5e991b4e991a1e6a5a2e699b3e991a3f09495a1f09495a1f09495a1f09381a1f0938dadf0a08db0"
# # b = from_base(a, 16)
# s = codecs.decode(bs, 'hex').decode('utf-8')
# print(s)
# print(b)
# c = to_base(b, 2**8)
# print(c)
# print([chr(x) for x in c])

x = "ʿ蛧鸩ઞ假备㮝螖𐱇𓉺澟嬚ᱸ芋ᗋޥ𒒽瀏即𑠌獀ʞ"
y = [ord(c) for c in x]
print(y)
# bc = "".join([str(x) for x in y])
# bc = int(bc)
# print(bc)

# # print(z)
# for i in range(10, 0xBABB):
z = from_base(y, 2**32)
for j in range(16, 0xBABB):
    w = to_base(z, j)
    if w[0] == 106 and chr(w[1]) == 'e' and chr(w[2]) == 'l':
        print("".join([chr(x) for x in w]))
        
