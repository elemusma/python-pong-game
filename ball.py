from turtle import Turtle
UP = 0
DOWN = 270
start_speed = 0.05

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.ball_speed = 0
        self.speed(self.ball_speed)
        self.shape('circle')
        self.color('white')
        self.speed('slow')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = start_speed
        # self.goto(350,250)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def increase_speed(self):
        self.ball_speed += 1/10
        print(self.ball_speed)


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = start_speed
        self.bounce_x()