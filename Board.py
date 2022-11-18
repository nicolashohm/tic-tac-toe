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
