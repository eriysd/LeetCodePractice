import itertools
'''
Understanding itertool.groupby()

iterable passed into groupby() will automatically grouped into nearst neighbors
'1223' --> groups: 1, 222, 3
'aa111a' --> groups: aa, 111, a

group variable needs to be list() to print as: <itertools._grouper object>
'''
s = '2112aaa'
for digit, group in itertools.groupby(s):
    print('digit: ', digit, '\ngroup:', list(group))

'''
Output
digit:  2 
group: ['2']
digit:  1 
group: ['1', '1']
digit:  2 
group: ['2']
digit:  a 
group: ['a', 'a', 'a']
'''
