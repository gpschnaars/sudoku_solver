

class Board(list):
    """
    Class for a sudoku board, containing methods to solving.

    init the board with an 81-char string of numbers read left to right, moving down the board (as if reading text)

    or as a list of lists
    """

    def __init__(self, s):
        try:
            matrix = self.convert_str(s)
        except TypeError:
            # already list of lists (testing purposes)
            matrix = s
        super().__init__(matrix)

    @staticmethod
    def convert_str(s):
        # convert 81-char input string to a 9x9 list of lists
        return [list(map(int, l)) for l in [s[i:i+9] for i in range(0, len(s), 9)]]

    @staticmethod
    def check_list(l):
        # ensure the total sum of the row is 45 and contains no dupes (9 items total)
        if sum(l) != 45 or len(set(l)) != 9:
            return False
        else:
            return True

    @staticmethod
    def transpose(arr):
        # transpose a list of lists 
        return list(map(list, zip(*arr)))

    @staticmethod
    def get_missing(l):
        # get ints missing from [1,9] in a list
        return {1,2,3,4,5,6,7,8,9} - set(l)

    def check_board(self):
        rows = all(self.check_list(l) for l in self)
        cols = all(self.check_list(l) for l in self.transpose(self))
        return rows and cols


    def get_empties(self):
        # return list of positions (i, j) of empty cells in <arr>
        return [(i, j) for i, sub_arr in enumerate(self) for j, item in enumerate(sub_arr) if item == 0]


    def get_possibles(self, i, j):
        # determine what possible values an empty cell may take on
        return self.get_missing(self[i]) & self.get_missing(self.transpose(self)[j])


    def solve(self):
        empties = self.get_empties()
        if empties:
            for i, j in empties:
                possible_vals = self.get_possibles(i, j)
                if possible_vals:
                    for val in possible_vals:
                        old_val = self[i][j]
                        self[i][j] = val
                        if self.solve():
                            return True
                        else:
                            self[i][j] = old_val
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return self.check_board()


    def show_nicely(self):
        for i, item in enumerate(self):
            print(' | '.join(str(j) for j in item))
            if i != len(self)-1:
                print('-'*33)


if __name__ == '__main__':

    pass