#bitwise operator & | ^ << >>
a=4
b=5
print(a&b)
print(a|b)
print(a^b)


print(~4)
print(~101)
print(~False)

a=10
print(a<<2)
print(a>>2)

#ternary operator

a,b=100,20
max= a if a>b else print("Max=",max)

a,b=100,20
print("a is max") if a>b else print("b is max")

a=19
b=17
max= a if a>b else print(max)

a,b=20,10
print("a can't") if a>b else print("b can")

c=8
print("Even")if a%2==0 else print("odd")

#max of 3 numbers
a,b,c=20,10,50
#print("a is greater")if a>b else print("b is greater") elif print("c")
print("a is max")if a>b and a<c else print("c is max")
