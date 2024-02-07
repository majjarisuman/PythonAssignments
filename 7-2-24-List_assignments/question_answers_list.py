#1 ------------  write down 4*4 matrix ?  
x=[[10,20,30,40],[50,60,70,80],[90,100,110,120],[130, 140, 150, 160]]
for i in x:
    for j in i:
        print(j, end=" ")  
    print() 

#2----------  compare string elements by using sort ?
names = ["Rohit","Kohli","Gill","Pant"]
names.sort()
print(names)     #['Gill', 'Kohli', 'Pant', 'Rohit']

#3---------------  print odd numbers in the range 0 to 30
l =  [i for i in range(0,31) if i%2!=0 ]
print(l)        
#o/p:- [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]


#4-----------  req 2*1 2*2 2*3 2*4 2*5(list comperhensive)
n = [2*i for i in range(1,6)]
print(n)    #[2, 4, 6, 8, 10]


#5-------------- words=['balaya','shafi','chiru']
# expected output/: [b,s,c]
words = ['balaya','shafi','chiru']
word = []
for i in words:
    word.append(i[0])
print(word)                #['b', 's', 'c']

#---- 2nd type
words = ['balaya','shafi','chiru']
word =[i[0] for i in words ]
print(word)     #['b', 's', 'c']

#6----- write a program to display unique vowels present in the user entered words ?
# vowels=['a','e','i'.'o','u']

vowels = ['a', 'e', 'i', 'o', 'u']
words = input("Enter words : ").split()
unique_vowels = set()

for word in words:
    for char in word.lower():
                if char in vowels:
                       unique_vowels.add(char)

print("Unique", unique_vowels)



