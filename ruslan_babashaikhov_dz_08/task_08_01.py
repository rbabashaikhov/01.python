import re
def email_parse(email_address):
    email_pattern = re.compile(r'(?P<key>[A-z0-9]+)@(?P<val>[A-z0-9]+\.[A-z]+)')
    if dict(*map(lambda x: x.groupdict(), email_pattern.finditer(email_address))):
        print(dict(*map(lambda x: x.groupdict(), email_pattern.finditer(email_address))))
    else:
        raise ValueError(f'wrong email: {email_address}')

email_parse('pochta@yandex.ru')