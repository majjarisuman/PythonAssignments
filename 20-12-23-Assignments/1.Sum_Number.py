# Find the sum of all numbers from 1 to N.

num = int(input("Enter a N number:- "))
sum = 0
for i in range(num+1):
  sum+=i
print(sum)