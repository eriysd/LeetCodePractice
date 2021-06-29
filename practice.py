import itertools

aList = [1, 2, 3, 4, 5, 6]
bString = 'Hello, It\'s me'


print(aList[::2])
print(bString[::2])
for i in itertools.islice(bString, None, None, 3):
    print(i)

print(aList.append(8))
