L = [10,20,30,40]

# L.insert(50)    #TypeError: insert expected 2 arguments, got 1
# print(L)   

# L.insert("MSR",50)    #TypeError: 'str' object cannot be interpreted as an integer   
# print(L)           

L.insert(4,50)
print(L)      #[10, 20, 30, 40, 50]

L.insert(1,20.25)
print(L)       #[10, 20.25, 20, 30, 40, 50]

L.insert(60,60)
print(L)          #[10, 20.25, 20, 30, 40, 50, 60]

L.insert(60,"MSR")
print(L)             #[10, 20.25, 20, 30, 40, 50, 60, 'MSR']