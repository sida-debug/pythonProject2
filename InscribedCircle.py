import turtle
def inscriber(r):
    length = 2*r
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.forward(r)
    turtle.circle(r)
    turtle.mainloop()

inscriber(50)