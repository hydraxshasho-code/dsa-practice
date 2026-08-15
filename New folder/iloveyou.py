import turtle as t

t.speed(10)
t.bgcolor("black")
t.pensize(3)
t.hideturtle()
def arc():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.penup()
t.goto(0, -100)         
t.setheading(140)       
t.pendown()

t.color('red', 'pink')
t.begin_fill()

arc()                  
t.left(120)
arc()                   
t.forward(111.65)       

t.end_fill()
t.penup()
t.goto(0, -160)         
t.color('white')
t.write("I love you lallu", align="center", font=("Arial", 20, "bold italic"))

t.done()