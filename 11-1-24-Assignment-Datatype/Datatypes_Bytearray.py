#--------------- ByteArray ------------------------

#Bytearray is mutable , we can modify.
#bytearray allows duplicates.

#byte data type allowed only 0 to 256.
#other than 256 will get error.
#indexing allows.
#insertion order preserved
#Allows duplicates.
#accepting only Integers and Bool(True or False).

s=[10,122,10]
ba = bytearray(s)
# print(type(s))    #<class 'list'>
# print(type(ba))   #<class 'bytearray'>

ba[1] = 22
# print(ba)   #bytearray(b'\n\x16\n')
# ba[3] = 55  #IndexError: bytearray index out of range
ba.append(43)

# for i in ba:
#     print(i, end= " ")    #10 22 10 43 
    
# print(ba[-1]) #-43
# print(ba[::])    #bytearray(b'\n\x16\n+')

# for i in ba[:2]:
#     print(ba, end= " ")   #bytearray(b'\n\x16\n+') bytearray(b'\n\x16\n+')

# ba.append(257)   #ValueError: byte must be in range(0, 256)
ba.append(43)

print(ba[-3])   #10

# for i in ba:
#     print(i, end= " ")      #10 22 10 43 43 

# ba.append("Rohit")    #TypeError: 'str' object cannot be interpreted as an integer
# ba.append(10.5)  # TypeError: 'float' object cannot be interpreted as an integer
ba.append(False)   # False means 0(zero)

for i in ba:
    print(i, end= " ")      #10 22 10 43 43 0
