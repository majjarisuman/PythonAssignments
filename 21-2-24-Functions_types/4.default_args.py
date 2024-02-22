#------------- exp1 -----------
def greet(name, message="Hello"):
    return f"{message}, {name}!"

result1 = greet("Rohit")
result2 = greet("Virat", "Hi")
print(result1)    #Hello, Rohit!
print(result2)    #Hi, Virat!


# --------- exp2 ----------------
def power(base, exponent=2):
    return base ** exponent

result1 = power(3)
result2 = power(2, 4)
print(result1)   #9
print(result2)   #16


#-------------- EXP3 -----------------
def create_person(name, age=30, city="Unknown"):
    person = {"Name": name, "Age": age, "City": city}
    return person

person1 = create_person("Rohit")
person2 = create_person("Virat", 25, "New Delhi")
print(person1)
print(person2)

#---------- exp4 -----------------
def greet(name, message="Hello"):
    return f"{message}, {name}!"

result1 = greet(name="Rohit")
result2 = greet("Virat", message="Hi")
print(result1)    #Hello, Rohit!
print(result2)    #Hi, Virat!

