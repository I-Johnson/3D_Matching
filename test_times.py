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
    # Timing Backtracking
    start_time = time.time()
    solver = MatchingSolver(M,N)
    solver.find_solutions()
    seconds_elapsed = time.time() - start_time
    print("Backtracking: N =",N, "m=", m, "took", seconds_elapsed, "seconds or", seconds_elapsed/60, "minutes.")


def main():
    N1 = 100
    m1= 100*N1
    M1 = random_M(1, N1, m1)

    solve_time(M1, N1, m1)

    # N2 = 20
    # m2= N2**3
    # M2 = random_M(1, N2, m2)

    # solve_time(M1, N1, m1)
    # solve_time(M2, N2, m2)



if __name__ == "__main__":
    main()