from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width=1000, height=1000, background="white")

def setInitialValues():
    global level, time, xCharacter, yCharacter, character, characterWidth, characterSpeed
    global characterWalking, xFood, yFood, food, foodWidth, foodSpeed, num
    global foodCaught, caughtPos, ground, topOfStack, stackWidth, xStack
    
    level = 0
    time = 0
    
    xCharacter = 500
    yCharacter = 850 #constant
    character = 0
    characterWidth = 100
    characterSpeed = 0
    characterWalking = False #this mainly serves the purpose of doing the "waddling" movement/animation fo the character

    xFood = [] #once random, then constant
    yFood = []
    food = []
    foodWidth = []
    foodSpeed = []
    
    #temporary variable until i get things sorted out (should technically keep falling but idk...
    num = 5

    foodCaught = []
    caughtPos = []
    ground = yCharacter
    topOfStack = yCharacter
    stackWidth = characterWidth
    xStack = xCharacter
##    FDrawing= 0
def allFoodImages():
    
def loadAllFoods():         #initializing all the x values
    global num, xFood, yFood, food, foodWidth, foodSpeed, foodCaught, caughtPos

    for i in range(0, num):
        x = randint(200, 800)
        y = 100 * randint(-7 , 0)
        img = 0 #need to somehow fill this with food. find if it matches with the order on the side...
        w = randint(50,90) #okay so apparently the food needs to be less wide than the character in order to be catched (?)
                            #nevermind it's not picking up other things too
        s = 3
        p = 0
        catch = False
        
        xFood.append(x)
        yFood.append(y)
        food.append(img)
        foodWidth.append(w)
        foodSpeed.append(s)
        caughtPos.append(p)
        foodCaught.append(catch)
        
    
        
#######
    
def drawBackground():     
    s.create_rectangle(0,0, 1000,800, fill="#ACE7FF", outline="")

    #top part of the building
    s.create_polygon(275,0, 325, 75, 1000, 75, 1000, 0, fill = "#ffc0b3",  outline="")
    s.create_rectangle(350, 75, 1000, 180, fill = "#FFEECC", outline="")
    s.create_rectangle(375, 100, 975, 155, fill = "#FFE6B3", outline="")
    s.create_polygon(375, 100, 975, 100, 975, 115, 390, 115, 390, 155, 375, 155, fill = "#FFDD99", outline="")

    s.create_text(555, 135, text=" - M a r k e t - ", font="Times 30", fill = "#ffab99", anchor = W)

    s.create_polygon(325, 180, 1000, 180, 1000, 210, 340, 210, fill = "#ffc0b3", outline="")
    s.create_rectangle(340, 210, 1000, 225, fill = "#FFAB99", outline="")
    s.create_rectangle(350, 225, 1000, 800, fill="#FFEECC", outline="")

    #door
    s.create_rectangle(800, 500, 970, 800, fill="#FFc0b3", outline="")
    s.create_rectangle(830, 530, 940, 700, fill= "#c6eeff", outline="")
    s.create_polygon(830, 530, 940, 530, 940, 550, 850, 550, 850, 700, 830, 700, fill="#E8D2D1", outline="")
    s.create_rectangle(800, 600, 812, 715, fill="#ffab99", outline="")
    
    #window
    s.create_rectangle(425, 500, 750, 700, fill="#c6eeff", outline="")
    s.create_polygon(425, 500, 750, 500, 750, 525, 450, 525, 450, 700, 425, 700, fill="#E8EEe0", outline="")

    s.create_polygon(650, 500, 710, 500, 635, 700, 575, 700, fill="#dff6ff", outline="")
    s.create_polygon(730, 500, 750, 500, 675, 700, 655, 700, fill="#dff6ff", outline="")

    s.create_rectangle(415, 700, 765, 720, fill="#ffdd99", outline="")
    
    
    #The shading roof
    s.create_polygon(350, 235, 1000, 235, 1000, 400, 275, 400, fill = "white", outline="")
    for i in range(8):
        x1 = 350 + 100*i
        x2 = x1 + 50
        x3 = x2 - 75
        x4 = x1 - 75
        y1 = 235
        y2 = 400
        s.create_polygon(x1, y1, x2, y1, x3, y2, x4, y2, fill="#dfdfdf", outline="")
        
    s.create_rectangle(275, 400, 1000, 470, fill= "#efefef", outline="")
    for i in range(8):
        x1 = 275 + 100*i
        x2 = x1 + 50
        y1 = 400
        y2 = 470
        s.create_rectangle(x1, y1, x2, y2, fill = "#b2b2b2", outline="")
    
    

def drawForeground():
    s.create_rectangle(-10, 800, 1010, 1010, fill="#ecd4ff", outline="#c5a3ff", width=5)

##def foodToCatch():
##    #create all the variable for the foods
    
def drawCharacter():
    global xCharacter, yCharacter, characterWidth, character

    character = s.create_rectangle( xCharacter, yCharacter, xCharacter + characterWidth, yCharacter + characterWidth, fill = "red")

def drawFood():
    global xFood, yFood, foodWidth, food
    for i in range(num):
        food[i] = s.create_rectangle(xFood[i], yFood[i], xFood[i] + foodWidth[i], yFood[i] + foodWidth[i], fill="blue")

def updateCharacter():
    global xCharacter, characterSpeed
    
    xCharacter = xCharacter + characterSpeed

def updateFood():
    global yFood, xFood, foodSpeed, foodCaught, caughtPos

    for i in range(num):
        if foodCaught[i] == False:
            yFood[i] += foodSpeed[i]
        else:
            xFood[i] = xCharacter + caughtPos[i]


def caughtTheFood():
    global xFood, yFood, xCharacter, topOfStack, stackWidth, yCharacter, foodSpeed, foodCaught, caughtPos, ground, xStack
    for i in range(num):
        #If the food is above the stack ADD NEW VARIABLE WIDTHOFSTACK
        if xFood[i] + foodWidth[i] <= xStack or xFood[i] <= xStack + stackWidth:

            #if the bottom of the food goes below the character
            if yFood[i] + foodWidth[i] >= topOfStack and yFood[i] >= topOfStack + foodWidth[i] and foodCaught[i] == False:
                yFood[i] = topOfStack - foodWidth[i]
                caughtPos[i] = xFood[i] - xCharacter #need to fix this 
                foodSpeed[i] = 0
                foodCaught[i] = True
                stackWidth = foodWidth[i]
                xStack = xFood[i]

def updateStackStatus(): #Grrrrr. No Yayyyyy. Works but still uses the character width even up of the stack
    global topOfStack
    
    topOfStack = yCharacter
    for i in range(num):
        if foodCaught[i] == True:
            topOfStack -= foodWidth[i]
    
########

def runGame():
    global xFood, yFood, xCharacter, yCharacter
    setInitialValues()
    loadAllFoods()
    drawBackground()

    while True:
        updateCharacter()
        updateFood()
        drawCharacter()
        drawFood()
        updateStackStatus()
        caughtTheFood()

        s.update()
        sleep(0.03)
        s.delete(character)
        for i in range(num):
            s.delete( food[i] )


##def mouseClickHandler( event ):
##    global xSpeedPM, ySpeedPM, xMouse, yMouse
##
##    xMouse = event.x
##    yMouse = event.y
##
##    xSpeedPM = ...some formula that uses xMouse, yMouse
##    ySpeedPM = ...some formula that uses xMouse, yMouse


def keyUpHandler( event ):
    global characterSpeed, characterWalking

    if event.keysym == "Left" or event.keysym == "Right":
        characterSpeed = 0 #makes the ball stop moving when the user lets go of the arrow keys
        characterWalking = False
        
def keyDownHandler( event ):
    global characterSpeed  #because we'll be changing these values in this procedure
    
    if event.keysym == "Left":     #LEFT ARROW WAS PRESSED
        characterSpeed = -5  #sets the xSpeed to a negative value so that the ball will move to the left
        characterWalking = True
        
    elif event.keysym == "Right":  #RIGHT ARROW WAS PRESSED
        characterSpeed = 5
        characterWalking = True



#At the bottom
root.after( 5, runGame )
##s.bind( "<Button-1>", mouseClickHandler )  #will need this for button clicking
s.bind( "<Key>", keyDownHandler )
s.bind( "<KeyRelease>", keyUpHandler)
s.pack()
s.focus_set()
root.mainloop()
