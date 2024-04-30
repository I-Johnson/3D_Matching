'''
Jonah Stephens
Backtracking Abstract Class
'''

from abc import abstractmethod, ABC

class ComputationTreeNode(ABC):
    @abstractmethod
    def __init__(self, *args):
        raise NotImplementedError

    @abstractmethod
    def is_promising(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_children(self):
        raise NotImplementedError

    @abstractmethod
    def is_complete_solution(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def write_solution(self) -> None:
        raise NotImplementedError


class BacktrackingSolver(ABC):

    @abstractmethod
    def __init__(self, *args):
        raise NotImplementedError

    @abstractmethod
    def get_root_node(self):
        raise NotImplementedError

    def check_node(self, node):
        if node.is_promising():
            if node.is_complete_solution():
                # Writes all feasible solutions.
                node.write_solution()
            else:
                for child in node.get_children():
                    self.check_node(child)

    def find_solutions(self):
        self.check_node(self.get_root_node())
