"""3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем
 в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def result_function():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield (None, klasses[i])
            i+=1
            j+=1
            break
        else:
            yield (tutors[j], klasses[i])
            i += 1
            j += 1

for res in result_function():
    print (res)
