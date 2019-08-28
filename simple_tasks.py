#1
print('Create list of 6 numbers and sort it in ascending order')
l=[4,23,15,42,16,8]
print('The initial list is ',l)
l.sort()
print(l)
print()

#2
print('Create dictionary with 5 items int:str and print it pairwise')
d = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'}
print('The initial dictionaty is ',d)
for key in d:
    print(key,d[key])
print()

#3
print('Create tuple with 5 fractions and find min and max in it')
from fractions import Fraction
t=(Fraction(1,2),Fraction(2,3),Fraction(5,7),Fraction(1,4),Fraction(7,8))
print('The initial tuple is ',t)
print('The maximum in this tuple is {}, the minimum is {}'.format(max(t),min(t)))
print()

#4
print('Create list of three words and concatenate it to get "word1->word2->word3"')
l2=['Earth','Spain','Madrid']
print('The initial list is ',l2)
sep='->'
print(sep.join(l2))
print()

#5
print(' Split the string "/bin:/usr/bin:/usr/local/bin" into list by symbol ":" ')
s = '/bin:/usr/bin:/usr/local/bin'
print(s.split(':'))
print()

#6
print('print which numbers from 1 to 100 are devided by 7 and which are not')
for i in range(1,101):
    if i%7==0:
        print(i, ' devided by 7')
    else:
        print(i, ' is not devided by 7')
print()

#7
print('Create matrix 3x4 and print firstly all the rows then all the columns')
multi=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]
]
print('The initial matrix is ',multi)
print('Rows are :')
for row in multi:
    print(row)
print('Columns are:')
for column in range(0,4):
    print()
    for i in range(0,3):
        print(multi[i][column])
print()
"""
also we can do it with the help of numpy:

import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8]])
array([[1, 2, 3, 4],
    [5, 6, 7, 8]])

A[:,2] # returns the third columm
"""

#8
print('Create a list and in the loop write the object and its index')
l3=['booom', 84, None, 'python', True, False, 90, 33]
print(l3)
for object in l3:
    print('Object {} has index {}'.format(object,l3.index(object)))

#9
print('Create a list with tree values "to_delete" among the others and delete them')
l4=['to_delete','Good!','better','to_delete','to_delete','the_best']
print(l4)
while 'to_delete' in l4:
    l4.remove('to_delete')
print('Clear list : ',l4)

#10
print('Print numbers from 10 to 1')
for i in range(10,-1,-1):
    print(i)
