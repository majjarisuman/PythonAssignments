#------- exp-1 -------------
#addition
#return
def add(a, b):
    return a + b

print(add(5,3))     #8
print(add(5,10))   #15


#print 
def add(a, b):
    print(a + b)
          
add(5,3)     #8
add(5,10)   #15


# ----------   exp2  -----------------
def Rectangle(length, width):
    return length * width

area = Rectangle(4, 6)
print("Rectangle Area:", area)    #Rectangle Area: 24


#----------   exp3 -----------------
def Fullname(first_name, last_name):
    return f"{first_name} {last_name}"

full_name = Fullname("Rohit", "Sharma")
print("Full Name:", full_name)            #Full Name: Rohit Sharma

full_name = Fullname("Virat", "Kohli")
print("Full Name:", full_name)            #Full Name: Virat Kohli


#------------  exp4  ------------------
def power(base, exponent):
    return base ** exponent

result = power(2, 3)
print("Result:", result)      #Result: 8


#-----------  exp5  --------------------
def date(day, month, year):
    print(day,"/",month,"/",year)

date(14, 2, 2024)    #14 / 2 / 2024

#---------exp ----------------------
def my_function(arg1,arg2,arg3,arg4):
    print(arg1,arg2,arg3,arg4)
    
my_function(10,20,30,40)  #10 20 30 40


#---------exp ------------------------
def my_function1(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
    
# my_function1(10,20,30)   #TypeError: my_function1() missing 1 required positional argument: 'num4'


#---------exp ------------------------
def my_function2(num1,num2):
    print(num1,num2,)
    
# my_function2(100,200,300)   #TypeError: my_function1() takes 2 positional arguments but 3 were given







