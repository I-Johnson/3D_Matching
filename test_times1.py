import random
import sys
import time
import csv
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

def solve_time_BT(M, N, m):
    start_time = time.time()
    solver = MatchingSolver(M,N)
    solver.find_solutions()
    seconds_elapsed = time.time() - start_time
    return seconds_elapsed

def append_to_csv(data, filename='data.csv'):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def run_experiment(N):
    for i in range(5):
        r_seed = i
        #r_seed = random.randint(1,N)
        experiments = [(N, 2*N), (N, N**2), (N, (N**2 + N**3)//2), (N, N**3)]  # Add more tuples as (N, m) for each experiment

        # Ensuring the CSV file has headers if it's empty/new
        try:
            with open('data.csv', 'x', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['N', 'm', 'Time (seconds)'])
        except FileExistsError:
            pass  # File already exists, skip writing headers

        for idx, (N, m) in enumerate(experiments, 1):
            M = random_M(r_seed, N, m)
            time_elapsed = solve_time_BT(M, N, m)
            append_to_csv([N, m, time_elapsed])

def main():
    run_experiment(5)
    run_experiment(9)
    run_experiment(12)
    print("Experiments completed and data saved to CSV.")

if __name__ == "__main__":
    main()