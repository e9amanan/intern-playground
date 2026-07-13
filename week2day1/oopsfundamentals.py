"""
OOP fundamentals (from scratch)

    Basic classes
        Define a simple Person class with __init__, attributes, and methods
        Instance vs class attributes
        self keyword and instance methods
    Special methods (dunder methods)
        __init__: constructor
        __repr__ and __str__: string representations
        __eq__: equality comparison
    Encapsulation
        Public vs "private" (underscore convention) attributes
        @property decorator for computed attributes and getters/setters
"""

class Person:

    species = "homo sapiens"            #class atribute

    def __init__(self,name: str, age: int,first_name:str,last_name:str):    #instance attribute
        self.first_name=first_name
        self.last_name=last_name
        self.name=name
        self._age =  age

    @property                                       #encapsulation of computed attibute
    def full_name(self) -> str:

        return f"{self.first_name}{self.last_name}"
    
    @full_name.setter
    def full_name(self,name:str):
        parts=name.split(" ")
        if len(parts)<2:
            raise ValueError("you must providen both first name and last name")
        
        self.first_name=parts[0]
        self.last_name=" ".join(parts[1:])
 
 
    #dunder
    def __repr__(self)->str:
        return f"Person(name='{self.name}', age={self._age})"
    
    def __str__(self)->str:
        return f"{self.name},{self.age} years old"
    

    def __eq__(self, other: object)-> bool:
        if not isinstance(other,Person):
            return NotImplemented
        return self.name == other.name and self._age == other.age
