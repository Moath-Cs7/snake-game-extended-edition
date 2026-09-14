import random
from turtle import Turtle

FOOD = {'red': {"value": 3, "ability": False, "chance": 75}, "green": {"value": 1, "ability": "recovery", "chance": 1}, "blue": {"value": 2, "ability": "slow", "chance": 9}, "yellow": {"value":1, "ability": "invincibility", "chance": 15}}
COLORS = [*FOOD]
CHANCES = [item["chance"] for item in FOOD.values()]

class Food(Turtle):

    def __init__(self, snake_body):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.value_ = 1
        self.ability_ = False
        self.appear(snake_body)


    def appear(self, snake_body):
        while True:
            x_random = random.randint(-13, 13) * 20
            y_random = random.randint(-13, 13) * 20

            overlapping = False

            for part in snake_body:
                if part.distance(x_random, y_random) < 15:
                    overlapping = True
                    break

            if not overlapping:
                color_ = random.choices(COLORS, weights=CHANCES, k=1)[0]
                self.color(color_)
                self.goto(x_random, y_random)
                self.value_ = FOOD[color_]["value"]
                self.ability_ = FOOD[color_]["ability"]
                break