from graphics import *
from SudokuGrids import *
from random import randint

win = GraphWin("Sudoku",450,320)
win.setBackground("white")
DictBoxes = {} 
boxNum = 1
#function to draw the boxes
def drawInputBoxes(first,second, x, y, w, rowNum, grid):
  inputBox = []
  global boxNum
  for num in range(first, second):
      inputBox.append(Entry(Point(x,y), w))
      if num%3 == 0:
        x += 24
      x = x + 40
  for box in inputBox:
    DictBoxes[boxNum] = box
    boxNum +=1
    box.draw(win)
    box.setFill("white")
    if grid[rowNum][inputBox.index(box)] != 0:
        box.setText(grid[rowNum][inputBox.index(box)])
        box.setTextColor("black") 

def rectangle():
  rect = Rectangle(Point(7, 33), Point(442, 247))
  rect.draw(win)
  rect.setFill("black")

def Setboard(grid): 
  row = 1
  col = 10
  x = 40
  w = 5
  y = 30
  no_row = 0
  rows1 = [drawInputBoxes(row, col, x, y + 20*(i+1), w, no_row+i, grid) for i in range(3)]

  y = 100
  no_row = 3
  rows2 = [drawInputBoxes(row, col, x, y + 20*(i+1), w, no_row+i, grid) for i in range(3)]

  y = 170
  no_row = 6
  rows3 = [drawInputBoxes(row, col, x, y + 20*(i+1), w, no_row+i, grid) for i in range(3)]
 
  rows = rows1 + rows2+ rows3

  rectangle()

  return rows

#def inside(point,rectangle) sourced from https://stackoverflow.com/questions/39867464/adding-button-to-python-graphics-py-window
def inside(point, rectangle):
    ll = rectangle.getP1()
    ur = rectangle.getP2()

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def check(finishedgrid):
  checkButton = Rectangle(Point(330, 260), Point(389, 290))
  checkButton.setFill("green")
  checkButton.draw(win)
  text = Text(Point(357, 275), "Check")
  text.draw(win)

  while True:
    clickPoint = win.getMouse()
    if clickPoint is None:
      text.setText("")  

    elif inside(clickPoint, checkButton):
      UserGuess = []
      for box in DictBoxes.values():
        if box.getText().isdigit():
          UserGuess.append(int(box.getText())) #set up a list of all the values the user entered
      Answer = [item for sublist in finishedgrid for item in sublist] #create a flat list of all the correct values
      if UserGuess == Answer:
        print("Your Guess is correct!")
        break
      else:
        print("Sorry, something's not right :(")
        response = input("Would you like to see the correct answer?(Y/N): ")
        if response == 'Y':
          GiveAnswer(finishedgrid) #show user correct board
          break
        elif response == 'N':
          print('Ok, keep working on it!')
          check(finishedgrid) #let user keep working and then check their answer again
          break 

def GiveAnswer(finishedgrid):
  Setboard(finishedgrid)

def main():
  print("Welcome to our sudoku game! To play, fill in missing values so that each row on the grid and 3*3 area has includes each number 1-9 exactly once")
  playagain = 'Y'
  #BoardNum = randint(0,len(TupleofGrids)-1)
  while playagain == 'Y':
    BoardNum = randint(0,len(TupleofGrids)-1) #choose random sudoku board to give user
    finishedgrid = TupleofGrids[BoardNum][0] 
    gridtosolve = TupleofGrids[BoardNum][1]
    Setboard(gridtosolve) #set up the board with values missing for the player to fill in
    check(finishedgrid)
    playagain = input("Would you like to play again? (Y/N): ") #allow user to play again
  win.close() #close the window when player is done
  
if __name__ == "__main__":
  main()