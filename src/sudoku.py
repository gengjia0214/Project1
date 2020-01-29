import time
import csv

"""
- A Soduku Solver using different search algorithms
- Soduku are generated via https://qqwing.com/generate.html
- Invalid Soduku are fetched from http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html
- Sudokus with multiple solutions are not included in the test cases as it is hard to create ground truth
- Invalid sudoku includes unsolvable sudoku and sudoku with invalid init state
"""


class Sudoku:
    """
    To use:
    1. Create a solver instance:        solver = Sudoku()
    2. Load csv data:                   parsed_data = Sudoku.parser('/path/to/dir/easy.csv')
    3. Read one data:                   sudoku_data = parsed_data[i]
    4. Solve it with selected mode:     can_solve, time = solver.solve(mode='dfs')
    5. Report & Read & Solve next one...
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
        self.memo = None

    def dfs(self) -> bool:
        """
        Depth First Search Approach
        Modify self.sudoku_board inplace
        :return: bool -> True: solution exists False: solution does not exist
        """

        # TODO: implement dfs approach
        pass

    def bfs(self) -> bool:
        """
        Breadth First Search Approach
        Modify self.sudoku_board inplace
        :return: bool -> True: solution exists False: solution does not exist
        """

        # TODO: implement bfs approach
        pass

    def deepening(self) -> bool:
        """
        Iterative Deepening Search Approach
        Modify self.sudoku_board inplace
        :return: bool -> True: solution exists False: solution does not exist
        """

        # TODO: implement iterative deepening approach
        pass

    def read_sudoku(self, sudoku_dict: dict):
        """
        Read one entry of the parsed sudoku metadata
        :return: void
        """

        def to_board(string: str) -> list:
            board = [list(string[i*9:i*9+9]) for i in range(9)]
            return board

        # read metadata
        self.sudoku_board = to_board(sudoku_dict['puzzle'])
        self.meta_data = sudoku_dict

    def solve_sudoku(self, mode: str, repeat=3) -> (bool, float):
        """
        Try to solve the soduku with selected approach
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
                can_solve = self.dfs()
            elif mode == 'bfs':
                can_solve = self.bfs()
            elif mode == 'deepening':
                can_solve = self.deepening()
            else:
                raise Exception("Mode must selected from ['dfs', 'bfs', 'deepening'] but was {}".format(mode))
            k -= 1
        end = time.time()

        # check correctness
        if self.meta_data['solution'] == 'False' and can_solve:
            raise Exception("Solution is incorrect!")
        elif to_str(self.sudoku_board) != self.meta_data['solution']:
            raise Exception("Solution is incorrect!")
        else:
            time_spent = round((end - start) / repeat, 4)

        return can_solve, time_spent

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

