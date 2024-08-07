def prime_generator():
    """素数を順番に生成するジェネレータ"""
    D = {}
    q = 2  
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

gen = prime_generator()
primes = [next(gen) for _ in range(10)]
print(primes)

