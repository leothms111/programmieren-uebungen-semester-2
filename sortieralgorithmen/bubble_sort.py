from random import randint

def bubble_sort(lst:list)->None:
    changed = True
    while changed:
        changed = False
        for i in range(len(lst)-1):
            j = i+1
            if lst[i]>lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
                changed = True


my_lst = [randint(1,9) for i in range(10)]
print(my_lst)
bubble_sort(my_lst)
print(my_lst)