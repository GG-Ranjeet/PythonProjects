from turtle import Screen, Turtle
import time


from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("seagreen1")
screen.title("Snake game")
screen.tracer(0)

dann = Turtle()
# dan = Turtle()
dann.penup()
dann.goto(300,300)
dann.color("white")
dann.pendown()

dann.goto(300,-300)
dann.goto(-300,-300)
dann.goto(-300,300)
dann.goto(300,300)
dann.penup()
dann.hideturtle()

food = Food()
snake = Snake()
score = Score()

screen.listen()
screen.onkeypress(fun = snake.up, key = "w")
screen.onkeypress(fun = snake.down, key = "s")
screen.onkeypress(fun = snake.left, key = "a")
screen.onkeypress(fun = snake.right, key = "d")

game_is_on = True
game_on = True
while game_is_on:

    time.sleep(0.1)
    snake.move_snake()
    head = snake.segments[0]
    
    #Food, new part and score
    if head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Collision with border
    if head.xcor() >= 300 or head.xcor() <= -300 or head.ycor() >= 300 or head.ycor() <= -300:
        game_on = False

        # score.game_over()

    #collition with tail
    #trigger game over
    for seg in snake.segments[2:]:
        if head.distance(seg)<10:
            score.game_over()
            game_on = False
    if not game_on:
        snake.reset()
        game_on = True
        score.game_over()

        # for i in range(1, 4):
        #     self.write(f"Continuing in {i} seconds...", align="center", font=FONT)
        #     time.sleep(1)


    screen.update()

screen.mainloop()