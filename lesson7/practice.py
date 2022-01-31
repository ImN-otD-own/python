import math

# Task 1

names = ['Danya', 'Zhora', 'Oleg', 'Gena', 'Max', 'Vlad']
leng = len(names)

for i in range(0, leng):
    print(names[i])

# Task 2

transport = ['Велосипед', 'Машина', 'Мотоцикл']
leng = len(transport)

for i in range(0, leng):
    print(f"Мой любимый вид транспорта это {transport[i]}")

# Task 3

years_list = [2006, 2007, 2008, 2009, 2010, 2011]
print(years_list[3])
years_list.append(2012)
print(f"Больше всего лет мне было в {years_list[-1]} году")

# Task 4

things = ['wallet', 'mirror', 'umbrella']
print(things[2].title())
print(things[2].upper())
things.pop(2)
print(things)

# Task 5

lang = ['Georgian', 'Estonian', 'Ukrainian']
print(lang[-1].lower())
print(lang[-1][::-1].title())

# Task 6

arr = ['Internet', 'Byte', 'Program']
cort = ('Internet', 'Byte', 'Program')

arr[0] = 'Phone'
#cort[0] = 'Phone'

print(arr)
print(cort)

# Task 7

langv = ['Ukrainian', 'English', 'Russian', 'Belarus', 'French', 'Italian']
print(langv)
sorted(langv)
print(langv)
langv.reverse()
print(langv)
langv.sort()
print(langv)

# Task 8

num = input("Введите числа через пробел:")
b = list(num)
temp = ' '
c = []
if b[-1] != ' ':
    b.append(' ')
for i in range(0, len(b)):
    if b[i] != ' ':
        temp += b[i]
    else :
        c.append(temp)
        temp = ' '

for i in range(0, len(c)):
    c[i] = int(c[i])
print(c)

Sum = 0
for i in range(0, len(c)):
    Sum += c[i]
print(Sum)

# Task 9

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(0 , len(a)):
    if a[i] < 5:
        print(a[i])

# Task 10

year = 2006
list = []
for i in range(0, 17):
    list.append(year)
    year += 1
print(list)