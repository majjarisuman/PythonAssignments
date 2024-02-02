#isalnum()

alpha_num = "Rohit45"
print(alpha_num.isalnum())  #True

text = "Python course training duration is 90 days"
print(text.isalnum())  #False

text1 = "Rohit45"
print(f'"{text1}" is alphanumeric: {text1.isalnum()}')   #"Rohit45" is alphanumeric: True

#With space
text2 = "Rohit 45"
print(f'"{text2}" is alphanumeric: {text2.isalnum()}')   #"Rohit 45" is alphanumeric: False

#String with Special Characters
text3 = "Kohli@18"
print(f'"{text3}"" is alphanumeric :{text3.isalnum()}')   #"Kohli@18" is alphanumeric :False

#Numeric String
text4 ="12345"
print(f'"{text4}" is alphanumeric :{text4.isalnum()}')    #"12345" is alphanumeric :True

# numeric string with space
text5 = "123 45"
print(f'"{text5}" is alphanumeric {text5.isalnum()}')   #"123 45" is alphanumeric False

#Non-Alphanumeric String
text6 = "python course"
print(f'"{text6}" is alphanumeric {text6.isalnum()}')   #"python course" is alphanumeric False

