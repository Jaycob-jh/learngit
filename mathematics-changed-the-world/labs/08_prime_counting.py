import math
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp


def prime_pi_table(n):
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = False
    return np.cumsum(is_prime)

N = 100000
pi_table = prime_pi_table(N)
x = np.unique(np.geomspace(10, N, 600).astype(int))
pi_x = pi_table[x]
x_over_log_x = x / np.log(x)
li_x = np.array([float(mp.li(int(v))) for v in x])

print("x, pi(x), x/log(x), li(x)")
for v in [100, 1000, 10000, 100000]:
    print(v, pi_table[v], v / math.log(v), float(mp.li(v)))

plt.figure()
plt.plot(x, pi_x, label="pi(x)")
plt.plot(x, x_over_log_x, label="x/log(x)")
plt.plot(x, li_x, label="li(x)")
plt.xscale("log")
plt.xlabel("x (log scale)")
plt.ylabel("count / approximation")
plt.title("Prime counting and asymptotic approximations")
plt.legend()
plt.tight_layout()
plt.show()
