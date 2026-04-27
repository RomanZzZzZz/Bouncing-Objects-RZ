from turtle import *
import random


def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    border = Turtle()
    border.hideturtle()
    border.speed(0)
    border.color("teal")
    border.penup()
    border.goto(-240, -240)
    border.pendown()
    for i in range(4):
        border.forward(480)
        border.left(90)


def move_with_heading(t, turtles):
    t.forward(0.5)
    x = t.xcor()
    y = t.ycor()
    hit_wall = False
    if x > 240 or x < -240:
        t.setheading(180 - t.heading())
        hit_wall = True
    if y > 240 or y < -240:
        t.setheading(360 - t.heading())
        hit_wall = True
    if hit_wall:
        tl = Turtle()
        tl.speed(0)
        tl.color(generate_color())
        tl.shape("arrow")
        tl.setheading(random.randint(0, 360))
        turtles.append(tl)
    return turtles


def move_with_deltas(t, deltax, deltay):
    x = t.xcor()
    y = t.ycor()
    new_x = x + deltax
    new_y = y + deltay
    if new_x > 240 or new_x < -240:
        deltax = -deltax
    if new_y > 240 or new_y < -240:
        deltay = -deltay
    t.setx(new_x)
    t.sety(new_y)
    return deltax, deltay


sc = Screen()
sc.bgcolor("black")
sc.setup(520, 520)
sc.tracer(0)


playing_area()


yertle = Turtle()
yertle.speed(0)
yertle.color("white")
yertle.shape("turtle")
yertle.setheading(random.randint(0, 360))


turtles = [yertle]


while True:
    for t in turtles:
        turtles = move_with_heading(t, turtles)
    sc.update()