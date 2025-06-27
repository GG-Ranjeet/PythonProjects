from re import M
from turtle import Screen, Turtle, xcor
import time
starting_pos = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def move_snake(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_coor = self.segments[seg-1].xcor()
            y_coor = self.segments[seg-1].ycor()
            self.segments[seg].goto(x_coor,y_coor)
        self.segments[0].fd(MOVING_DISTANCE)

    def create_snake(self):

        for i in starting_pos:
            self.new_part(i)

    def reset(self):
        for seg in self.segments:
            seg.clear()  # Clear drawing from the screen (optional if penup)
            seg.goto(1000, 1000)  # Move off-screen to avoid clutter during frame
            seg.hideturtle()  # Hide (just to avoid flicker during GC)
            del seg  # Remove reference

        self.segments = []  # Reassign to a new empty list (safe & clean)
        self.create_snake()


    def up(self):
        if self.segments[0].heading() !=270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() !=90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() !=0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() !=180:
            self.segments[0].setheading(0)
    
    def new_part(self,i):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.new_part(self.segments[-1].position())