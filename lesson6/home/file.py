## Task 1
fr = ['Maks', 'Gepa', 'Geoegiy', 'Danya']
lenght = len(fr)
for i in range(0,lenght):
    print(fr[i])

## Task 2
for i in range(0, lenght):
    print(f"Абвгдеё {fr[i]}")

## Task 3
car = ['Ford', 'BMW', 'Audi', 'Reno']
print(f"Я бы хотел машину {car[2]}")

## Task 4
gosti = ['Papich', 'KanyeWest', 'KanyeEast', 'BarakObama', 'FreddieMercury']
for i in range(0, len(gosti)):
    print(f"Приглашаю тебя, {gosti[i]}")

## Task 5
for i in range(0, len(gosti)):
    print(f"Приглашаю тебя, {gosti[i]}")
print(f"{gosti[3]} не сможет прийти(")
gosti[3] = 'DonaldTrump'
for i in range(0, len(gosti)):
    print(f"Приглашаю тебя, {gosti[i]}")

## Task 6
print("У нас появилось 3 новых гостя")
gosti.insert(0, 'JoeBiden')
gosti.insert(2, 'Valera')
gosti.append('Abdurozik')
for i in range(0, len(gosti)):
    print(f"Приглашаю тебя, {gosti[i]}")

## Task 7
print("К сожалению, остаться могут только 2 гостя")
while len(gosti) > 2:
    print(f"{gosti[0]} мы вынуждены убрать вас из списка")
    gosti.pop(0)
print(f"{gosti[0]} и {gosti[1]} -- вы остались в списке")
del gosti[0]
del gosti[0]
print(gosti)