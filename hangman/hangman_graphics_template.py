import time
import turtle

# Adjust the speed of the turtle 'fastest', 'fast', 'normal', 'slow', 'slowest'
turtle.speed('slowest')

# Available turtle shapes: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
turtle.shape('turtle')

DEFAULT_PEN_COLOR = "black"

def draw_line(start_x, start_y, end_x, end_y, pen_color):
    # TODO: Draw a line with the given parameters using turtle graphics
    pass

def draw_circle(x, y, radius, pen_color):
    # TODO: Draw a circle with the given parameters using turtle graphics
    pass

def draw_cross(center_x, center_y: int, size: int, pen_color):
    # TODO: Draw a cross with the given parameters using turtle graphics
    pass

def write_text(start_x: int, start_y, text):
    # TODO: Write the given text at the given position using turtle graphics (EXTRA)
    # Return the turtle object that writes the text
    pass


def main():
    # TODO: Draw the base
    # draw_line(, , , , )

    # TODO: Draw the pole
    # draw_line(, , , , )

    # TODO: Draw the  upper beam
    # draw_line(, , , , )

    # TODO: Draw the  rope
    # draw_line(, , , , )

    # TODO: Draw the head
    # draw_circle(, , , )

    # TODO: Draw the body
    # draw_line(, , , , )

    # TODO: Draw arms
    # draw_line(, , , , )
    # draw_line(, , , , )

    # TODO: Draw legs
    # draw_line(, , , , )
    # draw_line(, , , , )

    # TODO: Draw the eyes
    # draw_cross(, , , )
    # draw_cross(, , , )

    turtle.hideturtle()

    # TODO: Write hello world (Extra)
    # text = write_text(, , )
    # time.sleep(2)
    # text.clear()

    # TODO: Write goodbye world (Extra)
    # text = write_text(, , )
    # time.sleep(2)
    # text.clear()

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()