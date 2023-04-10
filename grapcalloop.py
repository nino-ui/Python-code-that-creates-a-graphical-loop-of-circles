import turtle

# initialize turtle screen
screen = turtle.Screen()

# set screen size and background color
screen.setup(width=600, height=600)
screen.bgcolor("white")

# create turtle object
t = turtle.Turtle()

# set turtle speed and pen color
t.speed(0)
t.pencolor("blue")

# loop through numbers 1 to 100
for i in range(1, 101):
    # set circle radius based on current number
    radius = i * 3
    
    # draw circle
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    
# hide turtle when finished
t.hideturtle()

# keep screen open until user clicks
screen.exitonclick()
