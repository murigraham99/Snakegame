from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.ht()
        self.goto(x=0, y=280)
        self.write(f"Your Score is = {self.score_num} Highscore is: {self.highscore}", False, align="center", font=("Arial", 18, "bold"))

    def resett(self):
        if self.score_num > self.highscore:
            self.highscore = self.score_num
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score_num = 0
        self.update()

    def increase (self):
        self.score_num +=1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Your Score is = {self.score_num} Highscore is: {self.highscore}", False, align="center", font=("Arial", 18, "bold"))

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over!", False, align="center", font=("Arial", 20, "bold"))
