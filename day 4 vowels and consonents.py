def vowelsconsonents(string):
    vowels=[each for each in string if  each in "aeiouAEIOU"]
    print("n.of vowels",vowels)
    consonents=[each for each in string if each not in "aeiouAEIOU"]
    print("n.of consonents",consonents)
string=input("input any string")
vowelsconsonents(string)
