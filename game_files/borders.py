from turtle import Turtle


class Borders(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest") 
        
        self.draw_grid(width, height)
        
        self.color("cyan")  
        self.pensize(4)     
        self.draw_borders(width, height)

    def draw_grid(self, width, height):

        self.color("#1a1a1a")  
        self.pensize(1)
        
        half_w = int((width / 2) - 10)
        half_h = int((height / 2) - 10)
        grid_size = 10  

        for x in range(-half_w, half_w + 1, grid_size):
            self.penup()
            self.goto(x, half_h)
            self.pendown()
            self.goto(x, -half_h)

        for y in range(-half_h, half_h + 1, grid_size):
            self.penup()
            self.goto(-half_w, y)
            self.pendown()
            self.goto(half_w, y)

    def draw_borders(self, width, height):
        half_w = (width / 2) - 10
        half_h = (height / 2) - 10

        self.penup()
        self.goto(-half_w, half_h)
        self.pendown()
        for _ in range(2):
            self.forward(half_w * 2)
            self.right(90)
            self.forward(half_h * 2)
            self.right(90)