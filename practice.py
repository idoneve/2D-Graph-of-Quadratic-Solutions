import matplotlib.pyplot as plt
import numpy as np

def quadratic(a, b, c):
    square = (b ** 2) - (4 * a * c)
    root = (square ** 0.5) / (2 * a)
    answer = (-b) / (2 * a)
    return [np.round(answer + root, 3), np.round(answer - root, 3)]


# print("ax^2 + bx + c")
# a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
# l, h = -100, 100
# n = [(a * x**2) + (b * x) + c for x in range(l, h)]
# equation = f'{a}x^2 + {b}x + {c}'
# print(equation)

for a in range(1, 10): # -1 +- sqrt(1 - 4a) / 2a
    if a % 10 == 0: print(a)
    for b in range(1, 20): # -b +- sqrt(b^2 - 4) / 2
        for c in range(1, 10): # -1 +- sqrt(1 - 4c) / 2
            answer = quadratic(a, b, c)
            # print("x = ", answer)
            plt.plot(answer[0], answer[1], marker='o', label=answer)
            
# plt.plot([i for i in range(l, h)], n, label=equation)
plt.grid()
# plt.legend()
plt.show()