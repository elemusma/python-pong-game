from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        # self.turtle = Turtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.setpos(position)

    
    def move_up(self):
        if self.ycor() < 250:
            self.forward(10)

    
    def move_down(self):
        if self.ycor() > -240:
            self.backward(10)


class PaddleLeft(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.setpos(-350, 0)
