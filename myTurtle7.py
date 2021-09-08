#******************************************************
#   Purpose: Draw different animations using the turtle extension
#
#   Author: Yasmeen Hart
#
#   Course: CS 1010
#
#   Date: 10.23.2020
#
#   Program: myturtle7.py
#
#******************************************************

import turtle

ANIMATION_SPEED = 0
BASE_X = 0
BASE_Y = -200
BASE_RADIUS = 100
MID_X = 0
MID_Y = 0
MID_RADIUS = 60

RIGHT_ARM_X1 = 60
RIGHT_ARM_Y1 = 60
RIGHT_ARM_X2 = 108
RIGHT_ARM_Y2 = 75
RIGHT_ARM_X3 = 118
RIGHT_ARM_Y3 = 75
RIGHT_ARM_X4 = 118
RIGHT_ARM_Y4 = 85

LEFT_ARM_X1 = -60
LEFT_ARM_Y1 = 60
LEFT_ARM_X2 = -105
LEFT_ARM_Y2 = 70
LEFT_ARM_X3 = -120
LEFT_ARM_Y3 = 110
LEFT_ARM_X4 = -130
LEFT_ARM_Y4 = 115
LEFT_ARM_X5 = -120
LEFT_ARM_Y5 = 125

HEAD_X = 0
HEAD_Y = 120
HEAD_RADIUS = 40

LEFT_EYE_X = -20
LEFT_EYE_Y = 170
RIGHT_EYE_X = 20
RIGHT_EYE_Y = 170
EYE_RADIUS = 5

MOUTH_START_X = -25
MOUTH_START_Y = 140
MOUTH_END_X = 25
MOUTH_END_Y = 140

HAT_X1 = -50
HAT_Y1 = 180
HAT_X2 = 50
HAT_Y2 = 180
HAT_X3 = 50
HAT_Y3 = 205
HAT_X4 = -50
HAT_Y4 = 205
HAT_X5 = -30
HAT_Y5 = 205
HAT_X6 = 30
HAT_Y6 = 205
HAT_X7 = 30
HAT_Y7 = 245
HAT_X8 = -30
HAT_Y8 = 245

#change variable from "turtle" to "t"
t = turtle.Turtle()

#beginning of snowman drawing

def drawBase():
#draws base of snowman
    t.penup()
    t.goto(BASE_X, BASE_Y)
    t.pendown()
    t.circle(BASE_RADIUS)

def drawMidSection():
#draws mid section of snowman
    t.penup()
    t.goto(MID_X, MID_Y)
    t.pendown()
    t.circle(MID_RADIUS)
    

def drawArms():  
    #draws right arm of snowman
    t.penup()
    t.goto(RIGHT_ARM_X1, RIGHT_ARM_Y1)
    t.pendown()
    t.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    t.goto(RIGHT_ARM_X3, RIGHT_ARM_Y3)
    t.penup()
    t.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    t.pendown()
    t.goto(RIGHT_ARM_X4, RIGHT_ARM_Y4)
    
    #draws left arm of snowman
    t.penup()
    t.goto(LEFT_ARM_X1, LEFT_ARM_Y1)
    t.pendown()
    t.goto(LEFT_ARM_X2, LEFT_ARM_Y2)
    t.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    t.goto(LEFT_ARM_X4, LEFT_ARM_Y4)
    t.penup()
    t.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    t.pendown()
    t.goto(LEFT_ARM_X5, LEFT_ARM_Y5)

def drawHead():
#draws head of the snowman
    t.penup()
    t.goto(HEAD_X, HEAD_Y)
    t.pendown()
    t.circle(HEAD_RADIUS)
    
    #draws left eye
    t.penup()
    t.goto(LEFT_EYE_X, LEFT_EYE_Y)
    t.pendown()
    t.circle(EYE_RADIUS)
    
    #draws right eye
    t.penup()
    t.goto(RIGHT_EYE_X, RIGHT_EYE_Y)
    t.pendown()
    t.circle(EYE_RADIUS)
    
    #draws mouth
    t.penup()
    t.goto(MOUTH_START_X, MOUTH_START_Y)
    t.pendown()
    t.goto(MOUTH_END_X, MOUTH_END_Y)

def drawHat():
    #draws brim of hat
    t.penup()
    t.goto(HAT_X1, HAT_Y1)
    t.begin_fill()
    t.goto(HAT_X2, HAT_Y2)
    t.goto(HAT_X3, HAT_Y3)
    t.goto(HAT_X4, HAT_Y4)
    t.end_fill()
    
    #draws top of hat
    t.penup()
    t.goto(HAT_X5, HAT_Y5)
    t.begin_fill()
    t.goto(HAT_X6, HAT_Y6)
    t.goto(HAT_X7, HAT_Y7)
    t.goto(HAT_X8, HAT_Y8)
    t.end_fill()

#end of snowman drawing

#beginning of original drawing
def drawHouse():
#draws main building
    t.reset()
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(200)

def drawRoof():
#draws roof
    t.penup()
    t.pendown()
    t.left(90)
    t.forward(40)
    t.right(150)
    t.forward(275)
    t.right(60)
    t.forward(275)
    t.right(150)
    t.forward(40)

def drawDoor():
#draws entry door
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(75)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(100)

#draws door knobs
    #left knob
    t.penup()
    t.goto(-15, -50)
    t.pendown()
    t.circle(5)

    #right knob
    t.penup()
    t.goto(5, -50)
    t.pendown()
    t.circle(5)

def drawWindows():
    #draws left window
    t.penup()
    t.goto(-110, 20)
    t.pendown()
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    
    #draws spokes on left window
    t.penup()
    t.goto(-135, 20)
    t.pendown()
    t.goto(-135, -55)
    t.penup()
    t.goto(-110, -20)
    t.pendown()
    t.goto(-160, -20)

    #draws right window
    t.penup()
    t.goto(160, 20)
    t.pendown()
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)

    #draws spokes on right window
    t.penup()
    t.goto(135, 20)
    t.pendown()
    t.goto(135, -55)
    t.penup()
    t.goto(110, -20)
    t.pendown()
    t.goto(160, -20)

    #draws center circle window
    t.penup()
    t.goto(0, 25)
    t.pendown()
    t.circle(35)

    #draws spokes on center window
    t.penup()
    t.goto(0, 95)
    t.pendown()
    t.goto(0, 25)
    t.penup()
    t.goto(-35, 60)
    t.pendown()
    t.goto(35, 60)
    
def drawChimney():
#draws chimney
    t.penup()
    t.goto(120, 168)
    t.pendown()
    t.goto(120, 280)
    t.forward(70)
    t.right(90)
    t.forward(160)
        
#end of original drawing
    
def snowman():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()

def myown():
    drawHouse()
    drawRoof()
    drawDoor()
    drawWindows()
    drawChimney()

def main():
    snowman()
    myown()

main()
    
