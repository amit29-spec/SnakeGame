from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(f"SCORE = {self.score} HIGHSCORE = {self.highest}", False, align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highest:
            self.highest = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest}")
        self.clear()
        self.write(f"SCORE = {self.score} HIGHSCORE = {self.highest}", False, align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score} HIGHSCORE = {self.highest}", False, align="center", font=("Arial", 24, "normal"))

    def over(self):
        self.color("red")
        self.penup()
        self.goto(x=0, y=0)
        self.hideturtle()
        self.write("GAME OVER!", False, align="center", font=("Arial", 24, "normal"))
