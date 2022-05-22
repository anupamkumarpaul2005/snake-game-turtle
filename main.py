from snake import Snake
from turtle import Turtle, Screen
from food import Food
from score import Score

s = Screen()
s.setup(width=600, height=640)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
game = True

score = Score()
snaky = Snake()
fruit = Food()

s.listen()
s.onkey(snaky.turn_up, "Up")
s.onkey(snaky.turn_down, "Down")
s.onkey(snaky.turn_left, "Left")
s.onkey(snaky.turn_right, "Right")
while game:
    s.update()
    snaky.move()
    if snaky.ate_food(fruit.position):
        fruit.get_food()
        score.change_score()
        if score.score > 0:
            snaky.grow()
    if snaky.hit_tail() or snaky.hit_wall():
        fruit.food.hideturtle()
        score.show_result()
        query=s.textinput(title="Want to continue?", prompt="'Play' or 'Quit'")
        if query.lower()=="play":
            score.show_score()
            snaky.reset_game()
            fruit.food.st()
            fruit.get_food()
            s.listen()
        else:
            game=False


