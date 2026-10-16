#non boolean behaviour
a=0
b=5
c=a or b
print(c)

a="python"
b=""
c=b or a
print(c)

a="python"
b=""
c=b and a
print(c)


#boolean behaviour
#NOT operator

a,b=10,5
c=not(a<b)
print(c)


#OR operator
a,b=10,5
c=a<b or b>50
print(c)

#AND operator

a,b=10,5
c=a<b and b<50
print (c)
a,b=10,5
c=a>b and b<50
print (c)
