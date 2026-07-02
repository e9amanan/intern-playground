#string

text="python"

print(text[0:3])
print(text[3:])
print(text[:3])
print(text[::-1])
print(text[::2])
print(text[::2])


age = 25
name ="alice"
print(f"my name is {name} and in 5 years i will be {age+5}")

sentence="lets learn python today"
words=sentence.split(" ")
print(words)


yo=sentence.split("e")
print(yo)

csv=",".join(words)
print(csv)

messy=" hello world  how are you   "
clean=messy.strip()
print(clean)

#lists 
numbers=[1,2,3,4,5]

doubles = [n*2 for n in numbers]
print(doubles)

evens = [n*2 for n in numbers if n % 2 ==0]
print(evens)

print(numbers[0:2])

numbers.append([3,4])
print(numbers)

numbers.extend([3,4])
print(numbers)

nums=[5,1.9]

new=sorted(nums)
print(new)
print(nums)

nums.sort()
print(nums)


#tupple

location=(40.7128,-74.0060)

lat,lon = location
print(f"latitutude of london is {lat}")

from collections import namedtuple

color=namedtuple("color", ["red","green","blue"])

pure_red=color(red=255,green=0,blue=0)

print(pure_red.red)

#dictionaries

employee={"name":"sarah","age":28,"department":"engineering"}

employee["salary"]=9000
employee["age"]=25

location=employee.get("location")
print(location)

for key in employee.keys():
    print(key)

for value in employee.values():
    print(value)

for key,value in employee.items():
    print(f"employees{key} is {value}")

 
numbers = [1, 2, 3, 4]
squares = {num: num * num for num in numbers}
print(squares)

#sets
unique_numbers = {1, 2, 3, 3, 3, 4}
print(unique_numbers)

empty_set = set()

allowed_users_list = ["alice", "bob", "charlie"]
allowed_users_set = {"alice", "bob", "charlie"}

user = "bob"
if user in allowed_users_set:
    print(f"{user} is allowed in!")


frontend = {"Alice", "Bob", "Charlie"}
backend = {"Charlie", "David", "Eve"}

all_devs = frontend | backend
print(all_devs)

fullstack = frontend & backend
print(fullstack)

pure_frontend = frontend - backend
print(pure_frontend)

specialists = frontend ^ backend
print(specialists)


