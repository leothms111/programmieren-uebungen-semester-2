from random import randint

def selection_sort(lst:list)->None:
    l = len(lst)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if lst[j]<lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst)


my_lst = [randint(1,9) for i in range(10)]
print(my_lst)
selection_sort(my_lst)
print(my_lst)