# #isalpha()
alpha = "Rohit45"
print(alpha.isalpha())  #False

text = "Python course training duration is 90 days"
print(text.isalpha())  #False

text1 = "Rohit45"
print(f'"{text1}" is alphabetic: {text1.isalpha()}')   #"Rohit45" is alphabetic: False

#With space
text2 = "Rohit 45"
print(f'"{text2}" is alphabetic: {text2.isalpha()}')   #"Rohit 45" is alphabetic: False

#String with Special Characters
text3 = "Kohli@18"
print(f'"{text3}"" is alphabetic :{text3.isalpha()}')   #"Kohli@18" is alphabetic :False

#Numeric String
text4 ="12345"
print(f'"{text4}" is alphabetic :{text4.isalpha()}')    #"12345" is alphabetic :False

# numeric string with space
text5 = "123 45"
print(f'"{text5}" is alphabetic :{text5.isalpha()}')   #"123 45" is alphabetic : False

#Non-alphabetic String
text6 = "python course"
print(f'"{text6}" is alphabetic :{text6.isalpha()}')   #"python course" is alphabetic: False

text7 = "Python"
print(f'"{text7} is alphabetic :{text7.isalpha()}')   #"Python is alphabetic :True