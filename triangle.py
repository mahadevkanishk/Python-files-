import math

# Function to calculate area of triangle
def area(base, height):
    return 0.5 * base * height

# Function to calculate perimeter of triangle
def perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Function to calculate semi-perimeter of triangle
def semi_perimeter(side1, side2, side3):
    return (side1 + side2 + side3) / 2

# Function to calculate area of triangle using Heron's formula
def herons_area(side1, side2, side3):
    s = semi_perimeter(side1, side2, side3)
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
