class Board:
    BOARD_SIZE = 9
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'
    PLAYERS = (PLAYER_1, PLAYER_2)
    board = [None] * BOARD_SIZE

    def tick(self, position: int, player: int):
        if player not in self.PLAYERS:
            raise Exception(f'Player {player} is invalid')

        target_position = self.board[position]
        if target_position is not None:
            raise Exception(f'Invalid move! There is already player {target_position} on position {position}')

        self.board[position] = player

    def is_free(self, position: int):
        return self.board[position] is None

    def get_winner(self):
        for line in self.get_lines():
            unique_line = set(line)
            if len(unique_line) == 1:
                return unique_line[0]
        return None

    def get_rows(self):
        rows = []
        for offset in [0, 3, 6]:
            rows.append(self.board[offset:offset + 3])

        return rows

    def get_columns(self):
        return [self.board[offset::3] for offset in range(0, 3)]

    def get_diagonals(self):
        return [self.board[0::4], self.board[2:7:2]]

    def get_lines(self):
        return self.get_rows() + self.get_columns() + self.get_diagonals()
