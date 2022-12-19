#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    ln = sum(map(lambda x: 1, my_list))
    if x <= ln:
        for i in range(x):
            try:
                int(my_list[i]) == my_list[i]
                print('{:d}'.format(my_list[i]), end='')
                count = count + 1
            except (ValueError, TypeError):
                continue
    else:
        raise IndexError
    print()
    return count
