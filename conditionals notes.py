#conditionals- if / else

age = input("What is your age? ") #prompt for age

#check if the age is more than 17, so the person 
#can see R rated parents
age = int(age)
if age > 17: #everything in the if statement only runs if the condition is true
	print("You can see an R rated movie")

else:
	print("you can not see an R rated movie, too bad so sad")

print("Have a nice day!")
#you can check all these conditions
# >, <, >-, <-, == (==means equal too)

birthday = input("Is today your brithday (yes or no)")
if birthday == "yes":
	print("Happy Birthday")
print("have a nice day!")

myNum = 7
guess = input("guess a number between 1 and 10? ")
guess = int(guess)
if guess == myNum:
	print("you guessed correctly")
elif guess > myNum:
	print("Too High")
else:
	print("Too Low")
print("Thanks for playing")
