L = [10,20,30,20,40,30,"MSR",50,"MSR"]

print(L.count("Rohit45"))   #0
print(L.count(10))     #1
print(L.count("MSR"))  #2
print(L.count("msr".upper)) #0
print(L.count("20"))    #0
print(L.count(20))    #2
print(L.count(40))    #1

# print(count(L)) #NameError: name 'count' is not defined
