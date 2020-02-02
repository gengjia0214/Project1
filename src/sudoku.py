import time
import csv
import copy
from queue import SimpleQueue

"""
- A Soduku Solver using different search algorithms
- Soduku are generated via https://qqwing.com/generate.html
- Invalid Soduku are fetched from http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html
- Sudokus with multiple solutions are not included in the test cases as it is hard to create ground truth
- Invalid sudoku includes unsolvable.csv sudoku and sudoku with invalid init state
"""


class Sudoku:
    """
    To use:
    1. Create a solver instance:        solver = Sudoku()
    2. Load csv data:                   parsed_data = Sudoku.parser('/path/to/dir/easy.csv')
    3. Get one data:                    sudoku_data = parsed_data[i]
    4. Read the data:                   solver.read_sudoku(sudoku_data)
    5. Solve it with selected mode:     can_solve, time = solver.solve(mode='dfs')
    6. Report & Read & Solve next one...
    """

    def __init__(self):
        """
        Constructor
        Metadata Keys include:
        'puzzle', 'solution', 'givens', 'singles', 'hidden_singles'
        'naked_pairs', 'hidden_paris', 'triples', 'intersections', 'guesses'
        'backtracks', 'difficulty'
        """

        # sudoku data
        self.sudoku_board = None  # sudoku board in 2-D list
        self.meta_data = None  # meta_data

        # data struct for the solvers
        # memo for dfs but might also work for other solution
        self.row_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th row
        self.col_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th col
        self.box_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th box

    def dfs(self, row, col, lim_dep = 810) -> bool:
        """
        Depth First Search Approach. Recursive implementation. Modify self.sudoku_board inplace.
        Try to fill column by column. If can finish filling the last column -> solution found.
        :param row
        :param col
        :param lim_dep
        :return: bool -> True: solution exists False: solution does not exist
        """

        # when done with the last column, found the solution
        if col == 9:
            return True

        # when depth reach limitation, return false
        if lim_dep == 0:
            return False
        
        # next row and column to be fill
        next_r = (row + 1) % 9
        next_c = col if next_r != 0 else col + 1  # grow col when the curr col is fully filled

        # if the current grid was filled, go to next step
        if self.sudoku_board[row][col] != '.':
            return self.dfs(next_r, next_c)

        # if the current grid is not filled yet -> try to fill the current grid with a valid candidate
        # valid input -> check row_used, col_used, box_used
        # if no valid candidate -> return False
        box_row = row // 3
        box_col = col // 3
        box_id = box_row * 3 + box_col

        # try all candidate
        for num in range(1, 10):
            # check whether num is a valid candidate
            if self.row_used[row][num] == 0 and self.col_used[col][num] == 0 and self.box_used[box_id][num] == 0:

                # fill the sudoku board and update the used memo
                self.row_used[row][num] = 1
                self.col_used[col][num] = 1
                self.box_used[box_id][num] = 1
                self.sudoku_board[row][col] = str(num)

                # go to next step -> True will be returned from the first valid solution
                if self.dfs(next_r, next_c, lim_dep - 1):
                    return True

                # before searching the next branch with dfs -> need to recover the board and memo
                self.sudoku_board[row][col] = '.'
                self.row_used[row][num] = 0
                self.col_used[col][num] = 0
                self.box_used[box_id][num] = 0

        # all possible candidate are checked, no valid solution
        return False

    def bfs(self) -> bool:
        """
        Breadth First Search Approach
        Modify self.sudoku_board inplace
        :return: bool -> True: solution exists False: solution does not exist
        """

        # prepare states
        queue = SimpleQueue()
        col, row = 0, 0  # fill values from col 0 -> col 8 stop at col 9
        init_state = [copy.deepcopy(self.row_used), copy.deepcopy(self.col_used), copy.deepcopy(self.box_used),
                      copy.deepcopy(self.sudoku_board)]

        # find the init loc for starting the bfs
        queue.put(init_state)
        while not queue.empty():
            size = queue.qsize()  # size of the current branch
            i = 0

            # each while loop work on one layer of the bfs tree
            # total of 9x9=81 layers
            while size > 0:

                # work on the next state
                # when down with the one layer, move to the next grid
                curr_state = queue.get()

                # move the row, col to the next grid when work on a new layer
                if i == 0:
                    # get the row and col for the next branches
                    while curr_state[3][row][col] != '.':
                        row = (row + 1) % 9
                        col = col if row != 0 else col + 1  # grow col when the curr col is fully filled

                        # col == 9 -> found solution
                        if col == 9:
                            self.sudoku_board = curr_state[3]
                            return True

                # get the box id
                box_row = row // 3
                box_col = col // 3
                box_id = box_row * 3 + box_col

                # get all possible next state from the current state
                for num in range(1, 10):

                    # check whether num is a valid candidate
                    row_valid = curr_state[0][row][num] == 0
                    col_valid = curr_state[1][col][num] == 0
                    box_valid = curr_state[2][box_id][num] == 0

                    # if row, col + num is valid, fill the next state
                    if row_valid and col_valid and box_valid:
                        next_state = copy.deepcopy(curr_state)
                        next_state[0][row][num] = 1
                        next_state[1][col][num] = 1
                        next_state[2][box_id][num] = 1
                        next_state[3][row][col] = str(num)
                        queue.put(next_state)

                size -= 1
                i += 1

        return False

    def deepening(self) -> bool:
        """
        Iterative Deepening Search Approach
        Modify self.sudoku_board inplace
        :return: bool -> True: solution exists False: solution does not exist
        """

        # TODO: implement iterative deepening approach
        lim_depth = 110
        while dfs(0, 0, lim_depth) = False：
            lim_depth += 50
            if lim_depth = 810:
                return False

    def solve_sudoku(self, mode: str, repeat=1) -> (bool, float):
        """
        Try to solve the soduku with selected approach.
        :raise Exception if the algorithm is not correct!
        :param mode: selected approach -> {'dfs', 'bfs', 'deepening'}
        :param repeat: solve the sudoku n times to get the average solving time
        :return: bool, float -> whether the input is solvable, time spent
        """

        def to_str(board: list) -> str:
            string = "".join([board[i][j] for i in range(9) for j in range(9)])
            return string

        k = repeat
        can_solve = False

        # main loop
        start = time.time()
        while k > 0:
            if mode == 'dfs':
                can_solve = self.dfs(0, 0)
            elif mode == 'bfs':
                can_solve = self.bfs()
            elif mode == 'deepening':
                can_solve = self.deepening()
            else:
                raise Exception("Mode must selected from ['dfs', 'bfs', 'deepening'] but was {}".format(mode))
            k -= 1
        end = time.time()
        time_spent = round((end - start) * 1000 / repeat)

        # check correctness
        solution = to_str(self.sudoku_board)
        if self.meta_data['solution'] == 'False' and can_solve:
            raise Exception("There should be no solution!")
        elif self.meta_data['solution'] != 'False':
            if not can_solve:
                raise Exception("There should be a solution but did not find any solution!")
            if to_str(self.sudoku_board) != self.meta_data['solution']:
                raise Exception("Solution should be {} but was {}!".format(self.meta_data['solution'], solution))

        # if reach here, means the algorithm is correct!
        return can_solve, time_spent

    def read_sudoku(self, sudoku_dict: dict) -> bool:
        """
        Read one entry of the parsed sudoku metadata
        :return: bool -> True the input is valid False the input is not valid
        """

        def to_board(string: str) -> list:
            board = [list(string[i*9:i*9+9]) for i in range(9)]
            return board

        # read metadata
        self.__reset_memo()
        self.sudoku_board = to_board(sudoku_dict['puzzle'])
        self.meta_data = sudoku_dict
        return self.__update_memo()

    def __reset_memo(self) -> None:
        """
        Reset the memo
        :return: void
        """

        self.row_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th row
        self.col_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th col
        self.box_used = [[0 for i in range(10)] for j in range(9)]  # whether i-th value is used for j-th box

    def __update_memo(self) -> bool:
        """
        Update the memo with the input sudoku board
        :return: bool -> True input is valid False -> input is invalid
        """

        for row in range(9):
            for col in range(9):
                box_row = row // 3
                box_col = col // 3
                box_id = box_row * 3 + box_col  # the box id
                fill_val = self.sudoku_board[row][col]
                if fill_val != '.':
                    fill_val = int(fill_val)

                    # if the value is used for twice, input invalid
                    if self.row_used[row][fill_val] != 0 or self.col_used[col][fill_val] != 0 \
                            or self.box_used[box_id][fill_val] != 0:
                        return False

                    self.row_used[row][fill_val] = 1
                    self.col_used[col][fill_val] = 1
                    self.box_used[box_id][fill_val] = 1

        return True

    @staticmethod
    def parser(src_p) -> list:
        """
        Data parser that read the soduku metadata.
        :param src_p: input sudoku samples in csv format
        :return: List -> parsed data that is compatible with this solver
        """

        parsed_data = []
        with open(src_p, mode='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in reader:
                line_count += 1
                if line_count == 1 or len(line) == 0:
                    continue

                # build metadata
                soduku_metadata = {'puzzle': line[0], 'solution': line[1], 'givens': int(line[2]),
                                   'singles': int(line[3]), 'hidden_singles': int(line[4]),
                                   'naked_pairs': int(line[5]), 'hidden_paris': int(line[6]),
                                   'triples': int(line[7]), 'intersections': int(line[8]), 'guesses': int(line[9]),
                                   'backtracks': int(line[10]), 'difficulty': line[11]}
                parsed_data.append(soduku_metadata)

        return parsed_data

