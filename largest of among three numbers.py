a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>b) and (a>c):
      largest=a
if(b>c) and (b>a):
      largest=b
if(c>b) and (c>a):
      largest=c
print("largest of three numbers",largest)
