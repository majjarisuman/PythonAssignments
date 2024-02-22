# Keyword arguments in Python allow you to pass values to a function using the parameter names

#---------- exp1 --------------------
def greet(name, msg):
    return f"{msg}, {name}!"

result = greet(name="Rohit",msg="Hello")   #
print(result)       #Hello, Rohit!

result1 = greet(name="Virat",msg="Hi ")
print(result1)      #Hello, Virat!



#print
def greet(name, msg):
    print(msg+" "+name)

greet(name="Rohit",msg="Hello")   #Hello Rohit

greet(name="Virat",msg="Hi")    #Hi Virat

#--------------- exp2 ---------------------- 
def display(name,age,city):
    print(f"Details: name = {name},age = {age},city = {city}")

display(age = 35 ,name = "Rohit" ,city = "Mumbai")    #Details: name = Rohit,age = 35,city = Mumbai
display(name="Virat",age = 34,city="Delhi")


#-----------  exp3  --------------------------
def fullname(Fname,Lname):
    print(Fname+Lname)
fullname(Lname="Sharma",Fname="Rohit")
# fullname(Lname="Virat")      #TypeError: fullname() missing 1 required positional argument: 'Fname'
# fullname(Fname="rohit",Lname=45)   #TypeError: can only concatenate str (not "int") to str(def fullname(Fname+Lname):)

