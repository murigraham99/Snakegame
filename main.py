from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

game_on = True
segments = []

# Screen setup:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
##################

food = Food()
score = Score()

# main game loop:

while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # detect collision using distance method()

    if snake.head.distance(food) < 15:
        food.new_food()
        score.increase()
        snake.extra_segment()

    # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.resett()
        snake.reset()


    # detect collision with itself

    for element in snake.segments[1:]:

        if snake.head.distance(element) < 5:

            score.resett()

screen.exitonclick()
##################
