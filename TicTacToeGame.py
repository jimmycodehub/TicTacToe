#c13707355 James McGovern
print("Tic Tac Toe!!")
#printing out the games grid and adding the 2d list to it
def printGame(grid):
    print("\n          1   2   3   4   5   6  ")
    print("        +-----------------------+")
    for row in range(6):
        print("     ",row+1, "|", grid[row][0],"|", grid[row][1],"|", grid[row][2],"|"
              , grid[row][3],"|", grid[row][4],"|", grid[row][5], "|")
        if((row+1) % 6 !=0):
                print("        |---+---+---+---+---+---|")
        elif((row+1) % 6 ==0):
            print("        +-----------------------+\n")

#this method appends the 2d list to underscores to show an empty grid
def emptyGrid():
    grid = []
    #I then appended the 2d List to be larger then the game grid
    #so that I could check all the diagonals in the game without getting out of space errors
    for i in range(10):
        grid.append(["_"] * 10)
    return grid


#this method takes in the current grid and player and then checks if that player is a winner
def checkWin(grid, player):
    if(player ==1):
        move = "X"
    elif(player ==2):
        move="O"
    elif(player ==3):
        move="%"
    result = 2

    for row in range(6):
        for col in range(6):
            #vertical wins
            if((grid[row][col] == move) and (grid[row+1][col] == move) and (grid[row+2][col]==move)):
                result = 1
            #horizontal wins
            if((grid[row][col]==move) and (grid[row][col+1]==move) and (grid[row][col+2]==move)):
                result = 1
            #diagonal right wins
            if((grid[row][col]==move) and (grid[row+1][col+1]==move) and (grid[row+2][col+2]==move)):
                result = 1
            #diagonal left wins
            if((grid[row][col]==move) and (grid[row+1][col-1]==move) and (grid[row+2][col-2]==move)):
                result = 1
    return result

#this method checks if the grid is full and there are no more moves to make 
def fullGrid(grid):
    full = 2

    counter = 0
    for row in range(6):
        for col in range(6):
            if(grid[row][col] == "_"):
                counter = counter+1
    if(counter ==0):
        full =1
    return full

def nextPlayer(player):
    if(player==1):
        nextPlayer = 2
    if(player==2):
        nextPlayer = 3
    if(player==3):
        nextPlayer = 1
    return nextPlayer

#3player game will begin ere until there is a winner or draw
def playGame(player):
    name = ""
    grid = []
    grid = emptyGrid()
    inGame = 1
    while(inGame != 0):
        if(player ==1):
            move = "X"
            name = p1
        elif(player ==2):
            move="O"
            name = p2
        elif(player ==3):
            move="%"
            name = p3
        print("\nIt's your turn !", name)
        print("Here is the grid. You are ", move)
        printGame(grid)

        while True:
            try:
                row = int(input("Enter row: ")) -1
                col = int(input("Enter col: ")) -1
                if((row>5 or row<0)
                   or (col>5 or col<0)):
                    print("ERROR: The number must be between 1 and 6")
                elif(grid[row][col] != "_"):
                    print("ERROR: This location has already been picked! Pick another location")
                else:
                    break
            except ValueError:
                print("Error: Invalid Entry!, You must enter a number")

        grid[row][col] = move
        wins = checkWin(grid, player)
        if(wins == 1):
            print("Game Over: ", name," Wins!")
            print("Here is the winning grid:")
            printGame(grid)
            inGame = 0
            break
        full = fullGrid(grid)
        if(full == 1):
            print("Game Over: Draw! Heres the table")
            printGame(grid)
            inGame = 0
            break
        player = nextPlayer(player)

#This is the beginning of the assignment that takes in the players names and gives an option of playing    
endGame = False;
while(endGame != True):
    play = input("Welcome to Tic Tac Toe, Do you wish to play(y/n)?: ")
    if(play =="y"):
        print("\nWelcome to TicTacToe")
        p1 = input("\nPlayer one enter your name?: ")
        p2 = input("\nPlayer two name?: ")
        p3 = input("\nPlayer three name?: ")
        print("\Hello "+ p1 + " youe are X, hello " + p2 + " you are O and hello "+ p3 +" you are % !")
        playGame(1)
    elif(play=="n"):
        print("GoodBye")
        endGame = True
    else:
        print("Invalid entry!")
