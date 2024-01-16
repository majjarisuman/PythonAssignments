int_num1 = 3
int_num2 = 5
str_chr = "Rohit_45"
str_num = "45"
float_num = 45.08
bool_val = True
list_ex = [12,21,31,1]
list_str = ["rohit","Kohli","Yuvi"] 
list_mix = ["rohit",45.08,True,10]

##----------------------- Division (/) ----------------------------------------
# print(int_num2/int_num1)   #1.6666666666666667
# print(int_num1/str_num)    #TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print(int_num1/float_num)    #0.06654835847382432
# print(int_num1/bool_val)     #3.0
# print(int_num1/list_ex)      #TypeError: unsupported operand type(s) for /: 'int' and 'list'
# print(str_chr/bool_val)     #TypeError: unsupported operand type(s) for /: 'str' and 'bool'
# print(str_chr/float_num)     #TypeError: unsupported operand type(s) for /: 'str' and 'float'
# print(str_chr/list_ex)      #TypeError: unsupported operand type(s) for /: 'str' and 'list'
# print(float_num/float_num)  #1.0
# print(float_num/bool_val)     #45.08
# print(list_ex/float_num)        #TypeError: unsupported operand type(s) for /: 'list' and 'float'
# print(bool_val/bool_val)   #1.0
# print(bool_val/list_ex)     #TypeError: unsupported operand type(s) for /: 'bool' and 'list'
# print(list_ex/list_ex)        #TypeError: unsupported operand type(s) for /: 'list' and 'list'