import random
import math
import matplotlib.pyplot as plt
import time

N, omega, n = 256, 1100, 8

t = [i for i in range(N)]

time_start = time.time()

# count x(t)
res = []
for i in range(n):
    A = random.random()
    fi = random.random() * 6.28
    res_i = [A * math.sin(omega * t[j] * j + fi) for j in range(N)]
    res.append(res_i)
x_t = []
for i in range(N):
    x = 0
    for j in range(n):
        x += res[j][i]
    x_t.append(x)


# count m
def count_m_x(x_t):
    m_x = 0
    for i in range(len(x_t)):
        m_x += x_t[i]
    return m_x / N


# count D
def count_d_x(x_t):
    m_x = count_m_x(x_t)
    d_x = 0
    for i in range(len(x_t)):
        d_x += (x_t[i] - m_x) ** 2
    return d_x / N


time_end = time.time()
plt.plot(t, x_t)
plt.xlabel('x(t) = sum(Asin(wt+f))')
plt.grid(True)
plt.show()

m_x = count_m_x(x_t)
d_x = count_d_x(x_t)
print('M =', m_x, '\nD =', d_x)
print('Час виконання:', time_end - time_start)
