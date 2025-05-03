import time

def collatz(n):
    itterrations = 0
    while n > 1:
        if n % 2 == 0:
            n //=2
        else:
            n = n * 3 + 1
        itterrations += 1
    return itterrations

def main():
    start_time = time.time()
    start_from = 2
    end_at = 10000002
    total_iterations = 0
    for i in range(start_from,end_at):
        total_iterations += 1
        if collatz(i) == 0:
            break

    print("--- %s seconds ---" % (time.time() - start_time))


main()
