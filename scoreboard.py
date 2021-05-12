from turtle import Turtle

ALIGNMENT = "center"
FONT1 = ("Courier", 50, "normal")
FONT2 = ("Arial", 48, "bold") 
VICTORY_CONDITIONS = {'total_score':11, 'margin':2}

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreboard()
        self.game_is_on = True
        self.winner = None

    def updateScoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT1)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT1)
    
    def addPoint(self, left_player=True, points=1):
        if left_player:
            self.l_score += points
        else:
            self.r_score += points
        self.clear()
        self.updateScoreboard()
        self.checkScore()

    def checkScore(self):
        VICTORY_CONDITIONS
        if (max(self.l_score, self.r_score) >= VICTORY_CONDITIONS['total_score']) and \
           (abs(self.l_score-self.r_score) >= VICTORY_CONDITIONS['margin']):
           self.game_is_on = False
           self.declareWinner()
    
    def declareWinner(self):
        if self.l_score >= self.r_score:
            self.winner = 'Player 1'
        else:
            self.winner = 'Player 2'
        
        self.goto((0,0))
        self.write("{} wins!".format(self.winner), align=ALIGNMENT, font=FONT1)



        