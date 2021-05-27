"""2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов """

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


insert_list = []
insert_number = 0
for i, x in enumerate(my_list):
    if ((x.startswith('+') or x.startswith('-')) and x[1:].isdigit()):
        insert_list.append(i + insert_number)
        insert_list.append(i + insert_number + 2)
        my_list[i] = '{0}{1:02d}'.format(x[0], int(x[1:]))
        insert_number += 2
    if x.isdigit():
        insert_list.append(i + insert_number)
        insert_list.append(i + insert_number + 2)
        my_list[i] = '{:02d}'.format(int(x))
        insert_number += 2
for i in insert_list:
    my_list.insert(i, '"')
my_list = list(' '.join(my_list))
char_index = 0
for i, char in enumerate(my_list):
    if char == '"' and char_index % 2 == 0:
        my_list.pop(i + 1)
        char_index += 1
    elif char == '"' and char_index % 2 == 1:
        my_list.pop(i - 1)
print(''.join(my_list))
