# # float

# # Integer to float
# #------------------

# int1 = float(77)
# print(int1)   #77.0

# long_int = float(123456789012345678901234567890)
# print("long int to float : ",long_int)     #1.2345678901234568e+29

# mid_int = float(12345678901234567890)
# print("mid int to float : ",mid_int)       #1.2345678901234567e+19

# low_int = float(1234567890)
# print("low int to float : ", low_int)       #1234567890.0 

# #string to float 
# #-----------------

# str1 = float("123.45")
# print(str1)   #123.45

# str2 = float("99")
# print(str2)   # 99.0

# str3 = float("one")
# print(str3)     #ValueError: could not convert string to float: 'one'

# str4 = float("Rohit45")
# print(str4)       #ValueError: could not convert string to float: 'Rohit45'


# # Bool to float 
# # ---------------

# bool1 = float(True)
# print(bool1)     # 1.0
 
# bool2 = float(False)
# print(bool2)      # 0.0

# bool3 = float(bool("True"))
# print(bool3)        # 1.0
