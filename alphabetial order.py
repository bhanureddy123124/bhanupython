n=int(input("Enter the length:"))
arr=[]
for i in range(0,n):
    a=input("Enter the string:")
    arr.append(a)
print(arr)
ch=input("Enter the order required(a/d):")
if(ch=='a'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("THE ASCENDING ORDER")
    for i in range(0,n):
        print(arr[i])
elif(ch=='D' or ch=='d'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("THE DESCENDING ORDER")
    for i in range(0,n):
        print(arr[i])
