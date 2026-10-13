#list --mutable sequence type

l1=[10,20,"python",30.5,True,"hello",30]
print("l1=",l1)
print("Datatype of l1:",type(l1))
print("l1[0]=",l1[0])
print(l1)

#append
l1.append(100)
print("l1=",l1)
l1[3]="java"
print("l1=",l1)

#remove
l1.remove("java")
print("l1=",l1)

#empty list
l1=[]
print("l1=",l1)
print("Datatype of l1:",type(l1))


l1=[10,20,30]
l2=[10,20,30]
print(l1)
print(l2)
print("Address of l1:",id(l1))
print("Address of l2:",id(l2))
l1[0]=100
print(l1)
print(l2)