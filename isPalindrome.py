def isPalindrome(s: str) -> bool:        
    newS = []
    
    for elem in s:
        print(elem)
        if elem.isalnum():
            newS.append(elem.lower())
    
    original = newS.copy()
    original.reverse()
    
    return newS == original

'''
    smart solution from the discussion
    
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True
    
    '''        
        
s = 'is car'
print(isPalindrome(s))
            