int_num1 = 3
int_num2 = 5
str_chr = "Rohit_45"
str_num = "45"
float_num = 45.08
bool_val = True
list_ex = [12,21,31,1]
list_str = ["rohit","Kohli","Yuvi"] 
list_mix = ["rohit",45.08,True,10]

#----------------------- Exponentiation () ** -----------------------------------------
# print(int_num1**int_num2)   #243
# print(int_num1**str_num)      #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
# print(str_chr**int_num1)   #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# print(int_num1**float_num)   #3.22571625539158e+21
# print(int_num1**bool_val)  #3
# print(int_num1**list_ex)   #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'list'
# print(str_num**float_num)   #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# print(str_num**bool_val)     #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
# print(str_num**str_num)   #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
# print(str_num**float_num)   #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# print(str_chr**bool_val)     #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
# print(str_chr**list_ex)     #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'list'
# print(float_num**float_num)   #3.644135730222331e+74
# print(float_num**bool_val)     #45.08
# print(float_num**str_num)     #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'str'
# print(float_num**list_ex)     #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'list'
# print(bool_val**bool_val)    #1
# print(bool_val**list_ex)    #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'list'
# print(list_ex**list_ex)    #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'
