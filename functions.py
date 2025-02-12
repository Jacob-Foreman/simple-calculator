import math
"""
Author-Jacob Foreman

Date- 1/25/25

Description- All the functions that are used to calculate data and add interactability with the GUI

Idea: All buttons only add to the label's text. Unless return key or '=' button pressed, no calculation takes place

Once those are pressed however that string gets recursively broken down into its mappings and returns its solution.


"""

def clearEntry(ui_instance):
    #We can substring the curr label by ' ' char and then remove the last entry and set label to that
    current_text = ui_instance.calc_io_label.cget("text")
    if current_text:
       new_text = current_text[:-1]
    else:
        new_text = ""
    ui_instance.calc_io_label.config(text=new_text)
    


def clearAll(ui_instance):
    #we clear the text in the label effectively wiping the entry before calculations
    ui_instance.calc_io_label.config(text="0")
    


def fractional(ui_instance,expression):
    #We divide 1 by the current expression in the calc.
    if expression == '' or expression =='0':
        ui_instance.calc_io_label.config(text="Cannot divide by zero")
        return
    ans = 1.0/ float(textDeparser(ui_instance,expression))
    ui_instance.calc_io_label.config(text=str(ans))

    return

def squared(ui_instance,expression):
    #solve the expression and multiply it by itself
    if expression == '' or expression =='0':
        ui_instance.calc_io_label.config(text="0")
        return
    ans = float(textDeparser(ui_instance,expression)) 

    ui_instance.calc_io_label.config(text=str(ans*ans))
    return

def squareRoot(ui_instance,expression):
    if expression == '' or expression =='0':
        ui_instance.calc_io_label.config(text="0")
        return
    ans = math.sqrt(float(textDeparser(ui_instance,expression)))
    ui_instance.calc_io_label.config(text=str(ans))
    return


def addSymbol(ui_instance,symbol):
    current_text = ui_instance.calc_io_label.cget("text")
    if current_text == "0":
        new_text = symbol
    else:
        new_text = current_text + symbol
    ui_instance.calc_io_label.config(text = new_text)

def appendDigit(ui_instance,digit):
    current_text = ui_instance.calc_io_label.cget("text")
    if current_text == "0":
        new_text = str(digit)
    else:
        new_text = current_text + str(digit)
    ui_instance.calc_io_label.config(text=new_text)
    


def signSwitch():
    #Must be entered before a number to ensure a difference in signs
    return


def equals(ui_instance,expression):
    #here we want to call our solution provider. This will parse through our equation we made and recursively break down the equations we pass to the smallest operations.
    #they will perform the operations then return a numerical answer which will be then be a part of the larger solution.
    ui_instance.calc_io_label.config(text=textDeparser(ui_instance,expression))
    return

#This is the solver
'''
    At the very base case we have a pair of parenthesis. If there is no pair then we infer left to right with respect to operation heirarchy
    If opening parenthesis is found, we iterate through and add to substring until either a new open parenthesis is found or we find the closing parenthesis. 
    Nested parenthesis should be solved inner out. Utilize a stack to manage nesting conditions
'''
#recursively called
#Params- ui instance for error handling , String Expression
#Returns- Digit value or throws error
def textDeparser(ui_instance, expression):
    # Check for valid pairs of parentheses
    if not pairCheck(expression):  # Invalid pair
        ui_instance.calc_io_label.config(text="Incorrect number of Parentheses")
        return

    ans = expression  # Copy of expression to manipulate
    parenthesisCounter = 0
    startIndex = -1
    currSegment = ''
    i = 0

    while i < len(ans):
        char = ans[i]

        if char == '(':
            if parenthesisCounter == 0:  # Start of a new parenthesis segment
                startIndex = i
                currSegment = ''  # Reset segment
            parenthesisCounter += 1
        elif char == ')':
            parenthesisCounter -= 1
            if parenthesisCounter == 0:  # Found matching closing parenthesis
                # Solve the inner expression recursively
                result = textDeparser(ui_instance, currSegment)
                # Replace the full (expression) with its computed value
                ans = ans[:startIndex] + result + ans[i + 1:]
                # Reset and restart parsing
                i = startIndex - 1  # Go back and reprocess from startIndex
                parenthesisCounter = 0
        else:
            if parenthesisCounter > 0:
                currSegment += char  # Store characters inside the current parenthesis

        i += 1

    # solve multiplication, division, addition, and subtraction left to right
    operators = ['x', '/', '+', '-']
    for op in operators:
        while op in ans:
            tempList = findLeftAndRight(ans, op)
            ans = ans.replace(tempList[0], tempList[1], 1)

    return ans


def solve(leftNum,rightNum,symbol):
    leftDigit = float(leftNum)
    rightDigit = float(rightNum)

    if symbol == '/':
        return str(leftDigit / rightDigit)
    elif symbol == 'x':
        return str(leftDigit * rightDigit)
    elif symbol == '+':
        return str(leftDigit + rightDigit)
    elif symbol == '-':
        return str(leftDigit - rightDigit)

 

#Params- 
# Expression- The string expression we are evaluating
# symbol - The symbol we are evaluating against
# Returns - A touple containing the extracted string expression and the solved answer to the epxression
def findLeftAndRight(expression,symbol):
    ans = ''
    tempSubStrings = expression.split(symbol,1)#splits into list of two elements. element 0 is left of match, element 1 is right of match
    leftPart = tempSubStrings[0]
    rightPart = tempSubStrings[1]

    tempLeftString =''
    for i in range(len(leftPart)-1,-1,-1):
        char = leftPart[i]
        if char.isdigit() or char == '.':
            tempLeftString = char + tempLeftString
        else:
            break


    tempRightString = ''
    for currIndex, char in enumerate(rightPart):
        if char.isdigit() or char == '.':
            tempRightString += char
        else:
            break
            

    return tempLeftString + symbol + tempRightString, solve(tempLeftString,tempRightString,symbol)


def pairCheck(expression):
    currCount = 0
    for char in expression:
        if char == '(':
            currCount += 1
        if char == ')':
            currCount -= 1
            
    if currCount == 0:
        return True
    else:
        return False

def on_key_press(event,TLabel):
    #here we want to add keyboard equivalents for fast keyboard support
    print(event.char, event.keysym,event.keycode)

    return
