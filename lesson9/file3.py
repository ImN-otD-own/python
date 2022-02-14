people = {1 : 'Oleg',2 :'', 3 : 'Sasha', 4 : 'Muhammad', 5 : '', 6 : 'Pasha', 7 : 'Gosha', 8 : ''}
for i, j in people.items() :
    if people[i] == '':
        print(f"Поздравляем, всех!")
    else :
        print(f"Поздравляем, {j}")