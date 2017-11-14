import math as math
import sys as sys
import numpy as np

inputFile = open("input.txt", 'r')

p, q, e, P = inputFile.readline().strip().split(" ")
p, q, e, P = int(p), int(q), int(e), int(P)


# Проверка на "простоту" чисел p и q
def isProst(x):
    if x == 1:
        return True
    for i in range(2, x - 1):
        if not x % i:
            return False
    return True


if (isProst(p) == True) and (isProst(q) == True):
    N = p * q

elif not isProst(p):
    print("Число p = " + str(p) + " не является простым")

elif not isProst(q):
    print("Число q = " + str(q) + " не является простым")

# Сравнение на простоту выбранного числа e с Fore
ForE = (p - 1) * (q - 1) * (p + 1) * (q + 1)
if (math.gcd(ForE, e)) != 1:
    print(
        "Выбранное число e = " + str(e) + " не является взаимнопростым с ForE = (p-1)*(q-1)*(p+1)*(q+1) = " + str(ForE))

# Параметр D для вычисления символа Лежандра
D = P * P - 4


# Функция для вычисления символа Лежандра
def Legendre(q, a, p):
    if (a == 0):
        return 0
    if (a == p):
        return 0
    if (a == -p):
        return 0
    if (a < 0):
        return 1
    if a != 1:
        t, J2P, q1 = 1, 1, 0
        if (a > p):
            a = a % p
        # Частные случаи Якоби
        if a == 1:
            return q
        if a == 2:
            return q * pow(-1, (p * p - 1) // 8)
        if a % 2 == 0:
            while (a // pow(2, t)) % 2 == 0:
                t += 1
            a = a // pow(2, t)
            if t % 2 != 0:
                J2P = pow(-1, (p * p - 1) // 8)
        q1 = (pow(-1, ((p - 1) // 2) * ((a - 1) // 2))) // J2P
        return Legendre(q * q1, p, a)
    else:
        return q


# Для вычисления функции S(N) требуется вычислить НОК
def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


SN = lcm(p - Legendre(1, D, p), q - Legendre(1, D, q))


# Вычисление закрытого ключа
def SecretKey(a, n):
    for i in range(sys.maxsize):
        if ((a * i) % n) == 1:
            return i


d = SecretKey(e, SN)


def LucasV(e, P, N):
    e += 1
    Vn = np.zeros(e)
    Vn[0] = 2
    Vn[1] = P
    i = 2
    while (i < e):
        Vn[i] = (P * Vn[i - 1] - Vn[i - 2]) % N
        i += 1
    return int(Vn[e - 1])


Encryption_Text = LucasV(e, P, N)
Decryption_Text = LucasV(d, Encryption_Text, N)


print("Выбранные два простых числа: p =", str(p) + ", q =", str(q))
print("Выбранное число e = " + str(e) + " взаимнопростое с (p-1)*(q-1)*(p+1)*(q+1) = " + str(ForE))
print("Исходное сообщение: ", str(P))
print("Открытый ключ: (", str(e) + ", " + str(N) + " )")
print("Закрытый ключ: (", str(d) + ", " + str(N) + " )")
print("Зашифрованное сообщение: ", Encryption_Text)
print("Расшифрованное сообщение: ", Decryption_Text)

# outputFile = open("output.txt", 'w')
# outputFile.write(str())
# outputFile.close()