import turtle
from turtle import *
from create_paddle import Paddle
from wall_to_break import Walls
from ball_and_bounce import Ball
import random





colors = ['#00FFD1', '#31C6D4', 'yellow', 'red']
x = -318
y = 300
score = 0
life = 5

#----------SETUP SCREEN-------------
screen = Screen()
screen.setup(width=755, height=800)
screen.bgcolor('#B7C4CF')
screen.title('Breakout Game')
screen.tracer(0)

#Scoreboard
def scoreboard():
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(280,350)
    turtle.write(f'Points: {score}', align='center', font=("Helvetica", 30, "bold"))
scorebaord = scoreboard()


#-------CREATE USER PADDLE----------
paddle = Paddle((0, -330))



#-----------SETTINS SCREEN FOR USER CLICK EVENT
screen.listen()
screen.onkey(paddle.move_right, 'Right')
screen.onkey(paddle.move_left, 'Left')


#---------CREATE WALLS TO BREAK---------
x_pos = 0
n_color = 0
keys = range(49)
dictionary_breaks = dict(zip(keys, [None] * len(keys)))
for n in dictionary_breaks:
    dictionary_breaks[n] = Walls((x + x_pos, y), colors[n_color])
    x_pos += 105

    if n > 0 and n % 7 == 0:
        n_color += 1
        if n_color == 4:
            n_color = 0
        x_pos = 0

        y -= 50
        dictionary_breaks[n] = Walls((x + x_pos, y), colors[n_color])
        x_pos += 105
print(len(dictionary_breaks))



#--------------CREATE BALL---------------

ball = Ball((0, -300))


game_on = True
time = 0
hit = 0

while game_on:
    screen.update()

    ball.move()
    time += 1

    #Ball bounce margin X
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.bounce_x()
    #Ball bounce top margin y
    if ball.new_y > 375:
        ball.bounce_y()
    #Check Hit paddle
    if time > 20:
        if ball.distance(paddle) < 50 and ball.ycor() < -300 :
            ball.bounce_y()
    #Reset position ball
    if ball.new_y < -420:
        ball.reset_ball()
        ball.bounce_y()
        list = [0, ball.bounce_x()]
        random.choice(list)
        #Countdown life
        life -= 1
        if life == 0:
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(0, 0)
            turtle.color('#FF1E1E')
            turtle.write(f"YOU LOSE WITH {score} POINTS 👎", align="center", font=("Helvetica", 40, "bold"))
            game_on = False

    #Check hit with the breaks
    for n in dictionary_breaks:
        if ball.distance(dictionary_breaks[n]) < 50:
            dictionary_breaks[n].goto(1000,0)
            ball.bounce_y()
            screen.update()
            hit += 1
            score += 1
            turtle.clear()
            scoreboard()

            #Check for the win
            if hit == 49:
                turtle.penup()
                turtle.hideturtle()
                turtle.goto(0, 0)
                turtle.color('#2192FF')
                turtle.write(f"YOU WIN WITH {score} POINTS! 👍", align="center", font=("Helvetica", 40, "bold"))
                game_on = False



screen.exitonclick()
