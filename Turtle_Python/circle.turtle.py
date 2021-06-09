import turtle    
turtle.title("@aaditya.co")         
my_wn = turtle.Screen()
turtle.bgcolor("yellow")
turtle.pencolor("red")
turtle.speed(10.5)
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()