import math


def f(x):
    return 4 * math.exp(-0.5 * x) - x

# f'(x) fonksiyonu
def f_prime(x):
    return -2 * math.exp(-0.5 * x) - 1

# Başlangıç değeri x0=2 olarak verelim
x0 = 2

# 4 iterasyon için formülü uygulayalım
for i in range(4):

    x0 = x0 - f(x0) / f_prime(x0)

    print(f"Iterasyon {i+1}: x = {x0:.4f}")


print(f"f({x0:.4f}) = {f(x0):.4f}")
