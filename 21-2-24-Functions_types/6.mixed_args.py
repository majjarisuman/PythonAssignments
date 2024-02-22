#---------  exp1  -------------------------
def my_function(name,age,wish1,wish2):
    print(name,age,wish1,wish2)
    
my_function("rohit",35,wish1="Hello",wish2="Hitman")           #rohit 35 Hello Hitman


#---------  exp2  -------------------------
def my_function1(name,age,wish1,wish2):
    print(name,age,wish1,wish2)
    
my_function1(wish1="Hello",name="rohit",wish2="Hitman",age=35)   #rohit 35 Hello Hitman


# #---------  exp3  -------------------------
# def my_function2(name,age,wish1,wish2):
#     print(name,age,wish1,wish2)
    
# my_function2(name="rohit",age=35,"Hello","Hitman")    #SyntaxError: positional argument follows keyword argument
# #   [Note* :- Positional argument cannot appear after keyword arguments]                                                         


#---------  exp4  -------------------------
def my_function3(name,age,wish1,wish2="Hit-Man"):
    print(name,age,wish1,wish2)
    
my_function3(wish1="Hello",name="rohit",age=35)     #rohit 35 Hello Hit-Man

#---------  exp5  -------------------------
def my_function4(name,age,wish1,wish2="Hit-Man"):     
    print(name,age,wish1,wish2)
    
my_function4("rohit",35,wish1="Hello ",wish2="Good-morning")     #rohit 35 Hello  Good-morning[#updated default value ]


# #---------  exp6  -------------------------
# def my_function5(name="Rohit Sharma",age,wish1,wish2):     
#     print(name,age,wish1,wish2)

# my_function5(age=35,wish1="Hi",wish2="Hello")   #SyntaxError: parameter without a default follows parameter with a default
# #Non-default argument follows default argument


#---------  exp7  -------------------------
def my_function6(name,age,*wish1,wish2="Hit-Man"):     
    print(name,age,wish1,wish2)
    
# my_function6("rohit sharma",35,city="Mumbai")    #TypeError: my_function6() got an unexpected keyword argument 'city'


#---------  exp8  -------------------------
def my_function7(name,age,*wish1,wish2="Hit-Man"):     
    print(name,age,wish1,wish2)
    
# my_function6("rohit sharma",35,wish1="Mumbai")      #TypeError: my_function6() got an unexpected keyword argument 'wish1'


#---------  exp9  -------------------------
def my_function8(name,age,*wish1,wish2="Hit-Man"):     
    print(name,age,wish1,wish2)
    
my_function6("rohit sharma",35,"Mumbai","Delhi")        #rohit sharma 35 ('Mumbai', 'Delhi') Hit-Man


#---------  exp10  -------------------------
def my_function9(*wish1,name,age,wish2="Hit-Man"):     
    print(name,age,wish1,wish2)
    
my_function6("rohit sharma",35,"Goa","Delhi")   #my_function6("rohit sharma",35,"Goa","Delhi")


