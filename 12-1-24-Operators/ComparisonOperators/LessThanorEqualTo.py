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

#------------------ LLess Than or Equal To (<==) -----------------------
# print(int_num1<=int_num2)   #True
# print(int_num1<=str_num)   #TypeError: '<=' not supported between instances of 'int' and 'str'
# print(int_num1<=str_chr)    #TypeError: '<=' not supported between instances of 'int' and 'str'

# print(int_num1<=int_num3)    #True
# print(int_num4<=str_num)    #TypeError: '<=' not supported between instances of 'int' and 'str'
# print(int_num4<=float_num)   #True
# print(int_num4<=bool_val1)   #False
# print(int_num1<=list_ex)    #TypeError: '<=' not supported between instances of 'int' and 'list'