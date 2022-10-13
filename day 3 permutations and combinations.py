n1=int(input("enter the number"))
n2=int(input("enter the number"))
n3=int(input("enter the number"))
list=[]
list.append(n1)
list.append(n2)
list.append(n3)
print(list)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
        
            if(i!=j and j!=i ):
                print(list[i],list[j],list[k])
                
            
