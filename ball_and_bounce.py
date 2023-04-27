from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.showturtle()
        self.x_move = 3
        self.y_move = 3
        self.new_x = 0
        self.new_y = 0






    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)

    def bounce_x(self):
        self.x_move *= -1


    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        x = random.randint(-300, 300)
        self.goto(x, -300)













