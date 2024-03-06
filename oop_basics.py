'''class=animal
object=dog
'''
'''import random
class xyz:
    #variables
    float_number=1.0
    #functions
    def random_function():
        return random.randrange(1,100)
    
c1=xyz    
print(c1.random_function)

class calculator:
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return b-a
    
    def division(a,b):
        return b/a
    
    def multiplication(a,b):
        return a*b
    
a=int(input("enter the number"))
b=int(input("enter the number"))
flag = input('Do you want to add,subtract, divide, multiply: ')
c1=calculator
if flag.lower() == 'add':
    print(c1.addition(a,b))
if flag.lower() == 'sub':
    print(c1.subtraction(a,b))
if flag.lower() == 'div':
    print(c1.division(a,b))
if flag.lower() == 'mul':
    print(c1.multiplication(a,b))'''


from datetime import datetime
class remainder:
    def remember_event():
        date_event = {}
        flag = True
        while flag:
            choice = input('Do you want to rememeber something: ')
            if choice.lower() == 'yes':
                date = input('Enter the important date: ')
                event = input('Enter the event for the date: ')
                date_event[date] =event
            if choice.lower() == 'no':
                flag = False
        return date_event
    
    def check_event(date_event):
        current_datetime = datetime.now()
        current_date = str(current_datetime.date())
        keys = list(date_event.keys())

        values = list(date_event.values())
        for value in keys:
            if  current_date == value:
                print(date_event[value])
        
rem= remainder
date_and_event =rem.remember_event()
print(date_and_event)
rem.check_event(date_and_event)



    
    
    
    
    
