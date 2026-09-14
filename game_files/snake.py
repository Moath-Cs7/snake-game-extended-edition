from turtle import Turtle

HEAD_COLOR = "#FFD43B"
BODY_COLOR = "#306998"
MOVEMENT_DISTANCE = 20

class Snake:
    def __init__(self):
        self.body = []
        self.positions = [(0,0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.body[0]
        self.direction = ""
        self.next_direction = "right"
        self.invincibility = False
        self.losed_parts = 0
        self.losed_parts_total = 0

    def create_snake(self):
        for i in range(len(self.positions)):

            new_part = Turtle("circle")

            if i == 0:
                new_part.color(HEAD_COLOR)
            else:
                new_part.color(BODY_COLOR)

            new_part.penup()
            new_part.goto(self.positions[i])
            self.body.append(new_part)

    def move(self):

        self.direction = self.next_direction
        self.head.setheading({"right": 0, "up": 90, "left": 180, "down": 270}[self.direction])
        for i in range(len(self.body) -1, 0, -1):
            self.body[i].goto(self.body[i -1].pos())
        self.head.forward(MOVEMENT_DISTANCE)

    def extend(self, value):
        for _ in range(value):
            new_part = Turtle("circle")
            new_part.color(BODY_COLOR)
            new_part.penup()
            new_part.goto(self.body[-1].pos())
            self.body.append(new_part)

    def cutting_parts(self, cutting_point):
        for i in self.body[cutting_point:]:
            i.hideturtle()
            self.losed_parts += 1

        self.losed_parts_total += self.losed_parts
        self.body = self.body[:cutting_point]
        self.recolor()

    def recolor(self):
        for idnex, part in enumerate(self.body[1::]):
            if idnex < (len(self.body) -1) // 3:
                part.color(HEAD_COLOR)
            else:
                part.color(BODY_COLOR)


    def reset(self):
        for part in self.body:
            part.hideturtle()
        
        self.body.clear()

        self.create_snake()
        self.head = self.body[0]
        self.next_direction = "right"
        self.invincibility = False
        self.losed_parts = 0
        self.losed_parts_total = 0
        
    def up(self):
        if self.direction != "down":
            self.next_direction = "up"
    def down(self):
        if self.direction != "up":    
            self.next_direction = "down"
    def right(self):
        if self.direction != "left":
            self.next_direction = "right"
    def left(self):
        if self.direction != "right":
            self.next_direction = "left"