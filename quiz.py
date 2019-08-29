print('Let\'s make simple quiz using dictionaries')

d={'Who is the author of the course?':'Nikita', 'What is the language of the course?':'Python',
 'How many lessons will be in the course?':26, 'What is the programm for version control?':'Git',
 'What is the capital of Russia?':'Moscow', 'What is the highest mark in russian school?':5}
r=0
for key in d:
    answer=input(key)
    if isinstance(d.get(key),(float,int)):
        try:
            v = float(answer)
            if v == d.get(key):
                print('Right!')
                r+=1
            else:
                print('Sorry, you are wrong')
        except ValueError:
            print('Sorry, you are wrong')
    else:
        if answer.lower() == d.get(key).lower():
            r+=1
            print('Right!')
        else:
            print('Sorry, you are wrong..')
print('Game is over! You have answered {} out of {} questions'.format(r,len(d)))
