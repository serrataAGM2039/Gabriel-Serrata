# Calculations, Printing, Variables 

#printing to the screen
# The built in function print(), prints to the screen
# it will print both strings and numbers 
print("printing to the screen...")
print("hello")# a string
print('hello again')
print(6) # a number 
print("6")# a string again
print(6 + 6) # 12 
print("6" + "6") # String concatenation

#print("6" + 6) #what will this be? -> error

#performing calculations
#addition +
#subtraction -
#multiplacation * 
#division /
#exponets **
#modulo %

print(4-2) #subtraction -> 2
print(4*2) #multiplacation ->8
print(4/2) #division ->1.33...
print(4 ** 3) #exponets -> 64
print("modulo operator test...")
print(5 % 3)
print(10 % 2)
print(16 % 3)
#modulo gives remainders 
# oythin operators follow the same order of operations as math 
print(4-2 * 2) #should be zero
print((4-2) * 2) #should give 4

#variables 
#variales are used to hold data
#variables are declared and set a value (initializing)
badLuck = 13 #declared a variable called badluck and initialized it to 13 
#1 can print the variable using its name 
print("badLuck =" + str (badLuck)) #cast it to a string
#lets do another one 
goodLuck = "4" #string variable
print("goodLuck = " + goodLuck) #dont havve to cast
badLuck + 5 #this is pointless
print(badLuck)
badLuck = badLuck + 5 # no0w badLuck is 18
print(badLuck)

#you can also save input into variables 
#using input() .. A prompt goes inside the ()
name = input("What is your name?")
print("Hello" + name)
print(name * 10)
name = name + "\n" #escape character (newline)
#lets try some amth
base = input("Enter the base number: ")
exp = input("Enter the exponets: ")
print(int (base) ** int (exp))