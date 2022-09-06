from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor: int, y_cor: int):
        super().__init__()
        self.penup()
        self.shape("square")  # create a 20x20 pxl square
        self.shapesize(stretch_wid=5, stretch_len=1)  # make it into 100x20 rectangle
        self.color("white")
        self.goto(x=x_cor, y=y_cor)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 30)
