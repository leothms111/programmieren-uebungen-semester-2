from typing import Callable

def add_three_nums(a)->Callable:
    def add_second_num(b)->Callable:
        def add_third_num(c)->Callable:
            return a + b+ c
        return add_third_num
    return add_second_num


summe = add_three_nums(3)(5)(1)
print(summe)


