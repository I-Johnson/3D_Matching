from backtracking_abc import *

class MatchingNode(ComputationTreeNode):
    def __init__(self, solver, Q):
        self.solver = solver
        self.Q = Q

    def get_children(self):
        children = []
        children.append(MatchingNode(self.solver, self.Q + [0]))
        children.append(MatchingNode(self.solver, self.Q + [1]))
        return children
    
    def is_promising(self) -> bool:
        for i in range(len(self.Q)):
            if self.Q[i] == 1:
                for j in range(i+1, len(self.Q)):
                    if self.Q[j] == 1:
                        if (self.solver.M[i][0] == self.solver.M[j][0] or 
                            self.solver.M[i][1] == self.solver.M[j][1] or 
                            self.solver.M[i][2] == self.solver.M[j][2]):
                            return False
        return True        
    
    def is_complete_solution(self) -> bool:
        return len(self.Q) == len(self.solver.M) or sum(self.Q) == self.solver.N
    
    def write_solution(self) -> None:
        self.solver.solutions.append(self.Q)
        

class MatchingSolver(BacktrackingSolver):
    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.solutions = []

    def get_root_node(self):
        return MatchingNode(self, [])
    
    def find_solutions(self):
        self.check_node(self.get_root_node())

        for i in range(len(self.solutions)):
            if sum(self.solutions[i]) == self.N:
                print("Perfect Mathing Found:", self.solutions[i])
                return
        print("No perfect solution")
    

def main():
    '''
    # X = ["golden", "bulldog", "lab"]
    # Y = ["siamese", "shorthair", "orange"]
    # Z = ["hamster", "capybara", "rat"]

    M = [("golden", "siamese", "hamster"),
         ("golden", "shorthair", "hamster"),
         ("bulldog", "shorthair", "capybara"),
         ("lab", "orange", "rat"),
         ("bulldog", "orange", "hamster")]
    
    #solution will be [1,0,1,1,0]

    solve = MatchingSolver(M, 3)
    solve.find_solutions()
    '''

    import time
    import sys 

    import random
    #random.seed(1)
    random.seed(2)
    #random.seed(3)

    sys.setrecursionlimit(50000)

    M = []
    N = 10
    m = 4*N
    for i in range(m):
        M.append((random.randint(1, N), random.randint(1, N), random.randint(1, N)))
    
    start_time = time.time()

    solve = MatchingSolver(M,N)
    solve.find_solutions()

    #seconds
    print(time.time() - start_time)
    # units in minutes
    print((time.time() - start_time)/60)

if __name__ == "__main__":
    main()
