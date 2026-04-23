from random import randint

def quick_sort(lst:list)->None:
    if len(lst)<=1:
        return lst

    pivot = lst[-1]
    smaller_nums = [num for num in lst[:-1] if num<=pivot]
    bigger_nums = [num for num in lst[:-1] if num>pivot]

    print(smaller_nums, pivot, bigger_nums)
    sorted_list = quick_sort(smaller_nums) + [pivot] + quick_sort(bigger_nums)
    return sorted_list


my_lst = [randint(1,100) for i in range(50)]
print(my_lst)
sorted_list = quick_sort(my_lst)
print(sorted_list)
