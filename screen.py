from turtle import Turtle, Screen
from paddle import Paddle, PaddleLeft



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

tim = Turtle()
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

play_game = True


screen.listen()
screen.onkey(paddle_right.move_up, 'Up')
screen.onkey(paddle_right.move_down, 'Down')
screen.onkey(paddle_left.move_up, 'w')
screen.onkey(paddle_left.move_down, 's')

while play_game:
    screen.update()

screen.exitonclick()
