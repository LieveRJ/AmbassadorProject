import time
import turtle

# Adjust the speed of the turtle 'fastest', 'fast', 'normal', 'slow', 'slowest'
turtle.speed('slowest')

# Available turtle shapes: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
turtle.shape('turtle')

DEFAULT_PEN_COLOR = "black"

def draw_circle(x, y, radius, pen_color):
    turtle.penup()
    turtle.pencolor(pen_color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)


def draw_line(start_x, start_y, end_x, end_y, pen_color):
    turtle.penup()
    turtle.pencolor(pen_color)
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)


def draw_cross(center_x, center_y, size, pen_color):
    draw_line(center_x, center_y, center_x + size, center_y + size, pen_color)
    draw_line(center_x + size, center_y, center_x, center_y + size, pen_color)


def write_text(start_x, start_y, text):
    erasable_text = turtle.Turtle()
    erasable_text.penup()
    erasable_text.setpos(start_x, start_y)
    erasable_text.write(text, font=("Arial", 16, "normal"))
    erasable_text.hideturtle()

    return erasable_text


def main():
    # Draw base
    draw_line(0, 0, 100, 0, DEFAULT_PEN_COLOR)

    # Draw pole
    draw_line(10, 0, 10, 100, DEFAULT_PEN_COLOR)

    # Draw top
    draw_line(10, 100, 50, 100, DEFAULT_PEN_COLOR)

    # Draw rope
    draw_line(50, 100, 50, 80, DEFAULT_PEN_COLOR)

    # Draw head
    draw_circle(50, 70, 10, DEFAULT_PEN_COLOR)

    # Draw body
    draw_line(50, 60, 50, 30, DEFAULT_PEN_COLOR)

    # Draw hands
    draw_line(50, 50, 40, 40, DEFAULT_PEN_COLOR)
    draw_line(50, 50, 60, 40, DEFAULT_PEN_COLOR)

    # Draw legs
    draw_line(50, 30, 40, 20, DEFAULT_PEN_COLOR)
    draw_line(50, 30, 60, 20, DEFAULT_PEN_COLOR)

    # Draw eyes
    draw_cross(45, 72, 2, DEFAULT_PEN_COLOR)
    draw_cross(52, 72, 2, DEFAULT_PEN_COLOR)

    turtle.hideturtle()

    # turtle print
    text = write_text(0, -25, "Hello World!")
    time.sleep(2)
    text.clear()

    text = write_text(0, -25, "Goodbye World!")
    time.sleep(2)
    text.clear()

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
