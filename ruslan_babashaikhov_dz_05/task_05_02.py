def num_gen(max_num):
    return (x for x in range(1, max_num +1, 2))

odd_to_15 = num_gen(15)
print(type(odd_to_15))
print(next(odd_to_15))
print(list(odd_to_15))
print(next(odd_to_15))