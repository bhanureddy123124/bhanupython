start = int(input("A="))
end = int(input("B="))
count = 0
if(start<0 or end<0 or start==end):
    print("invalid")
else:
    print("Composite Numbers between %d and %d: " % (start, end))

for start in range(start, end+1):
    for i in range(1, start+1):
        if(start % i == 0):
            count += 1;
    if(count > 2):
       print(start, end=" ")
    count = 0
