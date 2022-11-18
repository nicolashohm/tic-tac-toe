from Board import Board


class Computer:
    CORNERS = (0, 2, 6, 8)
    REAL_PLAYER = Board.PLAYER_1
    COMPUTER_PLAYER = Board.PLAYER_2

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

    def get_winning_move_for(self, player):
        for line in self.board.get_lines():
            line_list = list(line.values())
            if line_list.count(player) == 2 and line_list.count(None) == 1:
                return list(line.keys())[line_list.index(None)]
        return None

    def compute_next_move(self):
        winning_move_for_computer = self.get_winning_move_for(self.COMPUTER_PLAYER)
        if winning_move_for_computer:
            return winning_move_for_computer

        winning_move_for_real_player = self.get_winning_move_for(self.REAL_PLAYER)
        if winning_move_for_real_player:
            return winning_move_for_real_player

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
