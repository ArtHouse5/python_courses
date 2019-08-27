n=int(input('write a number'))
if n==2:
    print('Prime!')
elif n>1:
    for i in range(2,n):
            if n%i == 0:
                print('Not prime!')
                break
    else:
        print('This is a prime number!')
else:
    print('This is not a prime number')
