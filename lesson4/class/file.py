### 

print("Найти функцию f(x) = x^2")
x = 1
while x <= 10:
    y = x**2
    print(f"Число {x}, квадрат равен {y}")
    x += 1

###

print("S = 1 + 2 + 3 +....+ n")
n = int(input("Введите число: "))
Sum = 0
x = 1
while x<=n:
    Sum+=x
    x+=1
print(Sum)

###

print("Sum = 1/2 + 1/4 + 1/8 +...+ 1/n")
n= int(input("введите количество слагаемых"))
Sum = 0
i = 1
a = 1/2
while i<=n:
    Sum += a
    i += 1
    a /= 2
print(Sum)