from turtle import Turtle
import time

FONT = ('Arial', 15, 'normal')



class Score(Turtle):
        def __init__(self):
                super().__init__()
                self.clear()
                self.hideturtle()
                self.score = 0
                with open("data.txt", "r") as file:
                        data = file.read()
                        self.highscore = int(data)
                self.penup()
                self.color("white")
                self.goto(0,300)
                self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

        def update(self):
                self.goto(0,300)
                self.score += 1
                self.high_score()
                self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

        def increase_score(self):
                self.clear()
                self.update()
                # self.goto(-10,300)

        def game_over(self):
                self.home()
                self.write("GAME OVER!", align="center", font=FONT)
                self.goto(0,40)
                self.write(f"You scored: {self.score}", align="center", font=FONT)
                self.high_score()
                self.score = 0
                self.clear()
                self.update()

        def high_score(self):
                if self.score > self.highscore:
                        self.highscore = self.score
                with open("data.txt", "w") as file:
                        file.write(str(self.highscore))
