# from curses.textpad import rectangle
# from turtle import circle

# from numpy import square

#area calculation of different shapes

Ask = input("Enter the shape you want to calculate area for (circle, square, rectangle): ")
if Ask.lower() == "circle":
    radius = float(input("Enter the Radius of the circle: "))
    area = 3.14 * radius * radius
    print("The area of the circle is:", area)
elif Ask.lower() == "square":
    side = float(input("Enter the Side of the square: "))
    area = side * side
    print("The area of the square is:", area)
elif Ask.lower() == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("The area of the rectangle is:", area)
else:
    print("Invalid shape selected")
