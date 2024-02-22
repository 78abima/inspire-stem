#strings in python
#Date 22/02/24
#Name Abigael Mburu

city = "nairobi" 

print(city[0]) # first character
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[-1]) # a
print(city[-2]) # last character

#convert to uppercase

print(city)
print("\n") # prints a new line
print(city.upper())

name = "ABIGAEL MBURU"
print(name)
print(name.lower()) # converts strings to lower cases

town = "   Naivasha   "

print(town)
print("\t") # new tab
print(town.strip())

#add two strings

f_name = "Abigael"
s_name = "Mburu"

full_name = f_name + s_name

print(full_name)

# replacing a character

fruit = "orangeoooo"

print(fruit.replace("o" , "y"))

subject = "physical,sciences"

print(subject.split(" ,"))

age = 18
height = 1.2

print("I am {0} years old and {1} meters tall "  .format(age,height))

