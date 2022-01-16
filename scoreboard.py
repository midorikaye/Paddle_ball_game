from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 260)
        self.write(f"{self.l_score} vs {self.r_score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.boardupdate()

    def boardupdate(self):
        self.clear()
        self.write(f"{self.l_score} vs {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def addscore(self,player):
        if player == 1:
            self.l_score += 1
            self.boardupdate()
        if player == 2:
            self.r_score += 1
            self.boardupdate()

    def game_over(self,player):
        self.clear()
        self.write(f"{self.l_score} vs {self.r_score}.Player {player} won!", False, align=ALIGNMENT, font=FONT)
