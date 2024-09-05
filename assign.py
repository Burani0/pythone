import turtle

def circle(color, pos_vert, pos_horz):
    tr.penup()
    tr.goto(pos_vert, pos_horz)
    tr.pendown()
    tr.color(color)
    tr.circle(45)

def rings():
    colors = ["blue", "black", "red", "yellow", "green"]
    positions = [(-110, -25), (0, -25), (110, -25), (-55, -75), (55, -75)]
    
    for color, position in zip(colors, positions):
        circle(color, *position)

tr = turtle.Turtle()
tr.pensize(5)

rings()


