def solution(N, P, Q):
    primes = [1] * (N+1)
    primes[0] = primes[1] = 0

    N_sqrt = int(N ** 0.5)
    for i in range(2, N_sqrt + 1):
        if primes[i]:
            k = i * i
            while k <= N:
                primes[k] = 0
                k += i

    all_semi_primes = [0] * (N+1)
    for i in range(N+1):
        for j in range(N+1):
            if primes[i] and primes[j] and i*j <= N:
                all_semi_primes[i * j] = 1

            if i * j > N:
                break

    semi_primes = [0] * len(P)
    semi_prices_sum = [0] * (N+1)
    s = 0
    for i in range(N+1):
        s += all_semi_primes[i]
        semi_prices_sum[i] = s

    for i in range(len(P)):
        semi_primes[i] = semi_prices_sum[Q[i]] - semi_prices_sum[P[i]-1]
    return semi_primes