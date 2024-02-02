# istitle()


text1 = "Rohit45 Rohit45"
print(f'"{text1}" is istitle: {text1.istitle()}')   #"Rohit45" is istitle: True

#With space
text2 = "rohit 45 Kohli"
print(f'"{text2}" is istitle: {text2.istitle()}')   #"Rohit 45" is istitle: False

#String with Special Characters
text3 = "Kohli@18 kohli"
print(f'"{text3}"" is istitle :{text3.istitle()}')   #"Kohli@18" is istitle :False

#Numeric String
text4 ="12345"
print(f'"{text4}" is istitle :{text4.istitle()}')    #"12345" is istitle :False

# numeric string with space
text5 = "123 45"
print(f'"{text5}" is istitle :{text5.istitle()}')   #"123 45" is istitle : False

#Non-istitle String
text6 = "Python Course"
print(f'"{text6}" is istitle :{text6.istitle()}')   #"python course" is istitle: :True

text7 = "Python"
print(f'"{text7} is istitle :{text7.istitle()}')   #"Python is istitle :True