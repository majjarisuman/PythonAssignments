text = "Hello, world! Hello, Python!"
substring = "Hello"

# print(f'Index of Right side Hello :{text.rindex(substring)}')  #Index of Right side Hello :14
# print(f"Index of Right side Hello :{text.rfind(substring)}")  #Index of Right side Hello :14

# negative values
substring = "Rohit45"
# print(f'Index of Right side Hello :{text.rindex(substring)}')  #ValueError: substring not found
print(f'Index of Right side Hello :{text.rfind(substring)}')  #Index of Right side Hello :-1


