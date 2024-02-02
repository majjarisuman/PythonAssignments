#isdigit()

Digit = "Rohit45"
print(Digit.isdigit())  #False

text = "Python course training duration is 90 days"
print(text.isdigit())  #False

text1 = "Rohit45"
print(f'"{text1}" is Digit: {text1.isdigit()}')   #"Rohit45" is Digit: False

#With space
text2 = "Rohit 45"
print(f'"{text2}" is Digit: {text2.isdigit()}')   #"Rohit 45" is Digit: False

#String with Special Characters
text3 = "Kohli@18"
print(f'"{text3}"" is Digit :{text3.isdigit()}')   #"Kohli@18" is Digit :False

#Numeric String
text4 ="12345"
print(f'"{text4}" is Digit :{text4.isdigit()}')    #"12345" is Digit :True

# numeric string with space
text5 = "123 45"
print(f'"{text5}" is Digit :{text5.isdigit()}')   #"123 45" is Digit : False

#Non-Digit String
text6 = "python course"
print(f'"{text6}" is Digit :{text6.isdigit()}')   #"python course" is Digit: False

text7 = "Python"
print(f'"{text7} is Digit :{text7.isdigit()}')   #"Python is Digit :False