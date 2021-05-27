"""1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration..."""

def nums_gen(max_num):
    for x in range(1,max_num + 1,2):
        yield x

max_num = int(input('Введите число: '))
print(*nums_gen(max_num), sep='\n')
print('...StopIteration...')
