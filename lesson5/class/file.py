# бесконечный цикл

while True :
    name = input("введите ваше имя(введите  <остановить> чтобы остановить)")
    print("Привет", name, ", рад тебя видеть!")
    if name == "остановить":
        break

#

for i in range(1, 10) :  #вывод 10 цифр
    print(i)


#

ARR = {1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10}
for x in range(ARR):
    print(f"{x} --> {x^2}")