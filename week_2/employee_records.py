#This is a program to show the records of an employee
#Date 21/02/24
#Name Abigael Mburu

e_name = input("enter the employee's name")
e_age = input("enter the employee's age")
e_salary = int(input("enter the employee's salary"))
e_bonus = float(input("enter the employee's bonus"))
percentange =(30/100) 

s_increase =(e_salary + (e_salary * percentange))

print("enter the employee's name : " , e_name)
print("enter the employee's age: " , e_age)
print("enter the employee's salary : " , e_salary)
print("enter the employee's bonus : " , e_bonus)
print("enter the employee's new salary : " , s_increase)

e_deduction = int(input("enter the deduction"))
new_bonus =(e_bonus - e_deduction)

print("the solution : " , new_bonus)
