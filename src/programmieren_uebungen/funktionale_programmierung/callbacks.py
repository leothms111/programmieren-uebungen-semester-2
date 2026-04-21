def process_list(numbers, callback):
    transformed_nums = [number**2 for number in numbers]
    return callback(transformed_nums)

def get_sum(num_list:list[int])->int:
    return sum(num_list)

def calc_mean(num_list:list[int])->float:
    return sum(num_list)/len(num_list)

nums = [number for number in range(1,5)]
print(process_list(numbers=nums, callback=get_sum))
print(process_list(nums, calc_mean))