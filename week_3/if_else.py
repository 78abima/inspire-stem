#this is a program which shows functions of "if"
#Date 26\02\24
#Name Abigae Mburu

age = 25
if age > 18 :
    print("you are allowed to drive")


salary = 45000
if salary > 30000 or salary < 50000 :
    salary = salary * 0.1 + salary
    print(salary)

home_county = "Kiambu"
if home_county == "Kiambu" or  "Nyeri":
    print("you get a bursary")


grade = 70
if grade > 84 and grade <= 90 : 
    print("you win a calculator")

elif grade >= 50 and grade <= 83:
    print("you win a mathematical set")
else :
    print("you get nothing")
 




