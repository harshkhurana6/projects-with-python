name="Harsh"
age="20"
str=name+" is "+str(age)+" yr old"
print("name and age",str)


rate=625.7135
print("rate is %.2f"%(rate))

s="i like python"
ns=s.capitalize()
print(ns)

s=input("enter the string:")
if len(s)>2:
  x=s[0:2]+s[-2:]
  print(x)
else:
  print("string length should be >=2")

s=input("Enter any string:")
ch=input("Enter the character to replace:")
ns=s.replace(ch,'$')
print(ns)

s=input("enter string:")
if len(s)>3:
  if s.endswith("ing"):
    s=s+"ly"
  else:
    s=s+"ing"
  print(s)

s="I Like Python"
ns=s.lower()
print(ns)

s="I Like Python"
ns=s.upper()
print(ns)

s="I Like Python"
ns=s.title()
print(ns)

s="I Like Python"
print(s.center(22,'*'))

s="I Like Python"
print(s.ljust(22,'*'))

s="I Like Python"
print(s.rjust(22,'*'))

s="***python***"
ns=s.lstrip('*')
print(ns)

s="***python***"
ns=s.rstrip('*')
print(ns)

s="***python***"
ns=s.strip('*')
print(ns)

s="hello python\n "+"welcome"
s.strip
print(s)

s="this is my pen"
print(s.count("is",0,4))

s="this is my pen"
s=s.replace(" is "," was ")
print(s)


x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
max=lambda x,y: x if x>y else y
print(max(x,y))
product=lambda x,y:x*y
print(product(x,y))
