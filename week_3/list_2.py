#this is program that shows a list of my friends
#Date 26\02\24
#Name Abigael Mburu



friends = ["Chebet","Ivan","Nicole","Shante","Luke"]
for friend in friends:
    print(friend)

enemies = friends[:]


for enemy in enemies: #copy one list into another
    print(enemy)
    print("\n")

fruits = ["guava","mangoes","lemon","pawpaw","apple"]

print(fruits[0:3])

del fruits[0]

print(fruits)

print("\n")

squares = [] #initializing an empty list

for x in range(0,11):
    squares.append(x**2)

print(squares)
