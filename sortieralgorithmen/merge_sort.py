from random import randint

def merge_sort(lst:list)->None:
    if len(lst)<=1:
        return lst
    
    # liste in zwei Teile teilen
    mid = len(lst)//2
    right_side = lst[mid:]
    left_side = lst[:mid]
    print(left_side, right_side)

    # teillisten sortieren (rekursiv)
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    # teillisten in neuer liste zusammensetzen
    sorted_list = [ ]
    i = 0
    j = 0
    while i < len(right_side) and j<len(left_side):
        if left_side[j] > right_side[i]:
            sorted_list.append(right_side[i]) 
            i += 1
        elif left_side[j] <= right_side[i]:
            sorted_list.append(left_side[j])
            j +=1

    # entweder linke seite oder rechte seite ist schon vollständig hinzugefügt -> diese wird nicht angehänt (deshalb kann man beide aufrufen)
    # die linke und rechte hälfte an sich sind bereits sortiert
    sorted_list.extend(right_side[i:])
    sorted_list.extend(left_side[j:])
    return sorted_list


my_lst = [6,8,5,9,0,3,2,1,4]
print(my_lst)
sorted_list = merge_sort(my_lst)
print(sorted_list)