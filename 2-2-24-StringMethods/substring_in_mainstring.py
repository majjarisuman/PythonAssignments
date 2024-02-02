Main_string = input("Enter a sentence : ")
Substring = input("Enter a substring : ")

index = Main_string.find(Substring)
if index != -1:
    print(f"substring {Substring} is present in the Mainstring at index {index}")
else:
    print(f"Substring {Substring} not found in the Mainstring")

