from turtle import Screen
import paddle
import scoreboard
from ball import Ball
import time
import scoreboard

root = Screen()
root.setup(width=800, height=600)
root.bgcolor("black")
root.title("Pong Game")
root.tracer(0)  # animasyonu kapıyor
root.listen()

pad1 = paddle.Paddle(350, 0)
root.onkeypress(pad1.go_up, "Up")
root.onkeypress(pad1.go_down, "Down")

pad2 = paddle.Paddle(-350, 0)
root.onkeypress(pad2.go_up, "w")
root.onkeypress(pad2.go_down, "s")

ball = Ball()

scboard = scoreboard.Scoreboard()

game_on = True

while game_on:
    time.sleep(ball.speed_time)
    root.update()
    ball.move()
    #ust duvarlarla etkileşimi
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    #user padel ile etkileşimi
    if ball.distance(pad1) < 55 and ball.xcor() > 330 or ball.distance(pad2) < 55 and ball.xcor() < -330:
        ball.x_bounce()
    #eğer top tutamazsa right side
    if ball.xcor() > 380:
        ball.reset_position()
        scboard.l_score += 1
        scboard.update_sc()

    #eğer top tutmazsa left side
    if ball.xcor() < -380:
        ball.reset_position()
        scboard.r_score += 1
        scboard.update_sc()
root.mainloop()
