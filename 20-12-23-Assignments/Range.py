#---------------- Range ------------------

#range Data Type represents a sequence of numbers.
#range datatype is Immutable.
#we can't add,upated,delete elements in range.
#duplicates are not allowed
#indexing allowed
#slicing allowed

r = range(10)
# print(r)     #range(0, 10)

# for i in range(10):
#     print(i, end = " ")     #0 1 2 3 4 5 6 7 8 9
    
# for k in range(0:20:2):     
#     print(k , end = " ")    #SyntaxError: invalid syntax
    
# for k in range(0,20,2):     
    # print(k , end = " ")    # 0 2 4 6 8 10 12 14 16 18 

# print(r[3])    #3
# print(r[0:11])   #range(0, 10)

# print(range(a,m))  #NameError: name 'a' is not defined