#this is a block of reusable code that performs a specific task - function



#standard libtrary functions/in- built fuctions
y = max(89, 45, 45, 78, 590)
print("The maximum value is", y)


x = min(75, 54, 32, 3, 32)
print("The minimum value is", x)


#User-defined Fuctions
def school():
    print("My coding School is eMobilis")


school() #calling a fuction

def add():
    a = 20
    b = 30
    print(a + b)

add()



#parameter/variable and AArguemebts and arguement
def multiply(num1,num2):
    print(num1*num2)
multiply(8,9)
multiply(10,2)
multiply(9,9)




def student(fullname, age, gender):
    print(fullname, age, gender)

student("Kimberly", 45, "Female")
student("victor", 78, "male")
student("Kim", 55, "male")


#assignment

def employee(fullname, position, salary, email):
    print(fullname, position, salary, email)

employee("Kim", 30, 2500, "kim676@gmail.com")
employee("ray", 78, 2598, "ray676@gmail.com")
employee("john", 94, 28900, "john676@gmail.com")
employee("jay", 39, 25790, "jay6@gmail.com")
employee("paul", 34, 255765, "paulz@gmail.com")