num = 2

def pure_sqared(number:int):
    return number**2


def impure_squared():
    global num
    num = num*2
    print(num)


print(pure_sqared(13))

print(num)
impure_squared()
print(num)
