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


# count correlation
m_x = count_m_x(x_t)
m_y = count_m_x(x_t)
signal_x = x_t
signal_y = x_t
tau = [i for i in range(N // 2)]
r_x_x = [(signal_x[i] - m_x) * (signal_x[2 * i] - m_x) / N / 2 for i in range(N // 2)]
r_x_y = [(signal_x[i] - m_x) * (signal_y[2 * i] - m_y) / N / 2 for i in range(N // 2)]
time_end = time.time()
plt.plot([i for i in range(N // 2)], r_x_x, label='Rxx', color='yellow')
plt.plot([i for i in range(N // 2)], r_x_y, label='Rxy', color='green')
plt.legend()
plt.grid(True)
plt.show()

print('Час виконання:', time_end - time_start)
