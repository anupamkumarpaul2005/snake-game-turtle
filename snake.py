from turtle import Turtle
import time

DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            self.add_body(position)

    def add_body(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snake.append(body)

    def move(self):
        time.sleep(0.1)
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())
        self.snake[0].fd(DISTANCE)

    def turn_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].seth(90)

    def turn_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].seth(180)

    def turn_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].seth(0)

    def turn_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].seth(270)

    def ate_food(self, food):
        if self.snake[0].distance(food) < 15:
            return True
        return False

    def grow(self):
        self.add_body(self.snake[-1].pos())

    def hit_wall(self):
        x = self.snake[0].xcor()
        y = self.snake[0].ycor()
        if x >= 290 or x <= -290 or y >= 290 or y <= -290:
            return True
        return False

    def hit_tail(self):
        for body in self.snake[1:]:
            if self.snake[0].distance(body) < 15:
                return True
        return False

    def reset_game(self):
        for body in self.snake:
            body.ht()
        self.snake.clear()
        self.create_snake()
