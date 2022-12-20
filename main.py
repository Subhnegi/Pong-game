
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
BACKGROUND_COLOR = "green"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("=====PONG GAME=====")
screen.tracer(0)
screen_part = Turtle("square")
screen_part.pensize(5)
screen_part.hideturtle()
screen_part.speed(0)
screen_part.pencolor("white")
screen_part.penup()
screen_part.goto(x=0, y=300)
screen_part.pendown()
screen_part.setheading(270)
for _ in range(22):
    screen_part.forward(15)
    screen_part.penup()
    screen_part.forward(15)
    screen_part.pendown()

#paddle controls
l_paddle = Paddle((-580,0))
r_paddle = Paddle((580,0))
screen.listen()
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')

#ball setup
ball=Ball()

score_board=Score_board()

game_is_on=True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    

    #detect wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        #bounce ball
        ball.bounce_y()

    #detect paddle collision
    if ball.distance(l_paddle)<50 and ball.xcor()<-550   or ball.distance(r_paddle)<50 and ball.xcor()>550:
        ball.bounce_x()
        ball.speed()
    
    #detecting if ball has gone out of bounds

    if ball.xcor()>580:
        score_board.l_point()
        ball.reset()
        
    
    if ball.xcor()<-580:
        score_board.r_point()
        ball.reset()





screen.exitonclick()
