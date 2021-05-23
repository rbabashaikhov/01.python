"""2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро."""


def currency_rates(char_code):
    import requests
    from requests import utils
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    res_dict = {}
    res_list = []
    for el in content.split('><'):
        if el.startswith('CharCode'):
            res_list.append(el[9:12])
            key = el[9:12]
        elif el.startswith('Value'):
            res_list.append(el[6:13])
            res_dict[key] = el[6:13]
    return res_dict[char_code]

char_code = input('Введите символьный код валюты: ').upper()
print(currency_rates('USD'))



