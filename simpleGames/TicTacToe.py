#tic-tac-toe
import numpy as np

count = 0

def selectPlayer():
    firstPlayer = input('Select between x or o:')
    if firstPlayer != "x" and firstPlayer != "o":
        print("Pleae select the right symbol")
        firstPlayer = selectPlayer()
    return firstPlayer

def printTic(tic):
    for ii in tic:
        temp = '|'
        for jj in ii:
            if jj == 0:
                temp += ' '
            else:
                temp += jj
            temp += '|'
        print(temp)    

def recall():
    tac = input("Play again yes or no: ")   
    if tac == "yes":
        return 1
    else:
        return 0

def tic_tac_toe():
    global count
    firstPlayer = selectPlayer()
    if firstPlayer == 'x':
        secondPlayer = 'o'
    else:
        secondPlayer = 'x'
    chance = True
    tic = np.zeros((3,3)).tolist()
    for ii in range(8):
        def indexing(tic):
            # taking index input from user and validating the input index
            ind = input('enter the index:')
            xInd,yInd = int(ind[1]),int(ind[3])
            if tic[xInd][yInd] != 0:
                print("Please select the empty index")
                xInd,yInd = indexing(tic)
            return xInd,yInd
            
        xInd,yInd = indexing(tic)
        
        if chance:
            player = firstPlayer
            
        else:
            player = secondPlayer
        chance = not chance
        
        tic[xInd][yInd] = player
        printTic(tic)
        
        if ii>=4:     
            if tic[xInd][0]==tic[xInd][1]==tic[xInd][2] or tic[0][yInd]==tic[1][yInd]==tic[2][yInd] or tic[0][0]==tic[1][1]==tic[2][2]or tic[2][0]==tic[1][1]==tic[0][2]:
                print(player, " is winner")
                if ii%2:
                    count -= 1
                else:
                    count += 1
                    
                if recall():
                    tic_tac_toe()
                else:
                    break
                            
            elif ii == 8:
                print("Match Draw!!!")
                if recall():
                    tic_tac_toe()
                else:
                    break
        
game = tic_tac_toe()

print('Game Over')
if count > 0:
    print("First player is winner!!")
elif count < 0:
    print("Second player is winner!!")
else:
    print("Match Draw!!")


    
