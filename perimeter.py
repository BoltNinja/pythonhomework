shape = input("Enter shape.")
if (shape=="triangle"):
    side1 = int(input("What is the length of the first side?"))
    side2 = int(input("What is the length of the second side?"))
    side3 = int(input("What is the length of the third side?"))
    triangleperimeter = (side1 + side2 + side3)
    print("The perimeter of the triangle is: ", triangleperimeter)
elif (shape=="square"):
    squareside = int(input("What is the length of a side of your square?"))
    squareper = squareside*4
    print("The perimeter of your square is: ", squareper)
elif (shape=="rectangle"):
    reclength = int(input("What is the length of your rectangle"))
    recwidth = int(input("What is the width of your rectangle"))
    recper = 2*reclength + recwidth*2
    print("The area of thte rectangle is: ", recper)
elif (shape=="parallelogram"):
    length = int(input("What is the length of your parallelogram?"))
    width = int(input("What is the width of your parallelogram?"))
    parper = 2*length + 2*width
    print("The perimeter of the parallelogram is: ", parper)
elif (shape=="trapezoid"):
    sside1 = int(input("What is side number 1?"))
    sside2 = int(input("What is side number 2?"))
    sside3 = int(input("What is side number 3?"))
    sside4 = int(input("What is side number 4?"))
    print("The perimeter is: ", sside1+sside2+sside3+sside4)
elif (shape=="circle"):
    radius = int(input("What is the radius?"))
    circum = float(radius*6.28)
    print("The circumference is: ", circum)
elif (shape=="rhombus"):
    ssside = int(input("What is the length of a side of your rhombus?"))
    rhombusper = 4*ssside
    print("The perimeter of the rhombus is: ", rhombusper)
else:
    print("ERROR")