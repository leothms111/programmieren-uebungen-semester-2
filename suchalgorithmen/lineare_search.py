def linear_search(lst:list, target)->int:
    for i, val in enumerate(lst):
        if val == target:
            return i 
    return -1    
    

lst = [i for i in range(0,100,2)]
print(lst)
res = linear_search(lst, 5)
print(res)