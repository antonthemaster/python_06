import random


left_board = int(input('Input lesser board: '))
right_board = int(input('Input bigger board: '))

list_random = [random.randint(1, 99) for x in range(random.randint(7, 12))]
res = list()
for index, i_elem in enumerate(list_random):
    if left_board < i_elem < right_board:
        res.append(index)

print(res)
