#1 Throwing and catching exceptions
from random import randint
def randex():
    ex=(ValueError('I am ValueError'),TypeError('I am TypeError'),
    RuntimeError('I am RuntimeError'))
    x=randint(0,2)
    raise ex[x]

try:
    randex()
except ValueError as v:
    print('I cought Value error : ',v)
except TypeError as t:
    print('I cought Type error : ',t)
except RuntimeError as r:
    print('I cought Runtime error : ',r)

#2 Function which sorts given list if it consists of integers
def intlist(l):
    if isinstance(l,list):
        if all(isinstance(x,int) for x in l):
            l.sort()
            return l
        else:
            raise ValueError('Not all objects of list are integers')
    else:
        raise ValueError('Input should be list')
#tests ok!

#3 Function which receives dictionary and transform it's keys into strings
def strdic(d):
    if isinstance(d,dict):
        new=dict()
        for key in d:
            new.update({str(key):d.get(key)})
    else:
        raise ValueError('Input should be dictionary')
    if all(isinstance(x,str) for x in new):
        print('Everything is ok, here is the result :')
    return new

#tests ok!

#4 Function which receives numbers and multiply them
def multiplyer(*numbers):
    m=numbers[0]
    for n in numbers[1:]:
        m*=n
    return m
