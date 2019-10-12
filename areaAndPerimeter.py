shape = input("Enter a shape.")
if (shape=="triangle"):
    trianglebase = int(input("Enter base."))
    triangleheight = int(input("Enter height."))
    trianglearea = float(0.5*trianglebase*triangleheight)
    print("The area of the triangle is: ", trianglearea)
elif (shape=="square"):
    squareside = int(input("Enter side of the square."))
    squarearea = float(squareside**2)
    print("The area of the square is: ", squarearea)
elif (shape=="rectangle"):
    length = int(input("What is the length of the rectangle?"))
    width = int(input("Also enter the width of the rectangle?"))
    rectanglearea = float(length*width)
    print("The area of the rectangle is: ", rectanglearea)
elif (shape=="parallelogram"):
    parbase = int(input("What is the length of the base of your parallelogram?"))
    parheight = int(input("What is the height of your parallelogram?"))
    pararea = float(parbase*parheight)
    print("The area of the parallelogram is: ", pararea)
elif (shape=="trapezoid"):
    base1 = int(input("What is base number 1 in your trapezoid?"))
    base2 = int(input("What is base number 2 in your trapezoid?"))
    trapezoidheight= int(input("What is the height of your trapezoid?"))
    trapezoidarea = float(((base1 + base2)/2)*trapezoidheight)
    print("The area of the trapezoid is: ", trapezoidarea)
elif (shape=="circle"):
    radius = int(input("What is the radius of your circle?"))
    circlearea = float(3.14*(radius**2))
    print("The area of the circle is: ", circlearea)
elif (shape=="rhombus"):
    rhombusside = int(input("What is the length of a side of your rhombus?"))
    rhombusheight = int(input("What is the height of your rhombus?"))
    rhombusarea = float(rhombusside*rhombusheight)
    print("The area of the rhombus is: ", rhombusarea)
else:
    print("ERROR")
