int_num1 = 3
int_num2 = 5
str_chr = "Rohit_45"
str_num = "45"
float_num = 45.08
bool_val = True
list_ex = [12,21,31,1]
list_str = ["rohit","Kohli","Yuvi"] 
list_mix = ["rohit",45.08,True,10]

# ------------------------------- Modulus (%) ---------------------------------------
# print(int_num2%int_num1)   #2
# print(int_num1%str_num)  #TypeError: unsupported operand type(s) for %: 'int' and 'str'
# print(float_num%int_num1)   #0.0799999999999983
# print(int_num1%float_num)   #3.0
# print(int_num1%bool_val)    #0
# print(int_num1%list_ex)    #TypeError: unsupported operand type(s) for %: 'int' and 'list'
# print(str_num%float_num)    #TypeError: not all arguments converted during string formatting
# print(str_num%bool_val)       #TypeError: not all arguments converted during string formatting
# print(str_num%int_num1)     #TypeError: not all arguments converted during string formatting
# print(str_chr%list_mix)      #Rohit_45 (doubt)
# print(str_num%list_mix)       #45
# print(float_num%bool_val)     #0.0799999999999983
# print(float_num%list_str)      #TypeError: unsupported operand type(s) for %: 'float' and 'list'
# print(bool_val%list_str)     #TypeError: unsupported operand type(s) for %: 'bool' and 'list'
# print(list_ex%list_ex)     #TypeError: unsupported operand type(s) for %: 'list' and 'list'