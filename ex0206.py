# play with try/except
#input a value and answer if user is adult or not 
ageString=input('how olds are you?')

try:
    age=int(ageString)
except :
    age=-1

if age>18:
    print('you are an adult! you can enjoy the bar!') 
elif age>0:
    print('you are younger than 18! you can not get in the bar!') 
else:
    print('try again! invalid input!')
print('finish')