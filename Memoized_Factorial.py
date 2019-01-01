factorial_mem = {}

def memoized_fact(n):
    if n < 2:
        return 1
    if not n in factorial_mem:
        factorial_mem[n] = n * memoized_fact(n-1)
    return factorial_mem[n]

print(memoized_fact(4))
