L = [10,20,30,20,40,30,"MSR","A",50,"MSR"]

print(len(L))   #9
print(len(L[6]))   #3
print(len(L[7]))   #1

# print(len(L[2]))     #TypeError: object of type 'int' has no len()
# print(L.len(L))    #AttributeError: 'list' object has no attribute 'len'

l=[10,20,30]
l.append([40,50])
print(l)    #[10, 20, 30, [40, 50]]

print(len(l))   #4

r = [10,20,["MSR","Rohit45"]]
print(r)     #[10, 20, ['MSR', 'Rohit45']]

print(len(r))   #3

print(len(r[2]))  #2

print(len(r[2][1]))  #7

