from turtle import *
from datetime import datetime
from PIL import Image

def to_degree(value, max_value):
    return (value / max_value) * 360

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Analog Clock")
screen.tracer(0)

img = Image.open("clock.jpeg")
img = img.resize((480, 480))  
img.save("scaled_image.png")
try:
    screen.bgpic("scaled_image.png")
except:
    screen.bgpic("images.png")


hr_hand = Turtle()
min_hand = Turtle()
sec_hand = Turtle()
sec_hand.color('red')

for hand in (hr_hand, min_hand, sec_hand):
    hand.hideturtle()
    hand.speed(0)
    hand.pensize(3)

dot = Turtle()
dot.shape("circle")
dot.shapesize(0.5, 0.5)
dot.penup()

def update_clock():
    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    hr_angle = to_degree(hours, 12) + to_degree(minutes, 60)/12
    min_angle = to_degree(minutes, 60)
    sec_angle = to_degree(seconds, 60)

    for hand in (hr_hand, min_hand, sec_hand):
        hand.clear()
        hand.penup()
        hand.goto(0, 0)
        hand.pendown()

    hr_hand.setheading(90 - hr_angle)
    hr_hand.forward(60)

    min_hand.setheading(90 - min_angle)
    min_hand.forward(100)

    sec_hand.setheading(90 - sec_angle)
    sec_hand.forward(110)

    screen.update()
    screen.ontimer(update_clock, 1000)

update_clock()
screen.mainloop()



