"""3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки. """

for i in range(21):
    x = str(i)
    if int(x[-1]) == 1 and int(x) !=11:
        print('{} процент'.format(x))
    elif 2 <= int(x[-1]) <= 4 and int(x) < 10:
        print('{} процента' .format(x))
    else:
        print('{} процентов' .format(x))

