from turtle import *

myTurtle = Turtle()
screen = myTurtle.getscreen()
myTurtle.forward(200)

def printName():
	name = screen.textinput("name", "what is yout name?")
	myTurtle.write(name, move=True, align="left", font=("Arial", 40, "normal"))
	screen.listen()
def goForward():
	myTurtle.forward(10)
def goBackward():
	myTurtle.backward(10)
def goRight():
	myTurtle.right(10)

screen.onkey(printName, "p")
screen.onkey(goForward, "Up")
screen.onkey(goBackward, "Down")
screen.onkey(goRight, "Right")


screen.listen()
screen.mainloop()


