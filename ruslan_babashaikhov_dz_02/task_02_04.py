
person_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for e in person_list:
    new_list = []


    i = 0
    while i < len(e.split(" "))-1:
        new_list.append(e.split(" ")[i])
        i += 1
    new_list.append(e.split(" ")[i].title())
    print(" ".join(new_list))



