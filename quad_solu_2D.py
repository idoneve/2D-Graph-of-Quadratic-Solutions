import matplotlib.pyplot as plt
import numpy as np

n = 20

def quadratic(a, b, c):
    square = (b ** 2) - (4 * a * c)
    root = (square ** 0.5) / (2 * a)
    answer = (-b) / (2 * a)
    return [np.round(answer + root, 3), np.round(answer - root, 3)]

for a in range(1, n): # -1 +- sqrt(1 - 4a) / 2a
    if a % 10 == 0: print(a)
    for b in range(1, n + 10): # -b +- sqrt(b^2 - 4) / 2
        for c in range(1, n): # -1 +- sqrt(1 - 4c) / 2
            answer = quadratic(a, b, c)
            plt.plot(answer[0], answer[1], marker='o', label=answer)
            
plt.grid()
plt.show()
