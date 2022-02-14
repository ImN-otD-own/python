names = {'Alexandr Glyantsev' : '22/06/2006', 'Maksim Tverdohlebov' : '14/88/2006', 'Pavlik' : '12/04/1991'}
a = input('Введите имя ')
if names.get(a) == None :
    print("Ошибка")
else :
    print(f"Дата рождения {a} -- {names[a]}")