from __future__ import print_function

chs = []

for x in range (0, 9) :
    chs.append(str(x + 1))

playerOne_Turn = True
winner = False

def print_Board() :
    print( '\n -----')
    print( '|' + chs[0] + '|' + chs[1] + '|' + chs[2] + '|')
    print( ' -----')
    print( '|' + chs[3] + '|' + chs[4] + '|' + chs[5] + '|')
    print( ' -----')
    print( '|' + chs[6] + '|' + chs[7] + '|' + chs[8] + '|')
    print( ' -----\n')

while not winner :
    print_Board()
  
    if playerOne_Turn :
        print( "Player 1:")
    else :
        print( "Player 2:")
  
    try:
        ch = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if chs[ch - 1] == 'X' or chs [ch-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOne_Turn :
        chs[ch - 1] = 'X'
    else :
        chs[ch - 1] = 'O'

    playerOne_Turn = not playerOne_Turn

    for x in range (0, 3) :
        y = x * 3
        if (chs[y] == chs[(y + 1)] and chs[y] == chs[(y + 2)]) :
            winner = True
            print_Board()
        if (chs[x] == chs[(x + 3)] and chs[x] == chs[(x + 6)]) :
                winner = True
                print_Board()

    if((chs[0] == chs[4] and chs[0] == chs[8]) or
       (chs[2] == chs[4] and chs[4] == chs[6])) :
        winner = True
        print_Board()
print ("Player " + str(int(playerOne_Turn + 1)) + " wins!\n")
