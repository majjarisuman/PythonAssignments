##-------------------- Dict Datatype ----------------

#represent a group of values as key-value pairs
# Keys always unique , not duplicate
# values can be duplicated.
# dict is mutable , order is not preserved

d = {}
# print(type(d))    #<class 'dict'>

# d["a"]= 100
# d["a"] = 200
# print(d)      #{'a': 200}
# d[10] = "Rohit"
# d[11] = "Msr"
# d[12] = "Rohit"
# print(d)           #{'a': 200, 10: 'Rohit', 11: 'Msr', 12: 'Rohit'}

# print(d[0])    #KeyError: 0