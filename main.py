"""
Game
0 1 2
3 4 5
6 7 8
"""
from Board import Board
from Computer import Computer


def render_board(board: Board):
    content = ''
    for row in board.get_rows():
        content = f'{content}\n' + "\t|\t".join(
            map(lambda x: '_' if x is None else str(x), row.values())
        )
    return content


board = Board()
computer = Computer(board)

# Test game 1: 0, 4, 5, 1
# Test game 2: 0, 8, 6, 3
while board.is_possible_move() and not board.get_winner():
    board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
    print(render_board(board))
    if board.get_winner():
        break
    next_move = input('What is your next move? ')
    board.tick(int(next_move), Computer.REAL_PLAYER)

print('The winner is: ' + board.get_winner())
