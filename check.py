# This is a check/review to make sure nothing was "lost" over break

# Gabriel Serrata
# Period 1

# Variable declaration and assignment
# Example
myVar = "hello"
# You try, declare two variables 1 string and 1 number, and assign values 
myNum = 2
myVar2 = "Hi"

# While loop
# Example
x = 10
while x > 0:
	print(x)
	x = x - 1

# You try, print your name 100 times
# Dont do this 
# print("Gabriel" * 100)
Gabriel = 100
while Gabriel > 0:
	print("Gabriel")
	Gabriel = Gabriel - 1

# String Concatenation
name = "Gabriel"
print("Hello " + name)
# Make a variable with your favorite movie 
# Print "My favorite movie is" and then the value stored in the variable 
favMovie = "Star Wars"
print("My favorite movie is " + favMovie)

# Input
# Example 
myName = input("What is yout name: ")
print("Your name is: " + myName)
# Prompt for favorite song and print "your favorite song is: "
favSong = input("What is your favorite song: ")
print("Your favorite song is " + favSong)

# Casting: Changing the type of variable
myNumber = 40
print("My number is " + str(myNumber))
num1 = input("Enter a number: ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

# Ask for two numbers, add them and print the answer
Number1 = input("Enter first number: ")
Nubmber2 = input("Enter second number: ")
Number1 = int(Number1) + int(Nubmber2)
print("The two numbers added together equal: " + str(Number1))

# if/else
# example
num3 = int(input("Type a number: "))
if num3 > 100:
	print("Your number is more than 100")
elif num3 == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")
# ask if today is your birthday, if it is print happy birthday 

birthday = int(input("Is today your birthday: "))
if birthday == "yes":
	print("Happy birthday")
elif birthday == "no":
	print("Hope your birthday is close")