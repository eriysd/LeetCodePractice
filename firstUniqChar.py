'''
This didn't work, because the last repeated one would be registered as unique
as it only compares to the characters after its position!

def firstUniqChar(self, s: str) -> int:
        for index, char in enumerate(s):
            if s.find(char, index+1) is -1:
                return index
            
        return -1

'''

def firstUniqChar(s: str) -> int:
        dictionary = {}
        for element in s:
            if element not in dictionary:
                dictionary[element] = 1
            else:
                dictionary[element] = 2
                
        for element in dictionary:
            if dictionary[element] == 1:
                return s.index(element)
            
        return -1

s = "loveleetcode"
print(firstUniqChar(s))
