from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score = self.load()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def load(self):
        try:
            with open("save_file.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def saving(self):
        with open("save_file.txt", "w") as file:
            file.write(str(self.highest_score))
    
    def update_scoreboard(self):
        self.clear()
        if self.pos() != (0, 250):
             self.goto(0, 250)
        if self.highest_score != 0:
             
            self.write(f"Score: {self.score}    Highest Score: {self.highest_score}", align="center", font=("arial", 24, "normal"))
        else:
            self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))

    def increase_score(self, value):
        self.score += value
        self.update_scoreboard()

    def decrease_score(self, value):
        self.score -= value
        self.update_scoreboard()
        print("decreased score by", value)

    def reset_score(self):
         self.score = 0
         self.update_scoreboard()

    def game_over(self):

        self.goto(0, 80)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        
        is_new_record = False
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.saving()
            is_new_record = True

        self.goto(0, 10)
        self.color("white")
        self.write(f"Final Score: {self.score}", align="center", font=("Courier", 20, "bold"))

        self.goto(0, -30)
        if is_new_record:
            self.color("gold") 
            self.write(f"★ NEW HIGH SCORE: {self.highest_score} ★", align="center", font=("Courier", 16, "bold"))
        else:
            self.color("lightgray")
            self.write(f"Highest Score: {self.highest_score}", align="center", font=("Courier", 16, "normal"))

        self.goto(0, -90)
        self.color("gray")
        self.write("Press 'Space' to Restart", align="center", font=("Courier", 13, "italic"))
        self.goto(0,-120)
        self.write(" 'Escape' to exit", align="center", font=("Courier", 13, "italic"))
