sentence = "Hello, World! Welcome to Python."
# print(f'Index of World :{sentence.find('World')}')    #Index of World :7

# #Specifying Start and End Indices
print(f'start and end indices :{sentence.index('l',1,15)}')   #start and end indices :2

#Using Index with Negative Values
print(f'Negative Values :{sentence.index('o',-20,-1)}')   #Negative Values :18

words = "Python course"
# print("Not found :",words.index('rohit45'))   #ValueError: substring not found
print(f"Index of course :{words.index('course')}")    #Index of course :7

# #Finding Multiple Occurrences
word = "Hello, World! Hello, Python! Hello, Universe!"
index = word.index("Hello")
print(f"First occurrence of 'Hello': {index}")   #First occurrence of 'Hello': 0
print(f"Next occurrence of 'Hello': {word.index("Hello",index+1)}")  #Next occurrence of 'Hello': 14


