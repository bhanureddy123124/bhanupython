import statistics
n=int(input("enter the length of string"))
a=[]
for i in range(n):
    b=int(input("enter the element"))
    a.append(b)
print("mean",statistics.mean(a))
print("median",statistics.median(a))
print("mode",statistics.mode(a))
