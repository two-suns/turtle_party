import turtle

# Set turtle color
turtle.color("red")

# Move the turtle backwards
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

# Triangle function
def triangle(size):
  for side in range(3):
    turtle.forward(size)
    turtle.left(120)

# Square function
def square(size):
  for side in range(4):
    turtle.forward(size)
    turtle.left(90)

# Polygon function with error test    
def polygon(sides, length):
  angle = 360 / sides
  if sides < 3:
      turtle.hideturtle()
      print("Enter number of sides greater than 3.")
  else:
    for side in range(sides):
      turtle.forward(length)
      turtle.right(angle)

# Spiral function    
def spiral(side, angle):
  for sides in range(side, 5, -5):
    turtle.forward(sides)
    turtle.right(angle)

# Draw shapes in a clock pattern
# Set number of "dashes"
num_shapes = 12

# Draw shapes in a circle loop
for i in range(num_shapes):
  turtle.penup()
  turtle.goto(0, 0)
  turtle.setheading(360 / num_shapes * i)
  turtle.forward(100)
  turtle.pendown()
  polygon(6, 20)
  turtle.penup()

# spiral(100, 90)
