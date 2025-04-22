class Dog:
    '''desc dog profile and func'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(f'The dog {self.name} is sitting.')

    def roll(self):
        print(f'The dog age is {self.age}, is rolling')
    
dog = Dog('trump','13')
dog.sit()


class Car:
    '''modify class profile'''
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.mile=0
    
    def desc_name(self):
        '''print total name of car'''
        long_name=f'{self.name},{self.model},{self.year}'
        return long_name
    
    def read_mile(self):
        '''print miles'''
        print(f'The car mile is {self.mile}')

    def update_mile(self,mileage):
        '''modify mile'''
        if(mileage>self.mile):
            self.mile=mileage
        else:
            print('You can\'t roll back mile.')
    
    def incre_mile(self,add_miles):
        '''incredible miles'''
        if(add_miles>=0):
            self.mile+=add_miles
        else:
            print('You can\'t add negative num.')

my_car=Car('sky','vechiel',2019)
print(my_car.desc_name())
my_car.read_mile()
# direct modify profile
my_car.mile=2025
print(my_car.mile)

# modify by func
my_car.update_mile(202504)
my_car.read_mile()

# modify by func
my_car.update_mile(202503)
my_car.read_mile()

# incredible negative miles
my_car.incre_mile(-10)
my_car.read_mile()
# incredible negative miles
my_car.incre_mile(10)
my_car.read_mile()

# practice random modoule
import random
class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        result = random.randint(1,self.sides)
        return result
    def roll_times(self,times):
        i=0
        while i < times:
            print(self.roll_die())
            i+=1
die = Die(20)
die.roll_times(10)