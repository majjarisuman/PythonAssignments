#Find the sum of all number from 1 to N 
summ = 0
Num = int(input("Enter N number"))

for n in range(1,Num+1):
    summ += n
print(summ)