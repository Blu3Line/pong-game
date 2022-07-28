from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")

        self.shapesize(stretch_len=1, stretch_wid=5)

        self.setpos(x_pos, y_pos)

    def go_up(self):
        result = (self.xcor(), self.ycor() + 20)
        self.goto(result)

    def go_down(self):
        result = (self.xcor(), self.ycor() - 20)
        self.goto(result)
