# 틱택토
# https://www.acmicpc.net/problem/7682

# https://kibbomi.tistory.com/183

def check_x():
    check = False
    for i in range(3):
        if board[i][0] == 'X' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            check = True
    for i in range(3):
        if board[0][i] == 'X' and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            check = True
    
    if board[0][0] == 'X' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        check = True
    
    if board[0][2] == 'X' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        check = True
    return check

def check_o():
    check = False
    for i in range(3):
        if board[i][0] == 'O' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            check = True
    for i in range(3):
        if board[0][i] == 'O' and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            check = True
    
    if board[0][0] == 'O' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        check = True
    
    if board[0][2] == 'O' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        check = True
    return check

while True:
    line = input()
    if line == 'end':
        break
    board = [[0] * 3 for _ in range(3)]
    idx = 0
    left = 0
    right = 0
    result = 'invalid'
    for i in range(3):
        for j in range(3):
            board[i][j] = line[idx]
            if line[idx] == 'X':
                left += 1
            elif line[idx] == 'O':
                right += 1
            idx += 1
    
    x = check_x()
    o = check_o()

    if x and not o and left - 1 == right:
        result = 'valid'
    elif not x and o and left == right:
        result = 'valid'
    elif not x and not o and left == 5 and right == 4:
        result = 'valid'

    print(result)