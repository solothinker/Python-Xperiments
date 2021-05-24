#tic-tac-toe
import numpy as np


def printTic(tic):
    for ii in tic:
        temp = ''
        for jj in ii:
            if jj == 0:
                temp += ' '
            else:
                temp += jj
            temp += '|'
        print(temp)    
tic = np.zeros((3,3)).tolist()
##tic[0][0] = 'o'
##tic[1][1] = 'x'
##tic[2][2] = 'o'
##printTic(tic)
firstPlayer = input('Select between x or o:')
if firstPlayer == 'x':
    secondPlayer = 'o'
else:
    secondPlayer = 'x'

chance = True
for ii in range(3):    
    ind = input('enter the index:')
    xInd,yInd = int(ind[1]),int(ind[3])

    if chance:
        player = firstPlayer
        
    else:
        player = secondPlayer
    chance = not chance
    
    tic[xInd][yInd] = player
    printTic(tic)
