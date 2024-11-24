print("Hello World")


choice = ""

x = 0;

top_ten = []



while choice != "q" and x < 10 :
	choice = input("Enter in a name:")
	
	if(choice == "q"):
	    break
	if(choice == "s"):
	    print(top_ten)
	    
	elif choice.isalpha():
		top_ten.append(choice)
		x += 1
	else:
		print("invalid characters, enter an alphabetical character please")

count = 1;
for name in top_ten:
    print(str(count)+")"+name)
    count += 1

change = input("Would you like to replace a position(type in a number to change:")
if(change == "y"):
    top_ten.remove(int(change))
else:
    print("i just put an else statement here for no reason")

print(top_ten)   
# idea to add: try to replace a position within the list
