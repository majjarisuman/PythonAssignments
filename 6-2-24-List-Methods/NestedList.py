List = [10,20,[30,40],50,60]

# print(List[2[1]:4])    #TypeError: 'int' object is not subscriptable
# print(List[2])    #[30, 40]

a=(List[2][1])    #40
b=(List[3])

print(a,b)  #40 50

