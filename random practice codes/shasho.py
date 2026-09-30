import turtle as t
t.speed(5)
t.bgcolor("black")
t.pensize(5)
def func():
    for i in range(200):
        t.right(1)
        t.forward(1)
t.color('red','pink')
t.begin_fill()
func()
t.left(120)
func()
t.forward(111.65)

t.end_fill()
t.hideturtle()
t.done()
