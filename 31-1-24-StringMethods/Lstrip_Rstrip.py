#Lstrip-Rstrip
text = " Python course "
lstrip1 = text.lstrip()
rstrip1 = text.rstrip()
print(repr(lstrip1))   #'Python course '
print(repr(rstrip1))   # ' Python course'

#removing '@'
text1= "@@ python course @@"
lstrip2 = text1.lstrip('@')
rstrip2 = text1.rstrip('@')

print(repr(lstrip2)) #' python course @@'
print(repr(rstrip2)) #'@@ python course '

#removing '#'

text3 = "###Python###"
left_stripped_text = text3.lstrip('#')
right_stripped_text = text3.rstrip('#')


print("Original Text:", repr(text3))             #'###Python###'
print("Left Stripped Text:", repr(left_stripped_text))    #'Python###'
print("Right Stripped Text:", repr(right_stripped_text))  #'###Python'

#removing space and special char '!'
text4 = "   Mixed Strips!!!   "
mixed_strips_text = text4.lstrip().rstrip('!')
mixed_strips_text1 = text4.lstrip().rstrip('!').rstrip()

print("Original Text:", repr(text4))     # '   Mixed Strips!!!   '
print("Mixed Strips Text:", repr(mixed_strips_text))   #'Mixed Strips!!!   '
print("Mixed Strips Text:", repr(mixed_strips_text1))   #'Mixed Strips!!!'

text5 = "  @@python course##  "
strip = text5.rstrip()
strip1 = text5.lstrip()
strip2 = text5.rstrip().lstrip().lstrip('@@').rstrip('##')

print(repr(strip))   #'  @@python course##'
print(repr(strip1))     #'@@python course##  '
print(repr(strip2))    #'python course'
