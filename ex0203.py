#condition in python
#use random fuinction
#if and else condition
import random
x= random.randint(1,6)
y=random.randint(1,6)
print ('Dices Nr are: ',x,' and ',y)
if x+y<5 or x==y:
    print('you won!')
else:
    print('you lose!') 
print('finish') 