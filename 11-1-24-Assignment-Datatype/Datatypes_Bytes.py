#------------------- Bytes --------------------

#byte is immutable , does not modifying after creation.
#bytes data type represent a group of byte numbers.
#byte data type allowed only 0 to 256.
#other than 256 will get error.
#allows duplicate values
#indexing allowed
#accepting only Integers and Bool(True or False).



s= [10,29,30,True,10]
b = bytes(s)
# print(type(b))    #<class 'bytes'>
# print(b)   #b'\n\x1d\x1e\x01\n'
# print(b[2])  #30
# print(b[:3])  #b'\n\x1d\x1e'

for i in b:
    print(i ,end= " ")   #10 29 30 1 10 
    
# b.append(10)  #AttributeError: 'bytes' object has no attribute 'append'
# b.add(20)    #AttributeError: 'bytes' object has no attribute 'add'

# s= [10,29,30,True,10,"m"]
# b = bytes(s)   #TypeError: 'str' object cannot be interpreted as an integer

print("\n",b[-2]) # 1
print(b[2])  # 30
