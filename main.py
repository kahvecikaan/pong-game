import turtle as t
import paddle as p
import ball as b
import time
import scoreboard as s

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = p.Paddle((350, 0))
l_paddle = p.Paddle((-350, 0))
ball = b.Ball()
scoreboard = s.Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddles
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
        ball.bounce_x()
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()
