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

def random_M_greedy(r_seed: int, experiments):
    random.seed(r_seed)
    N = experiments[0][0]
    prod = list(itertools.product(range(N), repeat = 3))

    Ms = []
    for idx, (N, m) in enumerate(experiments, 1):
        Ms.append(random.sample(prod, k = m))

    return Ms
    

def solve_time_BT(M, N, m):
    start_time = time.time()
    solver = MatchingSolver(M,N)
    solver.find_solutions()
    seconds_elapsed = time.time() - start_time
    return seconds_elapsed

def solve_time_greedy(M):
    start_time = time.time()
    count = greedy_approx(M)
    seconds_elapsed = time.time() - start_time
    return seconds_elapsed, count

def append_to_csv(data, filename='data.csv'):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def run_experiment_BT(N):
    for i in range(5):
        r_seed = i
        #r_seed = random.randint(1,N)
        experiments = [(N, 2*N), (N, N**2), (N, (N**2 + N**3)//2), (N, N**3)]  # Add more tuples as (N, m) for each experiment

        # Ensuring the CSV file has headers if it's empty/new
        try:
            with open('data_BT.csv', 'x', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['N', 'm', 'Time (seconds)'])
        except FileExistsError:
            pass  # File already exists, skip writing headers

        for idx, (N, m) in enumerate(experiments, 1):
            M = random_M(r_seed, N, m)
            time_elapsed = solve_time_BT(M, N, m)
            append_to_csv([N, m, time_elapsed], 'data_BT.csv')

def run_experiment_greedy(N):
    # not doing multiple seeds; it'll take too long
    r_seed = 1
    #r_seed = random.randint(1,N)
    experiments = [(N, 2*N), (N, N**2), (N, (N**2 + N**3)//2), (N, N**3)]  # Add more tuples as (N, m) for each experiment

    # Ensuring the CSV file has headers if it's empty/new
    try:
        with open('data_greedy.csv', 'x', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['N', 'm', 'Time (seconds)', 'Accuracy'])
    except FileExistsError:
        pass  # File already exists, skip writing headers

    Ms = random_M_greedy(r_seed, experiments)
    for M in Ms:
        time_elapsed, count = solve_time_greedy(M)
        append_to_csv([N, len(M), time_elapsed, (count/N)], 'data_greedy.csv')

def main():
    #for i in range(4,13):
    #    run_experiment_BT(i)

    for j in range(100, 801, 50):
        run_experiment_greedy(j)
    
    print("Experiments completed and data saved to CSV.")

if __name__ == "__main__":
    main()