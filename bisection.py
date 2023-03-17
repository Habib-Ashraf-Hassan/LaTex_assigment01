import timeit


def f(x):
    return x ** 6 + x - 1


def bisection_method():
    a, b = 0, 2
    tolerance = 1e-6
    max_iteration = 1000
    count_iteration = 0
    if f(a) * f(b) >= 0:
        print("Root cannot be found; range[a, b] should generate f(a) and f(b) with opposite signs")
    for i in range(max_iteration):
        count_iteration += 1
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            print(f"Number of iterations taken are {count_iteration}")
            print(f"Root found at x={c:.6f}")
            break

        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c


bisection_method()

time_taken = timeit.timeit(bisection_method, number=10000)

print(f"Bisection method took an average of {time_taken / 10000:.6f} seconds per run over 10000 runs.")
