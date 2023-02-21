from turtle import Turtle, Screen
from paddle import Paddle, PaddleLeft
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# tim = Turtle()
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

play_game = True


screen.listen()
screen.onkey(paddle_right.move_up, 'Up')
screen.onkey(paddle_right.move_down, 'Down')
screen.onkey(paddle_left.move_up, 'w')
screen.onkey(paddle_left.move_down, 's')

while play_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect paddle_right missing ball
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()

    # Detect paddle_left missing ball
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
