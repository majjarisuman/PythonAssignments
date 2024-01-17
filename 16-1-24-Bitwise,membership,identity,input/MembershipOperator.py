#------------ in -----------
e = 5
x="rom"
i = 14.45

# print(5 in x)   #TypeError: 'in <string>' requires string as left operand, not int
# print(6 in e)    #TypeError: argument of type 'int' is not iterable
# print(0.45 in i)    #TypeError: argument of type 'float' is not iterable

print('r' in x)   #True
print('rm' in x)   #False
print('or' in x)   #False


# ------------ Not In --------------------
# print(5 not in x)   #TypeError: 'in <string>' requires string as left operand, not int
# print(6 not in e)    #TypeError: argument of type 'int' is not iterable
# print(0.45 not in i)    #TypeError: argument of type 'float' is not iterable

print('r' not in x)   #False
print('rm' not in x)   #True
print('or' not in x)   #True

