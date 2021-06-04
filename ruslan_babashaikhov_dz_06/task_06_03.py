def parsing(users, hobbies, result):
    users_list = []
    hobbies_list = []
    result_dict = {}

    with open(users, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        users_list = f.readlines()

    with open(hobbies, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        hobbies_list = f.readlines()

    if len(users_list) < len(hobbies_list):
        return 1

    for i in range(len(users_list)):
        if i <= len(hobbies_list) - 1:
            result_dict[(' '.join(users_list[i].replace('\n','').split(',')))] = hobbies_list[i].replace('\n','').split(',')
        else:
            result_dict[(' '.join(users_list[i].replace('\n','').split(',')))] = None

    with open(result, 'w', encoding ='utf-8') as f:
        f.write(str(result_dict))
    return 0

parsing('users.csv','hobby.csv','result.txt')

with open('result.txt', 'r', encoding ="utf-8",errors = 'ignore') as f:
    print(f.readlines())