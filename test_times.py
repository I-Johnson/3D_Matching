# Testing backtracking and greedy approaches to 3D matching
import random
import sys
import time
from matching_3d_backtracking import *
from matching_3d_greedy import *

'''
# Testing some ways to remove duplicates
l = [1,2,3,3,5,2,9,4,6,12,5,8]

print(l)
print(list(set(l)))

res = []
[res.append(x) for x in l if x not in res]
print(res)
'''

def random_M(r_seed: int, N: int, m: int):
    sys.setrecursionlimit(50000)
    random.seed(r_seed)

    M = []
    i = 0
    while i < m:
        triple = (random.randint(1, N), random.randint(1, N), random.randint(1, N))
        if triple not in M:
            M.append(triple)
            i += 1
    
    return M

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
    start_time = time.time()
    sol = greedy_approx(M)
    end_time = time.time()
    print(sum(sol) / N)
    seconds_elapsed = end_time - start_time
    #print(sum(sol) / N)
    return f"Greedy: N = {N}, m = {m} took {seconds_elapsed} seconds, or {seconds_elapsed/60} minutes"


def main():
    N1 = 100
    m1 = 100*N1
    M1 = random_M(2, N1, m1)
    experiment1 = solve_time(M1, N1, m1)
    print("Experiment1", experiment1)

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



if __name__ == "__main__":
    main()