#1

x=int(input('Insert integer: '))
try:
    if x < 0:
        raise TypeError('number < 0')
    elif x > 10:
        raise IndexError('number > 10')
    elif x%2 == 0 :
        raise ValueError('number is even')
except TypeError as t :
    print('Error : ',t)
except IndexError as i :
    print('Error : ',i)
except ValueError as v :
    print('Error : ',v)

#2

l=[1,3,'ki',True,0,None, 5, '5', 'mamma']
try:
    i=int(input('Insert desired index'))
    if i > len(l) or i < 0:
        raise IndexError('your index is out of range')
    print(l[i])
except IndexError as i:
    print('Error :',i)
except ValueError:
    print('input should be an integer number')

#3

def twoarg(a,b):
    if a>0 and b>0:
        return a+b
    if a<0 and b<0:
        return a-b
    if (a>0 and b<0) or (a<0 and b>0):
        return 0

#4 Returns two max values

def twomax(a,b,c):
    l=[a,b,c]
    l.sort()
    print(l[1],' ',l[2])

#5 Returns even or odd nembers from the list depending on flag

def evod(numlist,flag):
    new_list=list()
    if flag:
        for el in numlist:
            if el%2 != 0:
                new_list.append(el)
    else:
        for el in numlist:
            if el%2 == 0 :
                new_list.append(el)
    return new_list

#6

def maxmin(*nums):
    return max(nums),min(nums)

#7

def strcase(st,case=True):
    if case:
        return st.upper()
    else:
        return st.lower()

#8
def str_unlim(*strs,glue=':'):
    new=list()
    for s in strs:
        if len(s)>3:
            new.append(s)
    return glue.join(new)
