import turtle
def drawPolygon(n, s):
    if n != 0:
        angle = 360/n
        turtle.begin_fill()
        for i in range(n):
            turtle.forward(s)
            turtle.right(angle)
        turtle.end_fill()
        turtle.mainloop()
    else:
        turtle.begin_fill()
        turtle.circle(s)
        turtle.end_fill()
        turtle.mainloop()

drawPolygon(7, 100)