import os       #for unicode characters and clear command
os.system("")

area = ['   ', '   ', '   ']
p1_line,p1_column,p2_line,p2_column = '','','',''
score_x = 0
score_0 = 0


def start():
    #Clears terminal window
    os.system('cls' if os.name == 'nt' else 'clear')
    #Prints game banner and area
    print(f"\n{' '*24}▀█▀ █ █▀▀ ▄▄ ▀█▀ ▄▀█ █▀▀ ▄▄ ▀█▀ █▀█ █▀▀")
    print(f"{' '*24}░█░ █ █▄▄ ░░ ░█░ █▀█ █▄▄ ░░ ░█░ █▄█ ██▄\n")
    print(f"{' '*16}Place your mark ('X' or '0') using the numbers 1, 2 or 3.")
    print(f"{' '*18}First player to get 3 marks in a row is the winner.")
    print(f"{' '*16}If all squares are full and no one has 3 marks in a row,")
    print(f"{' '*29}the game ends in a stalemate.")
    print(f"{' '*40}Enjoy!\n")
    print(f"{' '*18}Score X: {score_x}{' '*32}Score 0: {score_0}\n")
    trigger = True
    t = 1
    for _ in area:
        if trigger:
            print(f'{' '*39}  1 2 3')
            trigger = False
        print(f'{' '*39}{t} {_[0]}|{_[1]}|{_[2]}')
        t += 1
        if t <= 3:
            print(f'{' '*39}  -+-+-')
    print('\n')
    

def player(x):
    
    def input_player(x):
        #Condition for Player 1('X') or Player 2('0')
        if x == 'p1':
            p_type = 'X'
        else:
            p_type = '0'
        print(f'{' '*38}{p_type} to play:\n{' '*100}')
        
        #Prompts player for 'LINE' input and checks if valid / if not prompts again
        line = input(f'{' '*40}Line: ')
        while line not in (str(1),str(2),str(3)):
            print(f'\033[4A\r\n{' '*28}Only 1, 2 or 3 allowed, try again!\n\n{' '*38}{p_type} to play:\n')
            line = input(f'{' '*40}Line: ')
        #Saves player's 'LINE' input in (x)_line
        globals()[f'{x}_line'] = int(line)
        
        #Prompts player for 'COLUMN' input and checks if valid / if not prompts again
        column = input(f'{' '*38}Column: ')
        while column not in (str(1),str(2),str(3)):
            print(f'\033[4A\r\n{' '*28}Only 1, 2 or 3 allowed, try again!\n\n{' '*38}{p_type} to play:\n')
            column = input(f'{' '*38}Column: ')
        #Saves player's 'COLUMN' input in (x)_column
        globals()[f'{x}_column'] = int(column)

    
    def indexing(x):
        global area
        #Condition for Player 1('X') or Player 2('0')
        if x == 'p1':
            p_type = 'X'
        else:
            p_type = '0'
        #Breaks string at player's inputs-1, adds 'X'/'0' and rejoins string
        area[globals()[f'{x}_line']-1] = area[globals()[f'{x}_line']-1][:globals()[f'{x}_column']-1] \
                                       + p_type \
                                       + area[globals()[f'{x}_line']-1][globals()[f'{x}_column']:]
        start()
    
    
    input_player(x)
    
    #Checks if player's input location is already used or not
    while area[globals()[f'{x}_line']-1][globals()[f'{x}_column']-1] != ' ':
        print(f"\033[4A\r{' '*30}This space was already used!\n{' '*100}")
        input_player(x)
    else:
        indexing(x)


def won():
    global area
    
        #Checks if there are 3 'X' in the same row
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
    global area,p1_line,p1_column,p2_line,p2_column,score_0,score_x
    
    #Runs game and checks if any player won or if it's a stalemate
    trigger = False
    start()
    while trigger == False:
        if won() == 'A':
            print(f"{' '*35}{'-'*16}\n{' '*35}0 is the Winner!\n{' '*35}{'-'*16}")
            score_0 += 1
            break
        elif won() == 'B':    
            print(f"{' '*34}{'-'*17}\n{' '*34}S T A L E M A T E!\n{' '*34}{'-'*17}")
            break
        else:    
            player('p1')
            trigger = True
        while trigger == True:
            if won() == 'A':
                print(f"{' '*35}{'-'*16}\n{' '*35}X is the Winner!\n{' '*35}{'-'*16}")
                score_x += 1
                break
            elif won() == 'B':    
                print(f"{' '*34}{'-'*17}\n{' '*34}S T A L E M A T E!\n{' '*34}{'-'*17}")
                break
            else:    
                player('p2')
                trigger = False
                break
    
    #Ask user if they want to play again and resets the game, else nothing
    temp = input(f"\n{' '*37}Play again ?\n{' '*35}Y (yes) / N (no)\n{' '*43}")
    if temp.upper() == 'Y':
        area = ['   ', '   ', '   ']
        p1_line,p1_column,p2_line,p2_column = '','','',''
        run_game()


run_game()
