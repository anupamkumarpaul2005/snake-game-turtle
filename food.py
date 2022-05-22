from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.food = Turtle("circle")
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.penup()
        self.food.color("yellow")
        self.get_food()

    def get_food(self):
        self.position = (randint(-280, 280), randint(-280, 280))
        self.food.goto(self.position)
