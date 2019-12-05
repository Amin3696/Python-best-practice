#find a random nember les than 10 which chosen with the user
import random
asw=input ('guss a number less than 10!did you?(Y/N)')

if (asw=='Y' or asw=='y'):
    answ2=input('is it less than 5?(Y/N)')
   
    if(answ2=='y' or answ2=='Y'):
        guess=random.randint(0,4)
        print ('is it ',guess)
        answ3=input('Y/N?')
        if(answ3=='y' or answ3=='Y'):
            print('you win!')
        elif(answ3=='N' or 'n'):
            print('try again! line 12')

    elif(answ2=='n' or answ2=='N'):
        guess2=random.randint(6,10)
        print('is it ',guess2)
        answ4=input('Y/N?')
        if(answ4=='y' or answ4=='Y'):
            print('you win!')
        elif(answ4=='N' or answ4=='n'):
            print('try again! line 22')
print ('See you!')

