"""2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
<<<<<<< HEAD
 http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
 посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
 Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
 величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
 передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
 в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро."""


def currency_rates(char_code):

    import requests
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    result_dict ={}

    for el in r.text.split('><'):
        if el.startswith('CharCode>'):
            key = el[9:12]
        elif el.startswith('Value>'):
            result_dict[key] = el[6:13]

    return result_dict[char_code]

char_code = input('Введите код валюты: ').upper()
print(currency_rates(char_code))