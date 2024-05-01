import random
import sys
import time
import csv
from matching_3d_backtracking import *
from matching_3d_greedy import *

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
    start_time = time.time()
    solver = MatchingSolver(M,N)
    solver.find_solutions()
    seconds_elapsed = time.time() - start_time
    return seconds_elapsed

def append_to_csv(data, filename='data.csv'):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def main():
    experiments = [(5, 5*10), (10, 10*10), (20, 20*50)]  # Add more tuples as (N, m) for each experiment

    # Ensuring the CSV file has headers if it's empty/new
    try:
        with open('data.csv', 'x', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Experiment ID', 'N', 'm', 'Time (seconds)'])
    except FileExistsError:
        pass  # File already exists, skip writing headers

    for idx, (N, m) in enumerate(experiments, 1):
        M = random_M(1, N, m)
        time_elapsed = solve_time(M, N, m)
        append_to_csv([f'e{idx}', N, m, time_elapsed])

    print("Experiments completed and data saved to CSV.")

if __name__ == "__main__":
    main()
