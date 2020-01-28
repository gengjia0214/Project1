

class Soduku:
    """
    A Soduku Solver using different search algorithms
    """

    def __init__(self):
        self.suduko = None
        self.solution = None
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
    def parser() -> list:
        """
        Data parser that read the soduku metadata .
        :return: List -> parsed data that is compatible with this solver
        """
        pass

