# Python-code-that-creates-a-graphical-loop-of-circles
Python code that creates a graphical loop of circles
n this code, we first import the turtle module and initialize the turtle screen. We set the screen size to 600x600 pixels and the background color to white.

We then create a Turtle object and set the turtle speed to 0 (the fastest possible speed) and the pen color to blue.

Next, we loop through the numbers 1 to 100 using a for loop. For each number, we set the radius of the circle to be drawn as i * 3. We then use the goto and circle methods of the turtle object to draw the circle with the current radius.

After drawing all the circles, we hide the turtle object using the hideturtle method and keep the screen open until the user clicks on it using the exitonclick method.
