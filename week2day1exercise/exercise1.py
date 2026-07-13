class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def introduce(self)->str:
        return f"hi, I'm {self.name} and I'm {self.age} years old"
    
    def is_adult(self)-> bool:
        return self.age >= 18
    
person=Person("Alice",25)
print(person.introduce())
print(person.is_adult())