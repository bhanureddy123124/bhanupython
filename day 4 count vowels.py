n=(input("enter any string"))
count=0
for char in n:
    if char.lower()in "aeiouAEIOU":
        print(char)
        count=count+1
print("n.of vowels",count)
