area = ['   ', '   ', '   ']
p1_line,p1_column,p2_line,p2_column = '','','',''


def start():
    #Prints game area
    trigger = True
    t = 1
    for _ in area:
        if trigger: print('  1 2 3'); trigger = False
        print(f'{t} {_[0]}|{_[1]}|{_[2]}')
        t += 1
        if t <= 3: print('  -+-+-')
    print('\n')


def player(x):
    
    def input_player(x):
        #Condition for Player 1('X') or Player 2('0')
        if x == 'p1': p_type = 'X'
        else: p_type = '0'
        print(f'{p_type} to play:')
        
        #Prompts player for 'LINE' input and checks if valid / if not prompts again
        line = input('Line: ')
        while line not in (str(1),str(2),str(3)):
            print(f'\nOnly 1, 2 or 3 allowed, try again!\n\n{p_type} to play:')
            line = input('Line: ')
        #Saves player's 'LINE' input in var (x)_line
        globals()[f'{x}_line'] = int(line)
        
        #Prompts player for 'COLUMN' input and checks if valid / if not prompts again
        column = input('Column: ')
        while column not in (str(1),str(2),str(3)):
            print(f'\nOnly 1, 2 or 3 allowed, try again!\n\n{p_type} to play:')
            column = input('Column: ')
        #Saves player's 'COLUMN' input in var (x)_column
        globals()[f'{x}_column'] = int(column)
    

    def indexing(x):
        global area
        #Condition for Player 1('X') or Player 2('0')
        if x == 'p1': p_type = 'X'
        else: p_type = '0'
        #Breaks string at player's inputs-1, adds 'X'/'0' and rejoins string
        area[globals()[f'{x}_line']-1] = area[globals()[f'{x}_line']-1][:globals()[f'{x}_column']-1] \
                                       + p_type \
                                       + area[globals()[f'{x}_line']-1][globals()[f'{x}_column']:]
        start()
    
    
    input_player(x)
    #Checks if player's input location is already used or not
    while area[globals()[f'{x}_line']-1][globals()[f'{x}_column']-1] != ' ':
        print('-'*28 + '\n' 'This space was already used!\n' + '-'*28)
        input_player(x)
    else:
        indexing(x)


def won():
    global area
    	#Checks if there are 3 'X' in the same row'''
    if ((area[0][0]=='X' and area[0][1]=='X' and area[0][2]=='X') or
        (area[1][0]=='X' and area[1][1]=='X' and area[1][2]=='X') or
        (area[2][0]=='X' and area[2][1]=='X' and area[2][2]=='X') or
            #Checks if there are 3 'X' in the same column
        (area[0][0]=='X' and area[1][0]=='X' and area[2][0]=='X') or
        (area[0][1]=='X' and area[1][1]=='X' and area[2][1]=='X') or
        (area[0][2]=='X' and area[1][2]=='X' and area[2][2]=='X') or
                #Checks if there are 3 'X' in the same diagonal
        (area[0][0]=='X' and area[1][1]=='X' and area[2][2]=='X') or
        (area[0][2]=='X' and area[1][1]=='X' and area[2][0]=='X') or
            
        #Checks if there are 3 '0' in the same row
        (area[0][0]=='0' and area[0][1]=='0' and area[0][2]=='0') or
        (area[1][0]=='0' and area[1][1]=='0' and area[1][2]=='0') or
        (area[2][0]=='0' and area[2][1]=='0' and area[2][2]=='0') or
            #Checks if there are 3 '0' in the same column
        (area[0][0]=='0' and area[1][0]=='0' and area[2][0]=='0') or
        (area[0][1]=='0' and area[1][1]=='0' and area[2][1]=='0') or
        (area[0][2]=='0' and area[1][2]=='0' and area[2][2]=='0') or
                #Checks if there are 3 '0' in the same diagonal
        (area[0][0]=='0' and area[1][1]=='0' and area[2][2]=='0') or
        (area[0][2]=='0' and area[1][1]=='0' and area[2][0]=='0')):
        return 'A'

    #Checks if there are any free spaces left, if not displays STALEMATE
    if ' ' not in area[0] and ' ' not in area[1] and ' ' not in area[2]:
        return 'B'


def run_game():
    global area,p1_line,p1_column,p2_line,p2_column
    #Runs game and checks if any player won or if it's a stalemate
    trigger = False
    start()
    while trigger == False:
        if won() == 'A':
            print('-'*16 + '\n' '0 is the Winner!\n' + '-'*16)
            break
        elif won() == 'B':    
            print('-'*17 + '\n' +'S T A L E M A T E\n' + '-'*17)
            break
        else:    
            player('p1')
            trigger = True
        while trigger == True:
            if won() == 'A':
                print('-'*16 + '\n' 'X is the Winner!\n' + '-'*16)
                break
            elif won() == 'B':    
                print('-'*17 + '\n' +'S T A L E M A T E\n' + '-'*17)
                break
            else:    
                player('p2')
                trigger = False
                break
    
    #Ask user if they want to play again and reset game, else do nothing
    temp = input('Play again?\nY (yes) / N (no)\n')
    if temp.upper() == 'Y':
        area = ['   ', '   ', '   ']
        p1_line,p1_column,p2_line,p2_column = '','','',''
        run_game()


run_game()
