## list ##

arr = ['Audi', 'BMW', 'Mersedes']
numbers = [3, 5, 7, 1, 10]

print(numbers) ## [3, 5, 7, 1, 10]
message = f"Я хочу машину -- {arr[1]}"  ##  = arr[-2]

arr[2] = 'Ford'

## добавление элемента ##

arr.append('Honda')    ##   .append()
arr.insert(2, 'Toyota')

## удаление ##

del arr[1]  ## или  arr.remove('BMW')

del_car = arr.pop(0)
print(del_car)

###

arr.sort()
arr.sort(reverse=True)  ## arr.reverse()

###

len(arr)