# Testing backtracking and greedy approaches to 3D matching
import random
import sys
import time
import itertools
from matching_3d_backtracking import *
from matching_3d_greedy import *
sys.setrecursionlimit(50000)


def random_M_for(r_seed: int, N: int, m: int):
    random.seed(r_seed)
    M = []
    for i in range(m):
        M.append((random.randint(1,N),random.randint(1,N),random.randint(1,N)))
    return M

def random_M(r_seed: int, N: int, m: int):
    random.seed(r_seed)
    return random.sample(list(itertools.product(range(N), repeat = 3)), k = m)

def solve_time(M, N, m):
    '''
    # Timing Backtracking
    start_time = time.time()
    solver = MatchingSolver(M,N)
    solver.find_solutions()
    seconds_elapsed = time.time() - start_time
    ret1 = f"Backtracking: N = {N}, m = {m} took {seconds_elapsed} seconds, or {seconds_elapsed/60} minutes"
    '''

    #Timing Greedy
    print("Starting time")
    start_time = time.time()
    sol = greedy_approx(M)
    end_time = time.time()
    print(sum(sol) / N)
    seconds_elapsed = end_time - start_time
    return f"Greedy: N = {N}, m = {m} took {seconds_elapsed} seconds, or {seconds_elapsed/60} minutes"


def main():
    N1 = 11
    m1 = N1**3
    M1 = random_M(2, N1, m1)
    experiment1 = solve_time(M1, N1, m1)
    print("Experiment1", experiment1)

    '''
    N2 = 100
    m2 = 500*N2
    M2 = random_M(2, N2, m2)
    experiment2 = solve_time(M2, N2, m2)
    print("Experiment2",experiment2)
    
    N3 = 100
    m3 = 1000*N3
    M3 = random_M(2, N3, m3)
    experiment3 = solve_time(M3, N3, m3)
    print("Experiment3",experiment3)
    '''



if __name__ == "__main__":
    main()