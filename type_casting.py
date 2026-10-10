#typecasting/type-corehsion
#1. int

x=2.45
i=int(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of i:",type(i))
print("i=",i)

x="234"
i=int(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of i:",type(i))
print("i=",i)


x=False
i=int(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of i:",type(i))
print("i=",i)


x=10
y=20
z=x+y
print(x)
print(y)
print(z)


#2.float

x=10
f=float(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of f:",type(f))
print("f=",f)

x=True
f=float(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of f:",type(f))
print("f=",f)


x=False
f=float(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of f:",type(f))
print("f=",f)


#3.string
x="123"
f=float(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of f:",type(f))
print("f=",f)

#complex


#single argument conversion
x=5
print("Datatype of x:",type(x))
print("x=",x)
c=complex(x)
print("Datatype of c:",type(c))
print("c=",c)


x=2.5
print("Datatype of x:",type(x))
print("x=",x)
c=complex(x)
print("Datatype of c:",type(c))
print("c=",c)

x=True
print("Datatype of x:",type(x))
print("x=",x)
c=complex(x)
print("Datatype of c:",type(c))
print("c=",c)


x="12"
print("Datatype of x:",type(x))
print("x=",x)
c=complex(x)
print("Datatype of c:",type(c))
print("c=",c)


#double argument conversion
'''
x=2
y="3"
z=complex(x,y)#double arguments cant convert string to complex 
print(x)
'''

x=4
y=True
z=complex(x,y)
print(x)
print(y)



#bool

#float into bool
x=0.00
print("Datatype of x:",type(x))
print("x=",x)
b=bool(x)
print("Datatype of b:",type(b))
print("b=",b)

#int into bool
x=-23
b=bool(x)
print("Datatype of x:",type(x))
print("x=",x)
print("Datatype of b:",type(b))
print("b=",b)   

#complex into bool
x=1+2j
print("datatype of x:",type(x))
print("x=",x)
b=bool(x)
print("Datatype of b:",type(b))
print("b=",b)

x=0.0+0j
print("datatype of x:",type(x))
print("x=",x)
b=bool(x)
print("Datatype of b:",type(b))
print("b=",b)

#string into bool
x=""
print("datatype of x:",type(x))
print("x=",x)
b=bool(x)
print("Datatype of b:",type(b))
print("b=",b)

x="Python"
print("datatype of x:",type(x))
print("x=",x)
b=bool(x)
print("Datatype of b:",type(b))
print("b=",b)

#5.string

a=10
b=2.4
c=2+3j
d=True
s=str(a)
s=str(b)
s=str(c)
s=str(d)
print("Datatype of a:",type(a))
print("a=",a)
print("Datatype of b:",type(b))
print("b=",b)
print("Datatype of c:",type(c))
print("c=",c)
print("Datatype of d:",type(d))
print("d=",d)