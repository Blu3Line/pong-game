from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 3
        self.y_move = 3
        self.speed_time = 0.01

    def move(self):
        result = (self.xcor() + self.x_move, self.ycor() + self.y_move)
        self.goto(result)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.speed_time *= 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.speed_time = 0.01
        self.x_bounce()
