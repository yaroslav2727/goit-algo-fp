import turtle

def pythagorean_tree(t, length, angle, level):
    if level == 0:
        return
    
    t.forward(length)
    
    x, y = t.position()
    current_angle = t.heading()
    
    t.left(angle)
    pythagorean_tree(t, length * 0.7, angle, level - 1)
    
    t.penup()
    t.goto(x, y)
    t.setheading(current_angle)
    t.pendown()
    
    t.right(90 - angle)
    pythagorean_tree(t, length * 0.7, angle, level - 1)
    
    t.penup()
    t.goto(x, y)
    t.setheading(current_angle)
    t.pendown()


screen = turtle.Screen()
screen.title("Pythagorean Tree Fractal")
screen.bgcolor("white")
    
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.left(90)
    
t.penup()
t.goto(0, -200)
t.pendown()

recursion_level = 0
while recursion_level <= 0:
    try:
        recursion_level = int(input("Введіть рівень рекурсії: "))
        if recursion_level <= 0:
            raise ValueError
    except ValueError:
            print("Будь ласка, введіть ціле додатнє число.")
        
pythagorean_tree(t, 100, 45, recursion_level)
    
t.hideturtle()
screen.mainloop()