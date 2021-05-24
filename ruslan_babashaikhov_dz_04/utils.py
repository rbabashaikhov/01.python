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