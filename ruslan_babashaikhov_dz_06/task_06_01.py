"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""

lines_list = []
with open('nginx_logs.txt','r',encoding='utf-8',errors='ignore') as f:
    for line in f:
        lines_list.append((line.split(' ')[0], line.split('"')[1].split(' ')[0], line.split('"')[1].split('"')[0].split(' ')[1]))
print(lines_list)