#index and slicing

#index --positioning of character in string

a="Python is easy language"
print(a[4])
print(a[6])
print(a[20])
print(a[-9])
print(a[-18])

#slicing -- extracting a part of string
s="Python is easy language"
print(s[0:6])#n
print(s[0:12])#Python
print(s[2:10])#Python is ea
print(s[0:20:2])#thon is
print(s[1: 10])#ython is easy
print(s[ : 10])#Python is
print(s[:])#Python is easy language
print(s[::])#Python is easy language
print(s[2:40])#thon is easy language

print(s[::-1])#egaugnal ysae si 
print(s[2:10:-1]) #no output
print(s[10:2:-1])#e si noh
print(s[10:2])#no output 
print(s[-12:-2])