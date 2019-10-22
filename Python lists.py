favFoods = ["Pizza", "Ice Cream", "Tacos"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# Adds to the end of the list 
favFoods.append("Chicken")
print(favFoods)
print(favFoods[3])
print("My fourth favorite food is " + favFoods[3])
#adds to an indec in a list 
favFoods.insert(1, "Pasta")
print(favFoods)
# Remove an item frim the list 
favFoods.remove("Pasta")
print(favFoods)
# Remove by index\
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "Pizza")
for food in favFoods:
	print(food)

numList = [1, 6, 9, 22, 67, 64, 23, 12]

# Lopp through the list and add all the numbers together then print the sum

sum = 0 
for num in numList:
	sum = sum + num
print(sum)
# function to get the length of a list 
print(len(favFoods))
print(len(numList))

# make a list of our favorite movies 
# prompt for a favorite movie 

myFood = input("What is your favorite food? ")
favFoods.append(myFood)
print(favFoods)

favMovie = ["Avengers End Game", "Star Wars the Empire Strikes Back", "Dead Pool", "Iron Man", "John Wick Chapter 3"]
myMovie = input("What is your favorite movie? ")
favMovie.append(myMovie)
print(favMovie)

# List methods and Functions 
# append - adds an item to the end of a list 
# Insert - adds an item to a specified idex
# Remove- removes a specified item from a list
# pop - removes an item from a specified index
# len - returns the length of a list \
print(favFoods[len(favFoods)-1])
