from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('blue')
        self.right(90)
        self.penup()
        self.goto(position)
        self.showturtle()
        self.x = self.xcor()
        self.y = self.ycor()



    def move_right(self):
        new_x = self.xcor() + 30
        if new_x < 340:
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        if new_x > -340:

            self.goto(new_x, self.ycor())


