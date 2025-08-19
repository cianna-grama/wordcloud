# Cianna Grama
# Programming Assignment 4
# Intro CS
# wordcloud.py

# program to create a wordcloud from a given text file

from graphics import *
from random import *
from time import *

################################## BUTTON CLASS ##################################
class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        # sets w equal to the width/2 and sets h equal to the height/2
        w,h = width/2.0, height/2.0

        # sets x equal to the x value of the given center point, sets y equal to the y value of the given center point
        x,y = center.getX(), center.getY()
        
        # sets self.xmax equal to the x value of the center plus the width/2, and sets self.xmin equal to the x-value of the center minus the width/2
        self.xmax, self.xmin = x+w, x-w

        # sets self.ymax equal to the y value of the center plus the height/2, and sets self.ymin equal to the y-value of the center minus the height/2
        self.ymax, self.ymin = y+h, y-h

        # sets p1 equal to a point at the points of the minimum x value and the minimum y value (aka the bottom left corner of the button)
        p1 = Point(self.xmin, self.ymin)

        # sets p2 equal to a point at the points of the maximum x value and the maximum y value (aka the top right corner of the button)
        p2 = Point(self.xmax, self.ymax)

        # sets <name of the button>.rect equal to a rectangle created with the given center, height, and width
        self.rect = Rectangle(p1,p2)

        # sets the color of the rectangle of the <name of the button> to light gray
        self.rect.setFill('lightgray')

        # draws the <name of the button> rectangle in the GUI window
        self.rect.draw(win)

        # creates the label of <name of the button> based on the given center and label, sets that equal to <name of the button>.label
        self.label = Text(center, label)

        # draws the <name of the button> label in the GUI
        self.label.draw(win)

        # calls to another method in the class
        self.activate() # Start off all buttons as active. This is how to call another method in this class

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') # color the text "black"
        self.rect.setWidth(2)       # set the outline to look bolder
        self.active = True          # set the boolean instance variable that tracks "active"-ness to True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgray") ## color the text "darkgray"
        self.rect.setWidth(1) ## set the outline to look finer/thinner
        self.active = False ## set the boolean instance variable that tracks "active"-ness to False

    def isClicked(self, pt):
        """Returns true if button is active and Point pt is inside"""
        if self.active == True and (self.xmin <= pt.getX() <= self.xmax and self.ymin <= pt.getY() <= self.ymax):
            return True
        else:
            return False

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()


################################## WINDOW CLASS ##################################

# object to create a gui window - use to call win in other functions within the same GUI and without creating a new one
class gui:
    
    # create gui
    win = GraphWin("Word Cloud", 600, 600)
    win.setCoords(0, 0, 100, 100)


################################## MAIN SCREEN CREATION ##################################

def mainscreen():
    gui.win.setBackground("LightBlue1")

    # create title and draw
    titleText = Text(Point(50, 90), "Word Cloud")
    titleText.setSize(60)
    titleText.setTextColor("blue2")
    titleText.draw(gui.win)

    # create buttons and draw
    makeCloudButton = Button(gui.win, Point(75, 65), 20, 10, "Create Word Cloud")
    exitButton = Button(gui.win, Point(50, 5), 15, 8, "Exit")

    # create instructions for entry boxes and draw
    txtfileInstructions = Text(Point(20, 75), "Enter the name of the txt file:")
    txtfileInstructions.draw(gui.win)
    
    wordAmInstructions = Text(Point(20, 60), "Enter the amount of words:\n(10 - 40 for best results)")
    wordAmInstructions.draw(gui.win)

    # create entry boxes and draw
    txtfileEntry = Entry(Point(20, 70), 20)
    txtfileEntry.setText("jobdescription.txt")
    txtfileEntry.draw(gui.win)

    wordAmEntry = Entry(Point(20, 55), 20)
    wordAmEntry.setText("20")
    wordAmEntry.draw(gui.win)

    # return the values of the drawn objects so they can be changed if neccessary
    return titleText, makeCloudButton, exitButton, txtfileInstructions, wordAmInstructions, txtfileEntry, wordAmEntry


################################## CLEAN UP TEXT FILE FUNCTION ##################################

# function to make file lowercase, remove punctuation, and remove filler words
def simplifyFile(file):

    # convert file to lowercase
    file = file.lower()

    # remove punctuation
    for character in "!\"#$%&()*+,-'./:;<=>?@'[\\]’_•":
        file = file.replace(character, "")

    # remove numbers
    for num in range(10):
        file = file.replace(str(num), "")

    # input stop words file, read, and lower stop words
    stopWords = open("stopwords.txt", "r").read().lower()

    # split stop words by commas
    stopWords = stopWords.split(",")

    # add spaces between both sides of the stopwords so letters are not taken out of words
    for i in range(len(stopWords)):
        stopWords[i] = stopWords[i] + " "

    # remove stop words
    for word in stopWords:
        file = file.replace(word, " ")

    return file


################################## RETURN WORD PAIR NUMBER ##################################

# program to return the number from the word pair
def frequencySort(wordpair):
    
    return wordpair[1]


################################## FREQUENCY COUNTER ##################################

def frequencyCounter(fileToCount, WordAmInput):

    # split words from text file by words to create a list
    words = fileToCount.split()

    # create counts dictionary to hold how often each word occurs
    counts = {}

    # for each word in the split words list
    for w in words:

        # add each word in counts the dictionary
        # add the words as a new key in the dictionary if it is not in the dictionary
        # if the word is in the dictionary already, add one count to it
        counts[w] = counts.get(w, 0) + 1

    # return the dictionary of words and their frequencies to the main program
    return counts

        
################################## FREQUENCY SORTER ##################################

def frequencySorter(dictionary, WordAmInput):
    
# creating list of top _ words

    # get list of key-value pairs (using items method)
    itemslist = list(dictionary.items())

    # sort items in list by alphabet
    itemslist.sort()

    # sort list items according to frequency using frequency function (returns the number value from the list)
    itemslist.sort(key = frequencySort, reverse = True) # reverse sorts list in reverse order(highest count to lowest)

    # get the amout of words desired for the word cloud
    givenWordAm = int(WordAmInput.getText())

    # create an empty list for the top words
    frequentItems = []
    
    # store list with report of given most frequent words and the corresponding number
    for i in range(givenWordAm):
        frequentItems.append(itemslist[i])

    # convert the most frequent words and their values (in order of freqeuncy) to a string
    frequentItems = str(frequentItems)

    # split the most frequent words and their values by in order to single out each word"'"
    frequentItems = frequentItems.split("'")

    # create new list for the top frequent words only
    frequentWords = []

    # add words only from the split list of the top most frequent words and their values
    for i in range(1, len(frequentItems), 2):
        frequentWords.append(frequentItems[i])

    # return the list of the most frequent words only (in order) and not their values
    return frequentWords


################################## CLEAR SCREEN FUNCTION ##################################

def clearScreen(win, a, b, c, d, e, f):

    # change background to white
    win.setBackground("white")

    # add each parameter to a list
    objectsOnScreen = [a, b, c, d, e, f]

    # undraw each object
    for thing in objectsOnScreen:
        thing.undraw()


################################## RANDOM COORDS AND RECTANGLE FUNCTION ##################################

def randomPoint(rectHeight, rectWidth):
        # set a random x and y value between the specified points
        randX = randrange(25, 75)
        randY = randrange(20, 90)

        # create a variable for the randomly generated point
        point = Point(randX, randY)
        
        # find the coordinates of the rectangle based on the random points
        p1x = randX - (rectWidth / 2)
        p1y = randY - (rectHeight / 2)
        p2x = randX + (rectWidth / 2)
        p2y = randY + (rectHeight / 2)

        wordRect = Rectangle(Point(p1x, p1y), Point(p2x, p2y))

        return point, wordRect


################################## CHECKS OVERLAP FUNCTION ##################################

def checkOverlap(wordRect, rect):

    # finds the coordinates of the new rectangle 
    R1p1x = wordRect.getP1().getX()
    R1p1y = wordRect.getP1().getY()
    R1p2x = wordRect.getP2().getX()
    R1p2y = wordRect.getP2().getY()

    # find the coordinates of the rectangle in the rectangle list
    R2p1x = rect.getP1().getX()
    R2p1y = rect.getP1().getY()
    R2p2x = rect.getP2().getX()
    R2p2y = rect.getP2().getY()

    # if the x coordinates of the new rectangle are between the x coordinates of the rectangle from the rectangle list and
    # if the y coordinates of the new rectangle are between the y coordinates of the rectangle from the rectangle list:
    if ((R2p1x <= R1p2x <= R2p2x) and (R2p1y <= R1p2y <= R2p2y)) or ((R2p1x <= R1p1x <= R2p2x) and (R2p1y <= R1p1y <= R2p2y)):

        return True

    # if the coordinates do not overlap
    return False

    
################################## IS OVERLAP FUNCTION ##################################

def isOverlap(wordRect, rectangleList):

    # for each rectangle in the rectangle list
    for rect in rectangleList:

        # if new rect overlaps with item in list:
        if checkOverlap(wordRect, rect) == True:

            # return True to the function
            return True 

        # if does not overlap, run through the loop again

    # if none of the items return True, return False to the function
    return False
         

################################## WORD CLOUD DRAW FUNCTION ##################################

def wordCloudDraw(wordAmEntry, topWordsList):

    # get the amount of words that the user inputted and make it an integer
    amOfWords = int(wordAmEntry.getText())

    # create empty lists for used points and used rectangles
    pointsList = []
    rectangleList = []
    
    # run following code as many times as there are words:
    for i in range(int(amOfWords)):
        
        # set the word equal to the value in the list of top words
        word = topWordsList[i]

        # find the color of the word (random)
        r = randrange(1, 250)
        g = randrange(1, 250)
        b = randrange(1, 250)

        textColor = color_rgb(r, g, b)

        # set the size of the word based on the amount of words
        sizeSubtract = (60 - 10) / (amOfWords) * (i + 1)

        textSize = int(60 - sizeSubtract)

        # create the size of the rectangle for the word based on the text size and amount of letters
        rectHeight = int(textSize / len(word))
        rectWidth = int(rectHeight * (len(word) / 1.4))

        # create random point and rectangle around word to accompany point, return the point and the rectangle coordinates
        point, wordRect = randomPoint(rectHeight, rectWidth)

        # while isOverlap returns true (happens when the new rectangle coordinates overlap with the old rectangles from the rectangle list)
        if isOverlap(wordRect, rectangleList) == True:
             
            # create new random point plus rectangle
            point, wordRect = randomPoint(rectHeight, rectWidth)

        # when isOverlap is false:
        else:
            
            # add the rectangle to the rectangle list                                  
            rectangleList.append(wordRect)

        # create the word object
        wordtext = Text(point, word)
        
        # set the color of the text
        wordtext.setFill(textColor)

        # set the size of the rectangle
        wordtext.setSize(textSize)
        
        # draw the word in the window 
        wordtext.draw(gui.win)


################################## SIMPLIZED CREATE CLOUD FUNCTION ##################################

def createWordCloud(win, titleText, makeCloudButton, txtfileInstructions, wordAmInstructions, txtfileEntry, wordAmEntry):
    
    # get the file name from the gui 
    filenameinput = txtfileEntry.getText()

    # open and read the file
    textFile = open(filenameinput, "r").read()

    # simplify file for program and return the simplified file
    textFilemod = simplifyFile(textFile)

    # find the frequency of each word and store in a dictionary
    countdictionary = frequencyCounter(textFilemod, wordAmEntry)

    # find the top number of words (amount based on user input) and place them into a list in order of most to least frequent
    topWordsList = frequencySorter(countdictionary, wordAmEntry)
                      
    # clear the screen except exit button
    clearScreen(gui.win, titleText, makeCloudButton, txtfileInstructions, wordAmInstructions, txtfileEntry, wordAmEntry)
        
    # draw up the word cloud
    wordCloudDraw(wordAmEntry, topWordsList)


################################## MAIN FUNCTION ##################################

def main():

    # create the main screen and return neccessary values
    titleText, makeCloudButton, exitButton, txtfileInstructions, wordAmInstructions, txtfileEntry, wordAmEntry = mainscreen()
    
    # get a mouse click
    pt = gui.win.getMouse()

    # while the exit butoon is not pressed
    while not exitButton.isClicked(pt):

        # if the make cloud button is clicked:
        if makeCloudButton.isClicked(pt):

            # create the word cloud (see function above for specific details)
            createWordCloud(gui.win, titleText, makeCloudButton, txtfileInstructions, wordAmInstructions, txtfileEntry, wordAmEntry)

        # if the make cloud button is not clicked get another mouse click
        pt = gui.win.getMouse()

    # if the exit button is pressed, close the window  
    gui.win.close()
            
        
if __name__ == "__main__": 
    main()
        
    

    














        
