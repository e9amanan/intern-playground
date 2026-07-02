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



location=(40.7128,-74.0060)

lat,lon = location
print(f"latitutude of london is {lat}")

