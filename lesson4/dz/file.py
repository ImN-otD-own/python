print("1234...num; num")
num = int(input("Введите целое число "))
i = 0

while num > 1: 
    i += 1
    num /= 10
print(i)