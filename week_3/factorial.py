#this is a program to show factorials
#Date 26/02/24
#Name Abigael Mburu

factorial_nums = 1
max_value = int(input("enter the max value :"))

for x in range(1,max_value + 1):
    factorial_nums= factorial_nums * x
    print(factorial_nums)

#printing even numbers
for i in range (0,20,2):
    print(i)

#printing odd numbers
for i in range (1,20,2):
    print(i)