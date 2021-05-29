import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def circle(r=50):
    t.penup()
    t.setpos(0,-1*r)
    t.pendown()
    t.circle(r)
    
circle(50)
circle(100)
circle(200)
