"""3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?"""

def thesaurus(*names):
    result = {}
    for name in names:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))