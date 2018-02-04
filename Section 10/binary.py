with open(".\\Section 10\\binary", "bw") as bin_file:
    for i in range(17):
        # if you pass int i without brackets to bytes
        # it will create i bytes all set to zero.
        bin_file.write(bytes([i]))
    # this version is more pythonic
    bin_file.write(bytes(range(17)))

with open(".\\Section 10\\binary", "br") as bin_file:
    for b in bin_file:
        print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
d = 2998302  # 02 2D C0 1E

import sys

# big/little endianness i.e. byte order
with open(".\\Section 10\\binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'little'))
    bin_file.write(d.to_bytes(4, sys.byteorder))

with open(".\\Section 10\\binary2", "br") as bin_file:
    a = int.from_bytes(bin_file.read(2), 'big')
    b = int.from_bytes(bin_file.read(2), 'big')
    c = int.from_bytes(bin_file.read(4), 'little')
    d = int.from_bytes(bin_file.read(4), sys.byteorder)
    print(a, b, c, d)
