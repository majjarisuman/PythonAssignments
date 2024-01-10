##Bool

##int to bool
##-----------

# int1 = bool(45)
# print(int1)    # True

# int2 = bool(0)
# print(int2)    #False

# long_int1 = bool(123456789012345678901234567890)
# print(long_int1)   #True

# long_int2 = bool(09)
# print(long_int2)   
# '''output : Syntax Error: leading zeros in decimal integer literals are not permitted; 
# use an 0o prefix for octal integers '''

##float to bool

# float1 = bool(123.456)
# print(float1)   #True 

# float2 = bool(000.456)
# print(float2)   #True 

# float3 = bool(000.000)
# print(float3)   #False 

# float4 = bool(-23.456)
# print(float4)   #True 

# float5 = bool(-0.456)
# print(float5)   #True 

##string to bool
##----------------

# str1 = bool("Hello world")
# print(str1)   #True

# str2 = bool(" ")
# print(str2)   #True

# str3 = bool("")
# print(str3)   # False

# str4 = bool("123")
# print(str4)   #True