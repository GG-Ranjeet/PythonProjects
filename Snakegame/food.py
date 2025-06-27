import random
from turtle import Turtle
POSITION = 280
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.hideturtle()
        self.color("red")
        self.penup()
        self.shapesize(0.8)
        self.refresh()
    def refresh(self):
        x_cor = random.randrange(start=-POSITION,stop= POSITION,step=20)
        y_cor = random.randrange(start=-POSITION,stop= POSITION,step=20)
        self.goto(x_cor, y_cor)