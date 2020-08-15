import math
from numba import jit

@jit
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

num = 600851475143
#num = 13195

for p in primes_sieve2(int(math.sqrt(num))):
	if num % p == 0:
		print(p)
		while num % p == 0:
			num /= p
	if num == 1:
		break