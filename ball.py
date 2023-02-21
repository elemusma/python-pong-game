from turtle import Turtle
UP = 0
DOWN = 270

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.color('white')
        self.speed('slow')
        self.penup()
        self.x_move = 1
        self.y_move = 1
        # self.goto(350,250)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()