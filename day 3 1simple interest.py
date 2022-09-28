p=int(input("enter principle amount"))
t=int(input("enter the n.of years"))
choice=str(input("is a customer senior citizen (y/n):"))
if choice in ('n','y'):
    if choice =='N':
        r=10       
    else:
        r=12                         
si=p*t*r/100
if(p<0 or t<0):
    print("invalid")
else:
    print("simple interest",si)

              
        
