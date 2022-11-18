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
    for offset in [0, 3, 6]:
        content = f'{content}\n' + "\t|\t".join(
            map(lambda x: '_' if x is None else str(x), board.board[offset:offset + 3])
        )
    return content


board = Board()
computer = Computer(board)
board.tick(0, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(4, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(5, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)

print(render_board(board))
