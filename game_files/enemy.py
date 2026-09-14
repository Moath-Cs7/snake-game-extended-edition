import random
from turtle import Turtle

MOVE_DISTANCE = 10

class Enemy:
    def __init__(self):
        self.body = []
        self.is_active = False
        self.direction = "right"

    def spawn(self, player_snake):
        self.clear_enemy()
        
        while True:
            x_random = random.randint(-12, 12) * MOVE_DISTANCE
            y_random = random.randint(-12, 12) * MOVE_DISTANCE
            
            if player_snake.head.distance(x_random, y_random) > 100:
                break

        length = random.randint(5, 10)
        for i in range(length):
            part = Turtle("square" if i > 0 else "triangle")
            part.shapesize(0.5 if  i > 0 else 1)
            part.color("crimson" if i > 0 else "dark red")
            part.penup()
            part.goto(x_random - (i * MOVE_DISTANCE), y_random)
            self.body.append(part)

        self.head = self.body[0]
        self.direction = "right"
        self.is_active = True

    def _set_direction(self, new_dir):
        opposite = {"right": "left", "left": "right", "up": "down", "down": "up"}
        if self.direction != opposite.get(new_dir):
            self.direction = new_dir
            return True
        return False

    def move_towards(self, target_pos):
        if not self.is_active or not self.body:
            return

        ex, ey = self.head.xcor(), self.head.ycor()
        tx, ty = target_pos[0], target_pos[1]

        primary_dir = "right" if tx > ex else "left"
        secondary_dir = "up" if ty > ey else "down"

        if abs(ty - ey) > abs(tx - ex):
            primary_dir, secondary_dir = secondary_dir, primary_dir

        if not self._set_direction(primary_dir):
            self._set_direction(secondary_dir)

        headings = {"right": 0, "up": 90, "left": 180, "down": 270}
        self.head.setheading(headings[self.direction])

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def clear_enemy(self):
        for part in self.body:
            part.hideturtle()
        self.body.clear()
        self.is_active = False
