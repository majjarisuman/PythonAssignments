#--------------------- Set --------------------

# set is Mutable datatype.
# we can add elements but we can't update elememnts
# insertion order is not preserved.
#duplicates not allowed.
# heterogenious are allowed
#unorder elements.
#no indexing
# no slicing

s = {10,12.4,"Rohit",2,33}
# print(type(s))    #<class 'set'>

# print(s)   #{33, 2, 10, 'Rohit', 12.4}   #insertion order not preserved.

# print(s[2])    #TypeError: 'set' object is not subscriptable

# s[2] ="msr"   #TypeError: 'set' object does not support item assignment

# s.add(10)
# print(s)   #duplicate values not updatating

s.add("Msr")
print(s)   #{33, 2, 'Msr', 10, 12.4, 'Rohit'}   #un-order
