"""1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии."""

duration = int(input('Введите число: '))
if duration < 60:
    print ('{} секунд'.format(duration))
elif duration < 3600:
    print('{} минут, {} секунд'.format(duration // 60, duration % 60))
elif duration < 86400:
    print('{} часов,{} минут, {} секунд'.format(duration // 3600, duration % 3600 // 60, round(((duration - duration // 3600 * 3600) / 60 - (duration - duration // 3600 * 3600) // 60) * 60)))


