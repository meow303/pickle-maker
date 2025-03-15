#imports
import turtle
import time

#initialize
t = 259200

screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.bgpic('pickleJar.gif')
screen.register_shape('pickle.gif')

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.pencolor("green")
text.setposition(-150, 20)

pickle = turtle.Turtle()
pickle.penup()
pickle.setposition(-140, -50)
pickle.shape('pickle.gif')

#functions
def timer():
  global t
  while t > 0:
    time.sleep(1)
    t -= 1
    text.clear()
    tt = str(t) + " seconds until pickle is ready!"
    text.write(tt, font=("Arial", 12, "normal"))
    
    if t == 0:
      text.clear()
      text.write("Pickle is ready!", font=("Arial", 12, "normal"))


def up():
  pickle.setheading(90)
  pickle.forward(10)
  check_jar_position()
  
def down():
  pickle.setheading(270)
  pickle.forward(10)
  check_jar_position()
  
def left():
  pickle.setheading(180)
  pickle.forward(10)
  check_jar_position()

def right():
  pickle.setheading(0)
  pickle.forward(10)
  check_jar_position()
  
def check_jar_position():
  # Check if pickle is at the target position (the jar location)
  if pickle.xcor() <= 20 and pickle.xcor() >= -20 and pickle.ycor() <= 20 and pickle.ycor() >= -20: 
    pickle.goto(0,0)  
    screen.ontimer(timer, t=1000)

#call functions
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
check_jar_position()

#timer()

#text.getscreen().ontimer(timer, t=1000)

screen.mainloop()
