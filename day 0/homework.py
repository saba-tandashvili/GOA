from turtle import *

# starting
speed(5)
width(7)
penup()

# drawing the house

left(180)
forward(150)
left(90)
forward(50)
right(90)
left(180)
pendown()
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)

# drawing the roof
color("red")

penup()
left(90)
forward(300)
left(90)
forward(200)
left(180)
left(135)
pendown()
begin_fill()
left(90)
forward(212)
left(90)
forward(210)
left(135)
forward(300)
end_fill()

penup()
goto(-120, -50)
color("yellow")
forward(100)
pendown()
begin_fill()
left(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

# windows

penup()
left(90)
forward(30)
left(90)
forward(100)
color("aqua")
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
forward(150)
right(90)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()