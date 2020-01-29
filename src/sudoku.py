import time
import csv


class Sudoku:
    """
    A Soduku Solver using different search algorithms
    Soduku are generated via https://qqwing.com/generate.html
    Invalid Soduku are fetched from http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html
    Sudokus with multiple solutions are not under considered
    Invalid sudoku includes unsolvable sudoku and sudoku with invalid init state
    """

    def __init__(self):

        # sudoku data
        self.sudoku_board = None
        self.meta_data = None

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

    def read_soduku(self, sudoku_dict: dict):
        """
        Read one entry of the parsed sudoku metadata
        :return: void
        """

        def to_board(string: str) -> list:
            board = [list(string[i*9:i*9+9]) for i in range(9)]
            return board

        # read data
        self.sudoku_board = to_board(sudoku_dict['puzzle'])
        self.meta_data = sudoku_dict

    def solve_soduku(self, mode: str, repeat=1) -> (bool, float):
        """
        Try to solve the soduku with selected approach
        :param mode: selected approach -> {'dfs', 'bfs', 'deepening'}
        :param repeat: solve the sudoku n times to get the average solving time
        :return:
        """

        def to_str(board: list) -> str:
            string = "".join([board[i][j] for i in range(9) for j in range(9)])
            return string

        start = time.time()
        k = repeat
        can_solve = False
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

        if to_str(self.sudoku_board) != self.meta_data['solution']:
            raise Exception("Solution is incorrect!")

        end = time.time()
        time_spent = round((end - start) / repeat, 4)

        return can_solve, time_spent

    def validate(self) -> bool:
        """
        Check whether the solution is valid
        :return: bool -> True: solution is valid False: solution is not valid
        """
        pass

    @staticmethod
    def parser(src_p) -> list:
        """
        Data parser that read the soduku metadata.
        csv columns:
        Puzzle,Solution,Givens,Singles,Hidden Singles,Naked Pairs,Hidden Pairs,Pointing Pairs/Triples,Box/Line Intersections,Guesses,Backtracks,Difficulty
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
                soduku_metadata = {'puzzle': line[0], 'solution': line[1], 'givens': line[2], 'singles': line[3],
                                   'hidden_singles': line[4], 'naked_pairs': line[5], 'hidden_paris': line[6],
                                   'triples': line[7], 'intersections': line[8], 'guesses': line[9],
                                   'backtracks': line[10], 'difficulty': line[11]}
                parsed_data.append(soduku_metadata)

        return parsed_data


src = '/home/jgeng/Documents/Git/ECE637-Project1/input/invalid.csv'
parsed = Soduku.parser(src)
print(len(parsed))
print(parsed[0])

