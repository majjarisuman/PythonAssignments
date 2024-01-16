int_num1 = 15
int_num2 = 25
str_chr = "Rohit_45"
str_num = "45"
float_num = 45.08
bool_val = True
list_ex = [12,21,31,1]
list_str = ["rohit","Kohli","Yuvi"] 
list_mix = ["rohit",45.08,True,10]

##------------------------- Subtraction (-) --------------------------------
# print(int_num1,"-",int_num2,"=",int_num1-int_num2)   #15 - 25 = -10

# print(int_num1,"-",str_num,"=",int_num1-str_num)   #TypeError: unsupported operand type(s) for -: 'int' and 'str'

# print(int_num1,"-",float_num,"=",int_num1-float_num)   #15 - 45.08 = -30.08

# print(int_num1,"-",bool_val,"=",int_num1-bool_val)   #15 - True = 14

# print(int_num1,"-",bool_val,"=",int_num1-list_ex)   #TypeError: unsupported operand type(s) for -: 'int' and 'list'

# print(str_num-str_chr)    #TypeError: unsupported operand type(s) for -: 'str' and 'str'

# print(str_num-float_num)    #TypeError: unsupported operand type(s) for -: 'str' and 'float'

# print(str_num+bool_val)  #TypeError: can only concatenate str (not "bool") to str

# print(str_chr-list_str)   #TypeError: unsupported operand type(s) for -: 'str' and 'list'

# print(float_num-float_num)   #0.0

# print(float_num-bool_val)  #44.08

# print(float_num-list_ex)   #TypeError: unsupported operand type(s) for -: 'float' and 'list'

# print(bool_val-bool_val)  #0

# print(bool_val-list_ex)   #TypeError: unsupported operand type(s) for -: 'bool' and 'list'

# print(list_ex-list_ex)     #TypeError: unsupported operand type(s) for -: 'list' and 'list'

# # --------------------Addition (+) --------------------------------------
# result1 = int_num1+int_num2
# print(result1)       #40

# #addition with int and string
# result2 = int_num1+str_chr
# print(result2)    #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # #addition with int and string integer
# result3 = int_num1+str_num   
# print(result3)     #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# #addition wit int and float 
# result4 = int_num1+float_num
# print(result4)   #60.08

## addition with int and bool 

# result5=int_num1+bool_val
# print(result5)  #16

## addition with int and list 
# result6=int_num1+list_ex
# print(result6)   #TypeError: unsupported operand type(s) for +: 'int' and 'list'

##addition with str char and str int
# result7=str_chr+str_num
# print(result7)   #Rohit_4545

##addition with str and int
# result8 = str_num+int_num2
# print(result8)      #TypeError: can only concatenate str (not "int") to str

##addition witth str and float
# result9 = str_num+float_num
# print(result9)         #TypeError: can only concatenate str (not "float") to str

# ##addition with str and bool
# result10 = str_num+bool_val
# print(result10)         #TypeError: can only concatenate str (not "bool") to str

##addition with str and list
# result11 = str_num+list_str
# print(result11)

##addition with float and int
# print(float_num+int_num2)    #70.08

##addition with float and str
# print(float_num+str_num)     #TypeError: unsupported operand type(s) for +: 'float' and 'str'

##addition with float and bool
# print(float_num+bool_val)  #46.08

##addition with float and list
# print(float_num+list_mix)     #TypeError: unsupported operand type(s) for +: 'float' and 'list'

##addition bool and int
# print(bool_val+int_num2)      #26

##addition bool and str
# print(bool_val+str_num)    #TypeError: unsupported operand type(s) for +: 'bool' and 'str'

##addition bool and float
# print(bool_val+float_num)  #46.08

##addition bool and bool
# print(bool_val+bool_val)     #2

##addition bool and list
# print(bool_val+list_ex)        #TypeError: unsupported operand type(s) for +: 'bool' and 'list'


