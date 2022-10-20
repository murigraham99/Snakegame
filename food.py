from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("red")
        self.new_food()

    def new_food(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
