import math
import timeit


def f(x):
    return x**6 + x - 1


def df(x):
    return 6*x**5 + 1


def newton():
    x0 = 1
    tolerance = 1e-6
    maxiterr = 1000
    count_iterations = 0

    for i in range(maxiterr):
        count_iterations += 1
        fx = f(x0)
        dfx = df(x0)

        x1 = x0 - (fx / dfx)

        if abs(f(x1)) < tolerance:
            print(f"Number of iterations taken = {count_iterations}")

            print(f"Root found at x = {x1:.6f}")

            break
        else:
            x0 = x1


time_taken = timeit.timeit(newton, number=10000)

print(f"Newton method took an average of {time_taken/10000:.6f} seconds per run over 10000 runs.")
