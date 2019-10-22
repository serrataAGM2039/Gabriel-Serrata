print("Welcome to To Do List")
# Make a variable to hold your list 
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Choose: ")

	if choice == "q":
		break 
	elif choice == "a":
		# add an item to the list 
		toList = input("Enter what you want to add to the list: ")
		todoList.append(toList)
		
		
	elif choice == "r":
		#remove item from list
		dolist = input("What would you like to remove from the list: ")
		todoList.remove(dolist) 
		 
	elif choice == "p":
		print(todoList)
	else:
		print("You chose something not on the list")
