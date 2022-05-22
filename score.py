from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        with open("highest_score.txt") as file:
            self.highest_score=int(file.read())
        self.scorecard = Turtle()
        self.scorecard.penup()
        self.scorecard.hideturtle()
        self.scorecard.color("white")
        self.show_score()

    def show_score(self):
        self.scorecard.goto(0, 300)
        self.scorecard.clear()
        self.scorecard.write(f"SCORE:\t{self.score}\tHIGHEST SCORE:\t{self.highest_score}", align="center")

    def change_score(self):
        self.score += 1
        self.show_score()

    def show_result(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.score=0
        self.scorecard.home()
        self.scorecard.write("Game Over!", align="center", font=("Courier", 60, "normal"))