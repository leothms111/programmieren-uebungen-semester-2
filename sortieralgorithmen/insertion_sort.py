from random import randint

def insertion_sort(lst:list)->None:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
    
        while j>=0 and key < lst[j]:
            lst[j+1]=lst[j]
            j -= 1

        lst[j+1] = key
        print(lst)

my_lst = [randint(1,9) for i in range(10)]
print(my_lst)
insertion_sort(my_lst)
print(my_lst)
    
