area = ('   ', '   ', '   ')
p1_line,p1_row,p2_line,p2_row = '','','','' 

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
    global area
    print('X to play:')
    p1_line = int(input())
    p1_row = int(input())
    new = area[p1_line-1][:p1_row-1] + 'X' + area[p1_line-1][p1_row:]
    y = list(area)
    y[p1_line-1] = new
    area = tuple(y)
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

def p2():
    global area
    print('0 to play:')
    p2_line = int(input())
    p2_row = int(input())
    new = area[p2_line-1][:p2_row-1] + '0' + area[p2_line-1][p2_row:]
    y = list(area)
    y[p2_line-1] = new
    area = tuple(y)
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

def won():
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
        return 'WINNER'

def run_game():
    start()
    p1()
    while won() != 'WINNER':
        p2()
        while won() != 'WINNER':
            p1()
            break
        else:
            print('0 is the Winner !')
            return 'end'
    else:
        print('X is the Winner !')
        return 'end'
    
    

run_game()