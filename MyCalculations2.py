#**********************************
#Purpose:   Getting started with Python
#           
#
#Input:     Name and numerical data
#           
#
#Output:    Calculations of areas and volumes
#
#Course:        CS 1010
#
#Author:       Yasmeen Hart
#
#Date:      Sept 1, 2020
#
#Program: #2 (MyCalculations2.py)
#*************************************


def shapesDimensions():
    name = str(input("What is your name? \n"))
    radius = float(input("Enter radius: \n"))
    length = int(input("Enter cylinder length: \n"))
    width = int(input("Enter width: \n"))
    height = int(input("Enter height: \n"))
    return name, radius, length, width, height

def circleArea(radius):
    return radius * radius * 3.14159

def rectangleArea(width, height):
    return width * height

def sphereVolume(radius):
    return 4/3 * 3.14159 * (radius * radius * radius)

def cylinderVolume(radius, length):
    return 3.14159 * (radius * radius) * length

def printAll (name, radius, length, width, height, c_area, r_area, s_volume, c_volume, cr_total_area, cr_total_volume):
    print("Radius:           ", radius)
    print("Length:           ", length)
    print("Width:            ", width)
    print("Height:           ", height)
    print("Circle Area:      ", c_area)
    print("Rectangle Area:   ", r_area)
    print("Sphere Volume:    ", s_volume)
    print("Cylinder Volume:  ", c_volume)
    print("Totals: ")
    print("Total areas:      ", cr_total_area)
    print("Total volumes:    ", cr_total_volume)
    print("        Have a Nice Day!")
    
name, radius, length, width, height = shapesDimensions()   
c_area = circleArea(radius)
r_area = rectangleArea(width, height)
s_volume = sphereVolume(radius)
c_volume = cylinderVolume(radius, length)
cr_total_area = c_area + r_area
cr_total_volume = s_volume + c_volume
printAll (name, radius, length, width, height, c_area, r_area, s_volume, c_volume, cr_total_area, cr_total_volume)


