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
board.tick(0, Board.PLAYER_1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(4, Board.PLAYER_1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(5, Board.PLAYER_1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(1, Board.PLAYER_1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)

print(render_board(board))

print(board.get_lines())

print(board.get_winner())
