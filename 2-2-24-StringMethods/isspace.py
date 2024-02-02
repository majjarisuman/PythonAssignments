# isspace()


text1 = " "
print(f'"{text1}" is isspace: {text1.isspace()}')   #"Rohit45" is isspace: True

#With space
text2 = "rohit    Kohli"
print(f'"{text2}" is isspace: {text2.isspace()}')   #"Rohit 45" is isspace: False

#String with Special Characters
text3 = ""
print(f'"{text3}"" is isspace :{text3.isspace()}')   #"Kohli@18" is isspace :False

#Numeric String
text4 ="\t"
print(f'"{text4}" is isspace :{text4.isspace()}')    #"12345" is isspace :True

# numeric string with space
text5 = "    45"
print(f'"{text5}" is isspace :{text5.isspace()}')   #"123 45" is isspace : False

#Non-isspace String
text6 = "Python Course"
print(f'"{text6}" is isspace :{text6.isspace()}')   #"python course" is isspace: :False

text7 = "\n \n"
print(f'"{text7} is isspace :{text7.isspace()}')   #"Python is isspace :True