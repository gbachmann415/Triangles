"""
Shrinking triangles
Gunnar Bachmann
triangles.py
9/9/2019
Using recursion to write functions and compose a
program that draws a pattern of triangles.
The program will prompt the user for the recursion
depth.

2 functions:
    init()
        Positions the turtle on the canvas 150 units south from the start position
    and
    triangles(depth, size)
        Recursive function which draws the pattern of triangles
"""
import turtle as t


def init():
    """
    post: pendown, facing east, 150 units south from start position.
    :return:
    """
    t.penup()
    t.right(90)
    t.forward(150)
    t.left(90)
    t.pendown()


def triangles(depth, size):
    """
    precondition: turtle is pendown facing east.
    postcondition: turtle is pendown facing east.

    uses recursion to draw a series of triangles. when depth is less
    than 1, the function will pass. If depth is 1, the function will draw
    a single triangle. As the depth is greater than 1, the function will use
    recursion to draw the pattern of triangles until reaching the base case.

    :param depth: the depth of how many series of the pattern will be drawn
    :param size: the size of the triangles being drawn
    :return:
    """
    if depth < 1:
        pass
    elif depth == 1:
        t.left(120)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.left(120)
    else:
        t.left(120)
        t.forward(size)
        t.right(120)
        triangles(depth-1, size/2)
        t.forward(size)
        triangles(depth-1, size/2)
        t.right(120)
        t.forward(size)
        t.left(120)


if __name__ == '__main__':
    """
    Prompts the user to enter an amount for the depth.
    Then runs the recursive function created to draw the pattern
    of triangles.
    """
    init()
    t.speed(0)
    depth = int(input("Enter depth: "))
    size = 150
    triangles(depth, size)
    t.done()