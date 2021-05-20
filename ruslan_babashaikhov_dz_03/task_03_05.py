"""5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?"""

def get_jokes(n):
    """функция get_jokes(n) принимает в качестве аргумента количество элементов списка шуток"""
    from random import choice
    jokes_result=[]
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i=0
    while i < n:
        jokes_item = []
        jokes_item.append(choice(nouns))
        jokes_item.append(choice(adverbs))
        jokes_item.append(choice(adjectives))
        i+=1
        jokes_string = ' '.join(jokes_item)
        jokes_result.append(jokes_string)

    return jokes_result
n = int(input('Введите желаемое количество шуток: '))
print(get_jokes(n))