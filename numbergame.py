import random

mysteryNum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number 1 and 100: "))
	score = score + 1 

	if guess == mysteryNum:
		print("Good Guess")
		break
	elif guess > mysteryNum:
		print("too high, try again")
	else:
		print("Too low,try again")
print("It took you " + str(score) + "guesses")