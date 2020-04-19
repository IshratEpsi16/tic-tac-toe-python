#----------------
#Tic_Tac_Toe_Game
#----------------

#First we define a dictionary which have keys & Values
board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}
    
player=1            #initialize first player
moves_count=0       #total moves count(1-9)
end_check=0         #check if any 3 row,column or diagonal are matching or not

#checking the cells
def check():
#This checking is for Player 1
#horizontal check
    if board['1']=='X' and board['2']=='X' and board['3']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
    if board['4']=='X' and board['5']=='X' and board['6']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
    if board['7']=='X' and board['8']=='X' and board['9']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1

#vertical check
    if board['1']=='X' and board['4']=='X' and board['7']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
    if board['2']=='X' and board['5']=='X' and board['8']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
    if board['3']=='X' and board['6']=='X' and board['9']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
#diagonal check
    if board['1']=='X' and board['5']=='X' and board['9']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1
    if board['3']=='X' and board['5']=='X' and board['7']=='X':
        print('Congratulations!! Player 1 has won the game ')
        return 1


#This checking is for Player 2
#horizontal check
    if board['1']=='X' and board['2']=='X' and board['3']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    if board['4']=='X' and board['5']=='X' and board['6']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    if board['7']=='X' and board['8']=='X' and board['9']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1

#vertical check
    if board['1']=='X' and board['4']=='X' and board['7']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    if board['2']=='X' and board['5']=='X' and board['8']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    if board['3']=='X' and board['6']=='X' and board['9']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
#diagonal check
    if board['1']=='X' and board['5']=='X' and board['9']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    if board['3']=='X' and board['5']=='X' and board['7']=='X':
        print('Congratulations!! Player 2 has won the game ')
        return 1
    return 0

#Demo of game output
print('    ')
print('Choose your input(1-9) :')
print("Player 1 will always be 'X' & Player 2 will always be 'O' :")
print('   |   | ')
print(' 1 | 2 | 3')
print('   |   | ')
print('---*---*---')
print('   |   | ')
print(' 4 | 5 | 6')
print('   |   | ')
print('---*---*---')
print('   |   | ')
print(' 7 | 8 | 9')
print('   |   | ')
print('**************************')

while True:
    print('   |   |')
    print('  '+board['1'] +'| '+ board['2'] +' | '+ board['3'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  '+board['4'] +'| '+ board['5'] +' | '+ board['6'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  '+board['7'] +'| '+ board['8'] +' | '+ board['9'])
    print('   |   |')
   
    end_check = check()
    if moves_count == 9 or end_check == 1:      #if total moves are 9 or any 3 row,column,diagonal matches the game is over
        break 
    #player One's input
    while True:
        if player == 1:
            
            p1_input = input('Player 1 : ')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()]='X'        #player one is X
                player = 2
                break
            else:
                print("Wrong input,your input should be 1,2... : ")
                continue
        
    #player two's input
        else:
             
             p2_input = input('Player 2: ')
             if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()]='O'        #player one is O
                player = 1
                break
             else:
                 print('Wrong input,your input should be 1,2... : ')
                 continue

    #increment moves
    moves_count=moves_count+1
print("Thanks for playing the game")










