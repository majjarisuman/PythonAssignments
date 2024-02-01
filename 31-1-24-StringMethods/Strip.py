#Strip
text = "  Hello,Good Morning"
text_strip = text.strip()

print(text)   #  Hello,Good Morning(with space will print op)
print(text_strip)   #Hello,Good Morning(without space will print op)

#removing specific char by use Strip()
text2 = "----Hello Dude----"
text_strip2 = text2.strip('-')

print(text2)        #----Hello Dude----
print(text_strip2)  #Hello Dude

#\t tab , \n newline removing by use of strip
text3 = "\t hello world \n"
text_strip3 = text3.strip()

print(text3)
#output
#  hello world      # tab space op
                    #newline op
print(text_strip3)    #hello world   #op-removed tab space and newline

#removing special char in string @
text4 = "@@@@ Rohit_45"
text_strip4 = text4.strip()
text_strip5 = text4.strip('@')
text_strip6 = text4.strip(' ')

print(text4)         #@@@@ Rohit_45
print(text_strip4)   #@@@@ Rohit_45
print(text_strip5)   # Rohit_45
print(text_strip6)   #@@@@ Rohit_45

#if-else
List = ['kf','boom','corona']
beer = input("Enter Beer Name :- ")

if beer.strip() in List:
    print(beer,'is avalable') 
else:
    print(beer,'is not available')
    
#for
original_list = ["   Apple  ", "Banana   ", "  Orange  "]
stripped_list = [fruit.strip() for fruit in original_list]

print("Original List:", original_list)
print("Stripped List:", stripped_list)




