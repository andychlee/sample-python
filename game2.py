from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width=1000, height=1000, background="white")

#Classes to have the same image for every butter and check if that butter has been caught
class Food:
    def __init__(self, x, y, width, height, speed, image):
        self.x1 = x
        self.x2 = x + width
        self.y = y

        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.alreadyCaught = False
        self.valid = 0
        #HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.triedCatch = False
        
    def caughtTheFood(self, xOfStack, widthOfStack, top):
        #checks if the y value is below or on the top of the stack but not so below that the item shouldn't even be caught
        #HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self.alreadyCaught == True:
            return True
        else:
            if self.y + 0.5* self.height >= top and self.y <= top + 0.5 * self.height:
                #checks if the x should be caught THE PROBLEM MUST BE HERE
                if self.x2 < xOfStack or self.x1 > xOfStack + widthOfStack:
                    return False
                else:
                    return True
            else:
                return False
        
    def drawFood(self, screen):
        self.drawing = screen.create_image(self.x1, self.y, image=self.image, anchor =W)
    def removeFood(self, screen):
        screen.delete(self.drawing)
    
        
class Butter(Food):
    w = 100
    h = 75
    image = PhotoImage(file="butterImg2.gif")
    def __init__(self, x, y, speed):
        Food.__init__(self, x, y, self.w, self.h, speed, self.image)
        
class Eggs(Food):
    w = 100
    h = 75
    image = PhotoImage(file="eggsImg2.gif")
    def __init__(self, x, y, speed):
        Food.__init__(self, x, y, self.w, self.h, speed, self.image)

class Flour(Food):
    w = 100
    h = 100
    image = PhotoImage(file="flourImg2.gif")
    def __init__(self, x, y, speed):
        Food.__init__(self, x, y, self.w, self.h, speed, self.image)

class Milk(Food):
    w = 100
    h = 100
    image = PhotoImage(file="milkImg2.gif")
    def __init__(self, x, y, speed):
        Food.__init__(self, x, y, self.w, self.h, speed, self.image)

class Sugar(Food):
    w = 100
    h = 100
    image = PhotoImage(file="sugarImg2.gif")
    def __init__(self, x, y, speed):
        Food.__init__(self, x, y, self.w, self.h, speed, self.image)

###
        
def setInitialValues():
    global gameMode, level, lives, liveHeart, hearts
    global xCharacter, yCharacter, character, characterImg, characterWidth, characterHeight, characterSpeed, characterWalking
    global foodList, foodSpeed, wrongImg, marking # i won't need any of these lists if i do the class thing
    global ground, topOfStack, stackWidth, xStack, shoppingList, item1, item2, listImg
##    global introImg, instructionImg, quitImg, successImg, totalSuccessImg, failImg

    gameMode = "IntroScreen"
    level = 0
    lives = 3
    liveHeart = PhotoImage(file="heart.gif")
    hearts = []
    
    xCharacter = 500
    yCharacter = 800 #constant
    character = 0
    characterImg = PhotoImage(file="bag.gif")
    characterWidth = 130
    characterHeight = 90
    characterSpeed = 0

    foodList = []
    foodSpeed = 4
    wrongImg = PhotoImage(file="bigFatX.gif")
    marking = 0

    ground = yCharacter
    topOfStack = yCharacter
    stackWidth = characterWidth
    xStack = xCharacter
    shoppingList = []
    item1 = 0
    item2 = 0
    listImg = PhotoImage(file="list.gif").subsample(2, 2)

    #introImg = PhotoImage(file="startingScreenImg.gif")
    #instructionImg = PhotoImage(file="")
    #quitImg = PhotoImage(file="")
    #successImg = PhotoImage(file="successScreenImg.gif")
    #totalSuccessImg = PhotoImage(file="")
    #failImg = PhotoImage(file="failScreenImg.gif")
    
def fillShoppingList():
    global shoppingList
    for i in range(7):
        xValue = randint(250, 850)
        yValue = 100*randint(-50, 0)
        newItem = 0
        a = randint(0,4)
        if a == 0:
            newItem = Butter(xValue, yValue, foodSpeed)
        elif a == 1:
            newItem = Eggs(xValue, yValue, foodSpeed)
        elif a == 2:
            newItem = Flour(xValue, yValue, foodSpeed)
        elif a == 3:
            newItem = Milk(xValue, yValue, foodSpeed)
        else:
            newItem = Sugar(xValue, yValue, foodSpeed)
        shoppingList.append(newItem)
        
def loadFood(): 
    global foodList
    xValue = randint(250, 850)
    yValue = 100*randint(-5, 0)
    newItem = 0
    a = randint(0,4)
    if a == 0:
        newItem = Butter(xValue, yValue, foodSpeed)
    elif a == 1:
        newItem = Eggs(xValue, yValue, foodSpeed)
    elif a == 2:
        newItem = Flour(xValue, yValue, foodSpeed)
    elif a == 3:
        newItem = Milk(xValue, yValue, foodSpeed)
    else:
        newItem = Sugar(xValue, yValue, foodSpeed)
    foodList.append(newItem)
        

#######
    
def drawBackground():
    global item1, item2
    
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

    s.create_image(20, 10, image=listImg, anchor = NW)
    s.create_rectangle(-10, 800, 1010, 1010, fill="#ecd4ff", outline="#c5a3ff", width=5)

    #initial shopping list
    item1 = s.create_image(90, 280, image=shoppingList[1].image, anchor = W)
    item2 = s.create_image(90, 380, image=shoppingList[0].image, anchor = W)
    
def drawGameStatus():
    global hearts
    for i in range(len(hearts)):
        s.delete(hearts[i])
    for i in range(lives):
        x = s.create_image(90 + 25 *i, 150, image=liveHeart, anchor = W)
        hearts.append(x)

##    if lives == 0:
##        failscreen()
        
def drawShoppingList():
    global item1, item2
    s.delete(item1, item2)
    if len(shoppingList) >= 2:
        item1 = s.create_image(90, 280, image=shoppingList[1].image, anchor = W)
        item2 = s.create_image(90, 380, image=shoppingList[0].image, anchor = W)
    elif len(shoppingList) == 1:
        item2 = s.create_image(90, 380, image=shoppingList[0].image, anchor = W)
    else:
        successScreen()
    
def drawCharacter():
    global xCharacter, yCharacter, characterWidth, character

    character = s.create_image( xCharacter, yCharacter, image=characterImg, anchor=W)
    print(xStack, topOfStack)

def drawFood(): 
    global foodList, wrongImg, marking
    for i in range(len(foodList)):
        foodList[i].drawFood(s)

def deleteFood():
    global foodList
    for i in range(len(foodList)):
        foodList[i].removeFood(s)

def updateCharacter():
    global xCharacter, characterSpeed, xStack
    
    xCharacter = xCharacter + characterSpeed
    xStack = xCharacter

def updateFood():
    global foodList, foodSpeed, characterSpeed

    for i in range(len(foodList)):

        #when it is caught
        #if ValidateCatch(foodList[i]) == True and foodList[i].caughtTheFood(xStack, stackWidth, topOfStack) == True and foodList[i].alreadyCaught == True:
        if foodList[i].alreadyCaught == True: # and ValidateCatch(foodList[i]) == True:
            foodList[i].x1 += characterSpeed
            #when the catch is the right one
            #if foodList[i].valid == True:
            #    foodList[i].x1 += characterSpeed
            #else:
            #    foodList[i].y += foodSpeed
            
        #when it isn't even caught yet    
        else:
            foodList[i].y += foodSpeed

        # We also want to check here if the food has fallen below the bottom of the screen
        # if it has then we want to delete the food.
        # we can do this by actually removing the food
        # or just set a flag in the object to say it below and we no longer care

#checks if the thing i caught it the next item on the shopping list
def ValidateCatch(caughtFood):
  #HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # check here if the list is not empty.
    if len(shoppingList) > 0:
        wantedFood = shoppingList[0]
        if wantedFood.image == caughtFood.image:
            return True
        else:
            return False
    else:
        return False
def foodOnStack(): 
    global topOfStack, stackWidth, xStack, foodList, shoppingList, lives, item1, item2
    for i in range(len(foodList)):
        #If the food is above the stack
        #HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if foodList[i].caughtTheFood(xStack, stackWidth, topOfStack) == True and foodList[i].triedCatch == False:
            #HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            foodList[i].triedCatch = True
            #if I caught the right thing
            if ValidateCatch(foodList[i]) == True:
                foodList[i].y = topOfStack - 0.5 * foodList[i].height
                foodList[i].speed = 0
                foodList[i].alreadyCaught = True
                foodList[i].valid = True
                stackWidth = foodList[i].width
                xStack = foodList[i].x1
                topOfStack -= foodList[i].height - 10
                shoppingList.remove(shoppingList[0])
            #if I caught the wrong thing
            else:
                lives -= 1 #this decreases really quickly because I DIDN"T CATCH THAT THING  AND IT THINKS I DID!!!!!

###### Screens #####

######

def runGame():
    setInitialValues()
    fillShoppingList()
    drawBackground()
    f = 0
    while True:
        #so that not a bunch of food load and crowd the screen, just load every so often
        if f % 50 == 0:
            loadFood()
        f += 1
        
        drawShoppingList()
        drawGameStatus()
        updateFood()
        updateCharacter()
        drawFood()
        drawCharacter()
        foodOnStack()

        s.update()
        sleep(0.03)
        s.delete(character)
        deleteFood()

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
        
def keyDownHandler( event ):
    global characterSpeed  #because we'll be changing these values in this procedure
    
    if event.keysym == "Left":     #LEFT ARROW WAS PRESSED
        characterSpeed = -5  #sets the xSpeed to a negative value so that the ball will move to the left
        
    elif event.keysym == "Right":  #RIGHT ARROW WAS PRESSED
        characterSpeed = 5

    elif event.keysym == "q":
        quitScreen()



#At the bottom
root.after( 5, runGame )
##s.bind( "<Button-1>", mouseClickHandler )  #will need this for button clicking
s.bind( "<Key>", keyDownHandler )
s.bind( "<KeyRelease>", keyUpHandler)
s.pack()
s.focus_set()
root.mainloop()

