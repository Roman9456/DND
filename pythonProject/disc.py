def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def solution(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(x1, x2)
    elif d == 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        print(x1)
    else:
        print('корней нет')
        return d


solution(1, 8, 15)
solution(1, -13, 12)
solution(-4, 28, -49)
solution(1, 1, 1)

# a = 1, b = 8, c = 15.
# a = 1, b = -13, c = 12.
# a = -4, b = 28, c = -49.
# a = 1, b = 1, c = 1.
