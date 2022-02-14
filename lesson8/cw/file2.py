# словари (dict)

user = {"user1" : "player", "user2" : "admin", "user3" : "zabanen"}
#dict = {"key" : "value"}
print(user)
print(user["user1"])
user["user4"] = "zxc" ## добавление
user["user1"] = "player 2-0"
print(user)


massiv = {'x' : 0, 'y' : 25, 'spped' : 'medium'}
print(f"оригинальная позиция-X игрока --> {massiv['x']}")

if massiv["spped"] == "slow":
    x_inc = 1
elif massiv["spped"] == "medium":
    x_inc = 2
else :
    x_inc = 3

massiv["x"] += x_inc


del user["user4"]
print(user)


#####


lang = {
    'Sanchoz' : "JavaScript",
    'Makson' : 'Python',
    'Bogdan' : 'C++',
    'Mary' : 'PhP'
}

for i, j in lang.items():
    print(f"Я, {i}, люблю язык програмирования --> {j}")