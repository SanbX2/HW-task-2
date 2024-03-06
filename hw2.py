import random

def get_numbers_ticket(min= 1, max= 1000, quantity= 1000):
    set_of_numbers = set()
    len_of_list = len(set_of_numbers)
    empty_list = []

    if min <= 0 or max > 1000 or quantity <= 0 or quantity > (max -(min-1)):
        return empty_list

    while len_of_list < quantity:
        set_of_numbers.add(random.randint(min, max))
        len_of_list = len(set_of_numbers)
        uniq_set_of_numbers = list(set_of_numbers)
        uniq_set_of_numbers.sort()

    return uniq_set_of_numbers

lottery_numbers = get_numbers_ticket(1, 50, 6)
print("Ваші лотерейні числа:", lottery_numbers)