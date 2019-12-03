#conditionals with if/elif
#2 player wants to play on dices with the rule
#the winner has a dice, first dice less than second or first dice equal to second
#first more than second and second less than 3 lead to conditional win and else is lose

import random
print('Dices')
x=random.randint(1,6)
y=random.randint(1,6)
print(x,y)
if x<y or x==y:
    print('Win!')
elif x>y & y<3: 
    print('Conditional Win!')
else:
    print('Lose!')
print('finish')    

 