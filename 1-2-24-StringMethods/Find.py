#syntax :-  str.find(substring, start, end)

sentence = "This is a simple example."
print('Index of Simple :-',sentence.find('simple'))    #OP: Index of Simple :- 10

print('Substring Not Found :',sentence.find('Rohit45'))  #OP:Substring Not Found : -1 

#Search within a Range
print('Search within a Range:',sentence.find('i',3,10))   #OP: Search within a Range: 5

#Case-sensitive Search
print("Case-sensitive :",sentence.find('this'))    #OP : Case-sensitive : -1

#Substring at the Beginning
print('Substring at the Beginning :',sentence.find('This'))  #OP : Substring at the Beginning : 0

#Substring at the End
print(f'Substring at the End:{sentence.find('example')}')    #OP: Substring at the End:17


sentence = "multiple occurrences example with multiple multiple words."
index = sentence.find("multiple")
while index != -1:
    print("Found 'multiple' at index:", index)
    index = sentence.find("multiple", index + 1)


word = "Hello, how are you doing today?"
index = word.find("how")
print("Index of 'how':", index)   # Op: 7
index_not_found = word.find("not found")
print("Index of 'not found':", index_not_found)  # Op: -1

