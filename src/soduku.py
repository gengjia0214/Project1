import csv


class Soduku:
    """
    A Soduku Solver using different search algorithms
    Soduku are generated via https://qqwing.com/generate.html
    """

    def __init__(self):
        self.suduko = None
        self.solution = None
        self.difficulty = None
        self.memo = None

    def read_soduku(self):
        """
        Read a soduku puzzle
        :return:
        """
        pass

    def solve_soduku(self, mode: str):
        """
        Try to solve the soduku with selected approach
        :param mode: selected approach -> {'dfs', 'bfs', 'deepening'}
        :return:
        """

        def __to_str(board: list) -> str:
            """
            Convert the soduku 2-D grid to string
            :return: string soduku rep
            """

            string = ""
            return string

        if mode == 'dfs':
            self.dfs()
        elif mode == 'bfs':
            self.bfs()
        elif mode == 'deepening':
            self.deepening()
        else:
            raise Exception("Mode must selected from ['dfs', 'bfs', 'deepening'] but was {}".format(mode))

    def dfs(self) -> bool:
        """
        Depth First Search Approach
        :return: bool -> True: solution exists False: solution does not exist
        """
        pass

    def bfs(self) -> bool:
        """
        Breadth First Search Approach
        :return: bool -> True: solution exists False: solution does not exist
        """
        pass

    def deepening(self) -> bool:
        """
        Iterative Deepening Search Approach
        :return: bool -> True: solution exists False: solution does not exist
        """
        pass

    def compare(self) -> bool:
        """
        Check whether the solution found is valid
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

        def to_board(string: str) -> list:
            """
            Convert raw soduku string into 2-D grid
            :return: list -> [[]]
            """

            board = []
            return board

        parsed_data = []
        with open(src_p, mode='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in reader:
                line_count += 1
                if line_count == 1:
                    continue

                # build metadata
                soduku_metadata = {'puzzle': to_board(line[0]), 'solution': line[1], 'given': line[2],
                                   'singles': line[3], 'hidden_singles': line[4], 'naked_pairs': line[5],
                                   'hidden_paris': line[6], 'triples': line[7], 'intersect': line[8],
                                   'guesses': line[9], 'backtracks': line[10], 'difficulty': line[11]}
                parsed_data.append(soduku_metadata)

        return parsed_data





src = '/home/jgeng/Documents/Git/ECE637-Project1/input/easy.csv'
parsed = Soduku.parser(src)
print(len(parsed))
print(parsed[0])

