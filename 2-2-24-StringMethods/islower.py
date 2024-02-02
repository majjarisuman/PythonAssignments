# #islower()
word = "Rohit45"
print(word.islower())  #False

text = "python course training duration is 90 days"
print(text.islower())  #True

text1 = "rohit45"
print(f'"{text1}" is islower: {text1.islower()}')   #"Rohit45" is islower: True

#With space
text2 = "Rohit 45"
print(f'"{text2}" is islower: {text2.islower()}')   #"Rohit 45" is islower: False

#String with Special Characters
text3 = "Kohli@18"
print(f'"{text3}"" is islower :{text3.islower()}')   #"Kohli@18" is islower :False

#Numeric String
text4 ="12345"
print(f'"{text4}" is islower :{text4.islower()}')    #"12345" is islower :False

# # numeric string with space
text5 = "123 45"
print(f'"{text5}" is islower :{text5.islower()}')   #"123 45" is islower : False

#Non-islower String
text6 = "python course"
print(f'"{text6}" is islower :{text6.islower()}')   #"python course" is islower: :True

text7 = "Python"
print(f'"{text7} is islower :{text7.islower()}')   #"Python is islower :False