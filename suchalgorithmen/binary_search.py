def binary(lst:list, target)->int:
    untere_grenze = 0
    obere_grenze = len(lst)-1

    while untere_grenze <= obere_grenze:
        mid = (untere_grenze+obere_grenze)//2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            obere_grenze = mid -1
        else: 
            untere_grenze = mid +1
    return -1

def binary_recursive(lst, target, obere_grenze=len(lst)-1, untere_grenze=0):
    mid = (untere_grenze+obere_grenze)//2
    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_recursive(lst, target,mid-1, untere_grenze)
    else:
        return binary_recursive(lst, target,obere_grenze, mid+1)

lst = [i for i in range(0,100,2)]
print(lst)
res = binary(lst, 90)
res2 = binary_recursive(lst, 90, len(lst)-1, 0)
print(res, res2)