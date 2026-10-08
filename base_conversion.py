# Base conversion in Python
#bin() - converts an integer to a binary string
#oct() - converts an integer to an octal string
#hex() - converts an integer to a hexadecimal string

x=0xa23
print(x)
oc=oct(x)
print("octal form of x:",oc)


x=0o156
print(x)
b=bin(x)
print("binary form of x:",b)

x=0b1010
print(x)
h=hex(x)
print("hexadecimal form of x:",h)

x=10
print(x)
o=oct(x)
print("octal form of x:",o)