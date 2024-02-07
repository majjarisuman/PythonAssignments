L = [10,20,30,20,40,30,"MSR","A",50,"MSR"]

print(len(L))  #10  #len starts from 1

print(L.index(10)) #0   #index starts from zero (0)

print(L.index("MSR"))   #6      #first occurence

print(L.index("MSR",7))   #9

# print(L.index("Rohit45"))   #ValueError: 'Rohit45' is not in list

# print(L.index(0))   #ValueError: 0 is not in list

