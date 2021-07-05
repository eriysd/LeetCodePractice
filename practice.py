import itertools

'''
[] operations works for any iterable elements
'''
aList = [1, 2, 3, 4, 5, 6]
bString = 'Hello, It\'s me'
print(aList[::2])
print(bString[::2])
print(aList[::-1])
print(bString[::1])

'''
index and find
'''
# index raise errors but can be used for all interable elements
print(aList.index(2))  # works
print(bString.index('e'))  # works
# print(aList.index(10))  # raises ERROR

# find doesn't, but can only be used for String
# print(aList.find(2)) #invalid!
print(bString.find('e'))  # works

# solution here is to use
#idx = bString.index(x) if x in aList else None

'''
itertools used for creating iterable sequence FROM interable element
'''
for i in itertools.islice(bString, None, None, 3):
    print(i)


# two ways to COMPREHEND a list
# using map() requires a new function, which is why lambda is required
print([x+2 for x in aList])
# print(list(map(x+2, aList))) --> x is undefined ERROR
print(list(map(lambda x: x+2, aList)))
