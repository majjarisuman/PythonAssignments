#-------------------   append()--------------------------------------------
L = [10,20,30,40]

L.append(50)
print(L)        #[10, 20, 30, 40, 50]

L.append(60)
print(L) #[10, 20, 30, 40, 50,60]

L.append([70,80])
print(L)   #[10, 20, 30, 40, 50, 60, [70, 80]]

L.append("Rohit45")
print(L)        #[10, 20, 30, 40, 50, 60, [70, 80], 'Rohit45']

# print(L[6[1]])   #TypeError: 'int' object is not subscriptable

# L.append(70,80)    #TypeError: list.append() takes exactly one argument (2 given)



#------------------------  extend() -----------------------------------------------------
L = [10,20,30,40]

L.extend("MSR")
print(L)      #[10, 20, 30, 40, 'M', 'S', 'R']

L.extend(["MSR"])
print(L)          #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR']

# L.extend(50,60,70)
# print(L)           #TypeError: list.extend() takes exactly one argument (3 given)

L.extend([50,60,70])
print(L)             #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR', 50, 60, 70]

L.extend(["Rohit45","Kohli18"])
print(L)             #[10, 20, 30, 40, 'M', 'S', 'R', 'MSR', 50, 60, 70, 'Rohit45', 'Kohli18']

#-------------------- insert() ------------------------------------------------------
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

#--------------------- pop() vs remove() ---------------------------------------------
#pop()  function removes the last element or item in a list.
#       element based on the index given.

L = [10,20,30,40,"MSR","A","B"]
a=L.pop()
print(a)   #B
print(L)   #[10, 20, 30, 40, 'MSR', 'A']

b=L.pop(4)
print(b)   #MSR
print(L)   #[10, 20, 30, 40, 'A']

# print(L.pop("A"))    #TypeError: 'str' object cannot be interpreted as an integer

# print(L.pop(15))     #IndexError: pop index out of range

print(L)    #[10, 20, 30, 40, 'A']
print(L.pop(-1))   #A

# print(L.pop(-10))    #IndexError: pop index out of range
print(L)     #[10, 20, 30, 40]


#---------------------- Remove() -----------------------------------
#remove() function removes the first occurrence of the specified element.
#          it does not return any value.

L = [10,20,30,40,"MSR","A","B"]

# print(L.remove())   #TypeError: list.remove() takes exactly one argument (0 given)

# print(L.remove(2))    #ValueError: list.remove(x): x not in list

print(L.remove("MSR"))   #None
print(L)     #[10, 20, 30, 40, 'A', 'B']

print(L.remove(20))     #None
print(L)    #[10, 30, 40, 'A', 'B']

# print(L.remove(30,40))    #TypeError: list.remove() takes exactly one argument (2 given)

# print(L.remove([30,40]))   #ValueError: list.remove(x): x not in list

l = [10,20,30,20,20,40,"MSR","A","B"]

l.remove(20)
print(l)         #[10, 30, 20, 20, 40, 'MSR', 'A', 'B']

l.remove(20)
print(l)         #[10, 30, 20, 40, 'MSR', 'A', 'B']

#------------------- count() -----------------------------------------
L = [10,20,30,20,40,30,"MSR",50,"MSR"]

print(L.count("Rohit45"))   #0
print(L.count(10))     #1
print(L.count("MSR"))  #2
print(L.count("msr".upper)) #0
print(L.count("20"))    #0
print(L.count(20))    #2
print(L.count(40))    #1

# print(count(L)) #NameError: name 'count' is not defined

#------------------------ index() --------------------------------------
L = [10,20,30,20,40,30,"MSR","A",50,"MSR"]

print(len(L))  #10  #len starts from 1

print(L.index(10)) #0   #index starts from zero (0)

print(L.index("MSR"))   #6      #first occurence

print(L.index("MSR",7))   #9

# print(L.index("Rohit45"))   #ValueError: 'Rohit45' is not in list

# print(L.index(0))   #ValueError: 0 is not in list

#-------------------------  len() function -------------------------------
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

#---------------- question and answer ------------------------------
#Q:- print 40,50 in a given list ? 

List = [10,20,[30,40],50,60]

# print(List[2[1]:4])    #TypeError: 'int' object is not subscriptable
# print(List[2])    #[30, 40]

a=(List[2][1])    #40
b=(List[3])

print(a,b)  #40 50





