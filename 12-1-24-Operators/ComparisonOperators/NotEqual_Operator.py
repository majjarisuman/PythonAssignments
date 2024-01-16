# Comparison operators are used to compare values and return Boolean results 

int_num1 = 3
int_num2 = 5
int_num3 = 3
int_num4 = 45
str_chr = "Rohit_45"
str_num = "45"
float_num = 45.00
bool_val1 = True
bool_val2 = False
list_ex = [12,21,31,1]
list_str = ["rohit","Kohli","Yuvi"] 
list_mix = ["rohit",45.08,True,10]

#------------------ Not Equal (!=) -----------------------
# print(int_num1!=int_num2)   #True
# print(int_num1!=str_num)   #True
# print(int_num1!=str_chr)    #True

# print(int_num1!=int_num3)    #False
# print(int_num4!=str_num)    #True
# print(int_num4!=float_num)   #False
# print(int_num4!=bool_val1)   #True
# print(int_num1!=list_ex)    #True

# print(str_chr!=str_num)   #True
# print(str_num!=int_num4)   #True
# print(str_chr!=float_num)  ##True
# print(str_chr!=str_chr)    #False
# print(str_chr!=bool_val1)   #True
# print(str_chr!=list_ex)   #True

# print(float_num!=bool_val2)   #True
# print(float_num!=list_ex)  #True
# print(float_num!=float_num)   #False

# print(bool_val1!=bool_val2)   #True
# print(bool_val1!=bool_val1)   #False
# print(bool_val1!=list_mix)    #True

# print(list_ex!=list_ex)   #False
# print(list_ex!=list_mix)   #True