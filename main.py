from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
switch = True
while switch:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.outside():
        scores.reset()
        switch = False
        scores.over()
    elif snake.outside_y():
        scores.reset()
        switch = False
        scores.over()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.increase()
    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            switch = False
            scores.over()

screen.exitonclick()
