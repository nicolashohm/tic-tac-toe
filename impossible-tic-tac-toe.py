"""
Game
0 1 2
3 4 5
6 7 8
"""
class Board:
    BOARD_SIZE = 9
    PLAYER = (0, 1)
    board = [None] * BOARD_SIZE

    def tick(self, position: int, player: int):
        target_position = self.board[position]
        if target_position is not None:
            raise Exception(f'Invalid move! There is already player {target_position} on position {position}')

        self.board[position] = player

    def is_free(self, position: int):
        return self.board[position] is None

def render_board(board: Board):
    content = ''
    for offset in [0, 3, 6]:
        content = f'{content}\n' + "\t|\t".join(map(lambda x: '_' if x is None else str(x), board.board[offset:offset+3]))
    return content

class Computer:
    CORNERS = (0, 2, 6, 8)
    COMPUTER_PLAYER = 0
    REAL_PLAYER = 1

    def __init__(self, board: Board) -> None:
        self.board = board

    def find_free_corner(self):
        for corner in self.CORNERS:
            # TODO pick random corner
            if self.board.board[corner] is None:
                return corner
        return None

    def find_ticked_corner(self):
        for corner in self.CORNERS:
            if self.board.board[corner] is self.COMPUTER_PLAYER:
                return corner

    def is_player_about_to_win(self):
        dangerous_state = {3: None, 4: 1, 5: 1}
        return self.board.board[3:6] == list(dangerous_state.values())

    def compute_next_move(self):
        if self.is_player_about_to_win():
            return 3

        neighbor_corners = {0: (2, 6), 2: (0, 8), 6: (0, 8), 8: (2, 6)}
        ticked_corner = self.find_ticked_corner()
        if ticked_corner is not None:
            for next_tick in neighbor_corners[ticked_corner]:
                if self.board.is_free(next_tick):
                    return next_tick

        free_corner = self.find_free_corner()
        if free_corner is not None:
            return free_corner
        else:
            print('TODO')

board = Board()
computer = Computer(board)
board.tick(0, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(4, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)
board.tick(5, 1)
board.tick(computer.compute_next_move(), Computer.COMPUTER_PLAYER)



print(render_board(board))
