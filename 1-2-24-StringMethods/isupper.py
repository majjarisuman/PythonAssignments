#isupper()

text1 = "ROHIT45"
print(f'"{text1}" is isupper: {text1.isupper()}')   #"Rohit45" is isupper: True

#With space
text2 = "ROHIT 45"
print(f'"{text2}" is isupper: {text2.isupper()}')   #"Rohit 45" is isupper: True

#String with Special Characters
text3 = "KOHLI@18"
print(f'"{text3}"" is isupper :{text3.isupper()}')   #"Kohli@18" is isupper ::True

#Numeric String
text4 ="12345"
print(f'"{text4}" is isupper :{text4.isupper()}')    #"12345" is isupper :False

# numeric string with space
text5 = "123 45"
print(f'"{text5}" is isupper :{text5.isupper()}')   #"123 45" is isupper : False

#Non-isupper String
text6 = "PYTHON course"
print(f'"{text6}" is isupper :{text6.isupper()}')   #"python course" is isupper: :False

text7 = "PYTHON"
print(f'"{text7} is isupper :{text7.isupper()}')   #"Python is isupper :True