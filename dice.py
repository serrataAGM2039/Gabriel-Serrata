# Name: Gabriel Serrata
# Period 1
# Dice Rolling Simulator
import random 
print("welcome to the Dice Rolling Simulator")
numRolls = int(input("How many rolls?"))
x = 1
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
while x<= numRolls:
	randomNum = random.randint(1 , 6)
	x += 1
	if randomNum == 1:
		one += 1
	elif randomNum == 2:
		two += 1
	elif randomNum == 3:
		three += 1
	elif randomNum == 4:
		four += 1
	elif randomNum == 5:
		five += 1
	elif randomNum == 6:
		six += 1
	print("Percentage:")
	print("1s - " + str(one/(numRolls)*100)+ "%")
	print("2s - " + str(two/(numRolls)*100)+ "%")
	print("3s - " + str(three/(numRolls)*100)+ "%")
	print("4s - " + str(four/(numRolls)*100)+ "%")
	print("5s - " + str(five/(numRolls)*100)+ "%")
	print("6s - " + str(six/(numRolls)*100)+ "%")
	print ("Roll number " + str(randomNum) + "\n" + "Dice rolled: " + str(x))
	print ("1s = " + str(one))
  	print ("2s = " + str(two))
 	print ("3s = " + str(three))
  	print ("4s = " + str(four)
) 	print ("5s = " + str(five))
 	print ("6s = " + str(six))
