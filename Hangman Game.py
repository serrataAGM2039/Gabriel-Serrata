import random
myWords = ["hangman", "computer", "school", "math", "english"]
mysteryWord = random.choice(myWords)


#choice = input(" Type a word: ")

#if choice == myWords:
	#print("Its a match")
#else:
	#print("Not a match")

# How to check if a letter is in a word 

#letter = input("Enter a letter: ")

#if letter in myWord:
	#print("Letter is in the word")
#else:
	#print("Letter is not in the word")
	
#count = 0
#myList = list(myWord)
#for letter2 in myList:
	#if letter2 == letter:
		#print(count)
	#count += 1
	

# How to change a string into a list
mystring = "Arizona"
mysteryWord2 = list(mystring)
print(mysteryWord2)
guessList = []
# How to make a list with _ for characters 
for letter in mysteryWord2:
	guessList.append("_")

# How to replace a specific index in a list 
guessList[3] = "z"

print(guessList)












frameList = ['''
  +---+
      |
      |
      |
 	 ===
 ''']
