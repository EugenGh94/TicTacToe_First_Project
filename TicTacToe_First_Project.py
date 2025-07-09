area = ('   ', '   ', '   ')
p1_line,p1_column,p2_line,p2_column = '','','','' 

def start():
    trigger = True
    t = 1
    for _ in area:
        if trigger:
            print('  1 2 3')
            trigger = False
        print(f'{t} {_[0]}|{_[1]}|{_[2]}')
        t += 1
        if t <= 3:
            print('  -+-+-')
    print('\n')

def p1():
    global area,p1_line,p1_column
    def input_p1():
        global area,p1_line,p1_column
        print('X to play:')
        p1_line = input('Line: ')
        while p1_line not in (str(1),str(2),str(3)):
            print('\nOnly 1, 2 or 3 allowed, try again!\n\nX to play:')
            p1_line = input('Line: ')
        p1_line = int(p1_line)
        p1_column = input('Column: ')
        while p1_column not in (str(1),str(2),str(3)):
            print('\nOnly 1, 2 or 3 allowed, try again!\n\nX to play:')
            p1_column = input('Column: ')
        p1_column = int(p1_column)
    def index_p1():
        global area,p1_line,p1_column
        new = area[p1_line-1][:p1_column-1] + 'X' + area[p1_line-1][p1_column:]
        y = list(area)
        y[p1_line-1] = new
        area = tuple(y)
        start()
    input_p1()
    while area[p1_line-1][p1_column-1] != ' ':
        print('-'*28 + '\n' 'This space was already used!\n' + '-'*28)
        input_p1()
    else:
        index_p1()

def p2():
    global area,p2_line,p2_column
    def input_p2():
        global area,p2_line,p2_column
        print('0 to play:')
        p2_line = input('Line: ')
        while p2_line not in (str(1),str(2),str(3)):
            print('\nOnly 1, 2 or 3 allowed, try again!\n\n0 to play:')
            p2_line = input('Line: ')
        p2_line = int(p2_line)
        p2_column = input('Column: ')
        while p2_column not in (str(1),str(2),str(3)):
            print('\nOnly 1, 2 or 3 allowed, try again!\n\n0 to play:')
            p2_column = input('Column: ')
        p2_column = int(p2_column)
    def index_p2():
        global area,p2_line,p2_column
        new = area[p2_line-1][:p2_column-1] + '0' + area[p2_line-1][p2_column:]
        y = list(area)
        y[p2_line-1] = new
        area = tuple(y)
        start()
    input_p2()
    while area[p2_line-1][p2_column-1] != ' ':
        print('-'*28 + '\n' 'This space was already used!\n' + '-'*28)
        input_p2()
    else:
        index_p2()

def won():
    global area
    if ' ' in area[0] or ' ' in area[1] or ' ' in area[2]:
        if ((area[0][0]=='X' and area[0][1]=='X' and area[0][2]=='X') or
            (area[1][0]=='X' and area[1][1]=='X' and area[1][2]=='X') or
            (area[2][0]=='X' and area[2][1]=='X' and area[2][2]=='X') or
            (area[0][0]=='X' and area[1][0]=='X' and area[2][0]=='X') or
            (area[0][1]=='X' and area[1][1]=='X' and area[2][1]=='X') or
            (area[0][2]=='X' and area[1][2]=='X' and area[2][2]=='X') or
            (area[0][0]=='X' and area[1][1]=='X' and area[2][2]=='X') or
            (area[0][2]=='X' and area[1][1]=='X' and area[2][0]=='X') or
            
            (area[0][0]=='0' and area[0][1]=='0' and area[0][2]=='0') or
            (area[1][0]=='0' and area[1][1]=='0' and area[1][2]=='0') or
            (area[2][0]=='0' and area[2][1]=='0' and area[2][2]=='0') or
            (area[0][0]=='0' and area[1][0]=='0' and area[2][0]=='0') or
            (area[0][1]=='0' and area[1][1]=='0' and area[2][1]=='0') or
            (area[0][2]=='0' and area[1][2]=='0' and area[2][2]=='0') or
            (area[0][0]=='0' and area[1][1]=='0' and area[2][2]=='0') or
            (area[0][2]=='0' and area[1][1]=='0' and area[2][0]=='0')):
            return 'A'
    else:
        return 'B'

def run_game():
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
            p1()
            trigger = True
        while trigger == True:
            if won() == 'A':
                print('-'*16 + '\n' 'X is the Winner!\n' + '-'*16)
                break
            elif won() == 'B':    
                print('-'*17 + '\n' +'S T A L E M A T E\n' + '-'*17)
                break
            else:    
                p2()
                trigger = False
                break

run_game()
