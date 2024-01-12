#------------- Tuple ------------------

# tuple is Immutable Type.
# Immutable means we can't add ,upadte ,delete elements after tuple creation.
# Duplicates are allowed.
# Tuple is heterogeneous type ,it means allows diff dattaype data in tuple.
# Insertion order is preserved.
# Indexing allowed.
# Slicing allowed.
# Tuple Should be enclosed within Parenthesis ().

tpl = (10,24,"Rohit",True,10)
print(tpl)     #(10, 24, 'Rohit', True, 10)

#adding new value  #but tuple is immutable
# tpl.append(10.4)     #AttributeError: 'tuple' object has no attribute 'append'

# #Indexing
# print(tpl[1])   #24
# print(tpl[-3])   #Rohit

# #Slicing
# print(tpl[::])    #(10, 24, 'Rohit', True, 10)
# print(tpl[::-1])  #(10, True, 'Rohit', 24, 10)

# print(tpl*3)    #(10, 24, 'Rohit', True, 10, 10, 24, 'Rohit', True, 10, 10, 24, 'Rohit', True, 10)

# print(tpl*tpl)   #TypeError: can't multiply sequence by non-int of type 'tuple'

print(tpl+tpl)    #(10, 24, 'Rohit', True, 10, 10, 24, 'Rohit', True, 10)