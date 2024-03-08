from classes import Board

is_go = True
while is_go:
    board = Board()
    check = 0
    while board.count_available_steps() != 0:
        player = 'x' if check == 0 else '0'
        coords = input(f'{player}, your turn, enter coordinates devided by space: ')
        x, y = map(int, coords.split())
        if not board.check_available_cell(x, y):
            board.put_value(int(x), int(y), player)
            board.show_board()
            if board.check_winner(player):
                print(f'{player} win!!')
                break
            check = 0 if check > 0 else 1
    ask = input('Continue? ')
    if ask.lower() == 'no':
        is_go = False