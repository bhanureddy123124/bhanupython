name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))

if age >= 18:
    print("{} can cast votes this year!".format(name))
else:
    print("{} can cast votes after {} years!".format(name, 18-age))
