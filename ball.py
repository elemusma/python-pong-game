from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.i = 0
        # self.goto(350,250)


    def move(self):
        self.i += 1
        self.goto(self.i, self.i/2)
        print(self.i)