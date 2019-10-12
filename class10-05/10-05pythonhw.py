#homework is to make a program for the perimeter and area of a triangle, square, rectangle, parallelogram, circle, rhombus, and trapeziod.
import math
triangle = "triangle"
square = "square"
rectangle = "rectangle"
parallelogram = "parallelogram"
circle = "circle"
rhombus = "rhombus"
trapezoid = "trapezoid"
print("Which of these shapes do you want to find the perimeter and area?")
print("A triangle, square, rectangle, parallelogram, circle, rhombus, or a trapezoid?")
shape = input(print(""))
if shape == pentagon
    triangleside1 = input("What is the measurement of the first side (the base of your triangle) of the triangle?")
    triangleside2 = input("What is the measurement of the second side of the triangle?")
    triangleside3 = input("What is the measurement of the third side of the triangle?")
    triangleheight = input("What is the height of your triangle?")
    triangleper = triangleside1 + triangleside2 + triangleside3
    trianglearea = 0.5*triangleheight*triangleside1
    print("The perimeter of the triangle is " + triangleper)
    print("The triangle's area is " + trianglearea)
    if shape == square :
        squareside = input("What is the length of one side of your square?")
        squareper = 4*squareside
        squarearea = squareside^2
        print("The perimeter of your square is " + squareper)
        print("The area of this square is " + squarearea)
        if shape == rectangle :
            rectanglelength = input(print("What is the length of your rectangle?"))
            rectanglewidth =  input(print("What is the with of your rectangle?"))
            rectangleper  = (2 * rectanglewidth) + (2*rectanglelength)
            rectanglearea = rectanglewidth * rectanglelength
    print("The perimeter of the rectangle is " + rectangleper)
    print("The area of the rectangle is " + rectanglearea)
    if shape == parallelogram :
        rectanglelength2 = input(print("What is the length of your parallelogram?"))
        rectanglewidth2 = input(print("What is the with of your parallelogram?"))
        rectangleper2 = (2 * rectanglewidth2) + (2 * rectanglelength2)
        rectanglearea2 = rectanglewidth2 * rectanglelength2
    print("The perimeter of the parallelogram is " + rectangleper2)
    print("The area of the parallelogram is " + rectanglearea2)
    if shape == rhombus :
        rhombuslength = input("What is the length of your rhombus?")
        rhombusheight = input("What is the height of your rhombus?")
        rhombusper = 4*rhombuslength
        rhombusarea = rhombuslength * rhombusheight
        print("The perimeter of your rhombus is " + rhombusper)
        print("area of your rhombus is " + rhombusarea)
        if shape == circle :
            pi = math.pi
        radius = input("What is the radius of your circle?")
        circumference = 2*radius*pi
        circlearea    = pi*radius*radius
        print("The area of your circle is " + circlearea)
        print("The perimeter(circumference) of your circle is " + circumference)
        if shape == trapezoid :
            base1 = input(print("What is the length of the top base(base number 1)"))
            base2 = input(print("What is the length of the bottom base(base number 2)"))
            print("There are two sides in a trapezoid other than the bases.")
            side1 = input(print("Give one of those sides."))
            side2 = input(print("Give the other side."))
            height = input(print("What is the height of your trapezoid?"))
            trapeziodarea = ((base1 + base2)/2) *height
            trapeziodper =  base1 + base2 + side1 + side2