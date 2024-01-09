# #Type casting in python.

# #String datatype to Int type converting.
# #-------------------------------------------

# a=int("45")   
# print("String value 45 to int :",a)   #  45

# a3=int("one")
# print(a3)          #ValueError: invalid literal for int() with base 10: 'one'

# a1 = int("Rohit45")  #ValueError: invalid literal for int() with base 10: 'Rohit45'
# print(a1)

# a2 = int("45Rohit")
# print(a2)        #ValueError: invalid literal for int() with base 10: '45Rohit'

# a4="123.45"
# print(int(a4))     #ValueError: invalid literal for int() with base 10: '123.45'

# a44=int(float("45.08"))
# print("strint to float ,Float(45.08) to int  : ",a44)   #45

# a8 = int("True")
# print(a8)    #ValueError: invalid literal for int() with base 10: 'True'

# #convert float to int
# #----------------------

# a5 = int(18.08)
# print("float to int, value 18.08 = ",a5)   #18

# a6= int(99.99)
# print("float to int, value 99.99 = ",a6)  #99

# a7 = int(float("123.45"))
# print("String to float,float to int :",a7)    #123

# #Bool to int 
# #-------------
# a9 = int(bool("True"))   #str to bool , bool to int
# print(a9)   # o/p= 1 

# a10 = int(True)
# a11 = int(False)
# print(a10)   # 1
# print(a11)   # 0 
