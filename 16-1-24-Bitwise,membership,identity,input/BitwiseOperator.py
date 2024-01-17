#-------------------- BitWise -----------------------------------------
# These operators are applicable only for int and boolean types.
# By mistake if we are trying to apply for any other type then we will get Error.

# #----------- &,|,^,~,<<,>>  ------------------------

a,b,c,d = 5,3,6,8
m = True
k = False
x="rom"
y="ram"

#------------ Bitwise AND (&) --------------------
# result = a & b
# print(result)   #1

# result1 = c&d
# print(result1)   #0

# result2 = a&c
# print(result2)   #4

# result3 = b&d
# print(result3)   #0

# print(x&y)  #TypeError: unsupported operand type(s) for &: 'str' and 'str'
# #note :- bitwise support for int and bool only
# print(m&k)   #False
# print(m&m)   #True
# print(k&k)   #False

# #------ Bitwise OR (|) ----------------
# print(a|b)   #7
# print(c|d)   #14
# print(a|c)   #7
# print(b|d)   #11
# print(x|y)  #TypeError: unsupported operand type(s) for |: 'str' and 'str'
# print(a|x)   #TypeError: unsupported operand type(s) for |: 'int' and 'str'
# print(a|m)    #5

# #---------------- Bitwise XOR (^) --------------------
# print(a^b)   #6
# print(c^d)   #14
# print(a^c)   #3
# print(b^d)   #11
# print(x^y)  #TypeError: unsupported operand type(s) for ^: 'str' and 'str'
# print(a^x)   #TypeError: unsupported operand type(s) for ^: 'int' and 'str'
# print(a^m)    #4

#--------------------- Bitwise NOT (~) -----------------------
a,b,c,d = 5,3,6,8
m = True
k = False
x="rom"
y="ram"
# op1 = ~a
# op2 = ~b
# op3 = ~c
# op4 = ~d
# op5 = ~m
# op6= ~k
# op7 = ~x   #TypeError: bad operand type for unary ~: 'str'
# op8 = ~y     #TypeError: bad operand type for unary ~: 'str'

# print(op1)  #-6
# print(op2)    #-4
# print(op3)    #-7
# print(op4)      #-9
# print(op5)     #-2
# print(op6)     #-1
# print(op7)   #TypeError: bad operand type for unary ~: 'str'
# print(op8)  #TypeError: bad operand type for unary ~: 'str'


# #-------------- Left Shift (<<) ---------------
a,b,c,d = 5,3,6,8
m = True
k = False
x="rom"
y="ram"

# print(a<<b)   #40
# print(c<<d)   #1536
# print(a<<c)   #320
# print(b<<d)   #768
# print(a<<m)    #10
# print(x<<y)  #TypeError: unsupported operand type(s) for <<: 'str' and 'str'
# print(a<<x)   #TypeError: unsupported operand type(s) for <<: 'int' and 'str'

# #------------- Right Shift (>>) --------------
a,b,c,d = 5,3,6,8
m = True
k = False
x="rom"
y="ram"

# print(a>>b)   #0
# print(c>>d)   #0
# print(a>>c)   #0
# print(b>>d)   #08
# print(a>>m)    #2
# print(x>>y)  #TypeError: unsupported operand type(s) for >> 'str' and 'str'
# print(a>>x)   #TypeError: unsupported operand type(s) for >> 'int' and 'str'





