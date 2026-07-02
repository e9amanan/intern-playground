#parameters

def power(x, y=2):
    return x ** y

print(power(3, 3)) 

print(power(y=3, x=3))

def create_profile(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Extra positional args: {args}")
    print(f"Extra keyword args: {kwargs}")

create_profile("Alice", 25, "Engineer", location="NYC", active=True)

#Return Values
def get_min_max(numbers):
    
    return min(numbers), max(numbers)

lowest, highest = get_min_max([10, 20, 5, 40])
print(lowest)   
print(highest)


#SCOPE LEGB

x = "Global X"
len = "Wait, I just overwrote the built-in len function!" 

def outer_function():
    
    x = "Enclosing X"
    
    def inner_function():
        
        x = "Local X"
        
        
        print(x) 
        
    inner_function()

outer_function()

#Type Hints

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."