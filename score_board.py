from turtle import Turtle

class Score_board(Turtle):


    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100,y=200)
        self.write(self.lscore,align="center",font=("Courier",80,"normal"))
        self.goto(x=100,y=200)
        self.write(self.rscore,align="center",font=("Courier",80,"normal"))

    def l_point(self):
        self.lscore+=1
        self.update_scoreboard()
    
    def r_point(self):
        self.rscore+=1
        self.update_scoreboard()
    