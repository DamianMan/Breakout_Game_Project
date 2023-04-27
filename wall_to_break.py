from turtle import Turtle


class Walls(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.hideturtle()
        self.speed(0)

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.color(color)
        self.right(90)
        self.penup()
        self.goto(position)
        self.showturtle()


