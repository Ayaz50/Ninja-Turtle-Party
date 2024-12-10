# Ninja Turtle Party Project
# by: Ayaz Sadiq
12/09/24

import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

# forward helper function
#def move (len):
  #back(-1 * len)

def polygon (num, size):
  for i in range (num):
    turtle.forward(size)
    turtle.left(360 / num)

polygon(4, 100)
back(125)
polygon(3,50)
#def spiral (len, angle):
  #for i in range(len, 5, -5):
    #turtle.forward(i)
    #turtle.right(angle)
    


#spiral(75, 45)
#move(150)
#turtle.color("blue")
#spiral(100, 90)

# for n in range (3, 10):
#  move(50) # forward
#  polygon(n, 100 / n)
#  back(50)
#  turtle.right(360 / 7)
  
