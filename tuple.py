#tuple --immutable sequence type

t=()
print("t=",t)
print(type(t))

t=(10,20,"python",True)
print(t)
print(type(t))
print(t[2])
print(t[:4])

t=10,
print(t)
print(type(t))

