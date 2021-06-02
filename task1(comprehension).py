s = input("Enter a sequence of characters: ")
dictionary = {i:s.count(i) for i in s}
print(dictionary)
b = sorted(list(dictionary.values()))
print(b)
temp = 0
for x in b:
    if(x  == b[-1] or x == b[-1]-1):
        temp+=1
if(temp == len(b)):
    print("My string")
else:
    print("Not my string")
