import time
from turtle import Screen

from borders import Borders
from enemy import Enemy
from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

window = Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
window.bgcolor("black")
window.title("-|| The python Game ||-")
window.tracer(0)

snake = Snake()
enemy = Enemy()
food = Food(snake.body)
score = Scoreboard()
borders = Borders(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

game_on = True
game_pace = 0.1

SPAWN_INTERVAL = 15.0  
ENEMY_LIFESPAN = 10.0  
last_spawn_time = time.time()
enemy_spawn_moment = 0

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.right, "Right")
window.onkey(snake.left, "Left")


def restart_game():
    global game_on, last_spawn_time ,game_pace
    if not game_on:
        snake.reset()
        enemy.clear_enemy()
        score.reset_score()
        food.appear(snake.body)
        last_spawn_time = time.time()
        game_pace = 0.1
        game_on = True
        game()

def game_exit():
    if not game_on:
        window.bye()

snake.invincibility_end_time = 0

def activate_invincibility():
    snake.invincibility = True
    snake.invincibility_end_time = time.time() + 5.0


def ability_handler(ability):
    global game_pace
    if ability:
        if ability == "invincibility":
            activate_invincibility()
        elif ability == "slow":
            if game_pace > 0.1:
                game_pace *= 1.1

        else:
            snake.extend(snake.losed_parts_total)
            score.increase_score(snake.losed_parts_total)
            snake.losed_parts_total = 0


window.onkey(restart_game, "space")
window.onkey(game_exit, "Escape")

def game():
    global game_on, last_spawn_time, enemy_spawn_moment, game_pace

    while game_on:
        snake.move()

        current_time = time.time()

        if not enemy.is_active and (current_time - last_spawn_time >= SPAWN_INTERVAL):
            enemy.spawn(snake)
            enemy_spawn_moment = current_time

        if enemy.is_active:
            if current_time - enemy_spawn_moment >= ENEMY_LIFESPAN:
                enemy.clear_enemy()
                last_spawn_time = time.time()
            else:
                enemy.move_towards(snake.head.pos())

        window.update()
        time.sleep(game_pace)

        if snake.invincibility and time.time() >= snake.invincibility_end_time:
            snake.invincibility = False

        if snake.head.distance(food) < 15:
            ability_handler(food.ability_)
            snake.extend(food.value_)
            score.increase_score(food.value_)
            food.appear(snake.body)
            snake.recolor()
            game_pace *= 0.95

        x, y = snake.head.xcor(), snake.head.ycor()
        if abs(x) > 290 or abs(y) > 290:
            if snake.invincibility:
                snake.head.setx(-290 if abs(x) > 290 else 290)
                snake.head.sety(-290 if abs(y) > 290 else 290)
            else:
                game_on = False
                score.game_over()

        for part in snake.body[4:]:
            if snake.head.distance(part) < 10:
                if snake.invincibility:
                    snake.cutting_parts(snake.body.index(part))
                    score.decrease_score(snake.losed_parts)
                    snake.losed_parts = 0
                    break
                else:
                    game_on = False
                    score.game_over()

        if enemy.is_active and enemy.body:

            if snake.invincibility:
                for enemy_part in enemy.body:
                    if snake.head.distance(enemy_part) < 15:
                        enemy.clear_enemy()
                        score.increase_score(10)  
                        last_spawn_time = time.time()
                        break

            else:
                for i in range(1, len(snake.body)):
                    if enemy.head.distance(snake.body[i]) < 15:
                        snake.cutting_parts(i)
                        score.decrease_score(snake.losed_parts)
                        snake.losed_parts = 0
                        break

                if snake.head.distance(enemy.head) < 15:
                    game_on = False
                    score.game_over()


game()
window.mainloop()