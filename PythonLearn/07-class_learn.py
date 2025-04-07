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