def block_generator(start, end, lenght):
    current = start
    while current <= end:
        stop = min(current + lenght, end + 1)
        yield list(range(current, stop))
        current = stop

def call_block_generator():
    block = block_generator(1,10,4)
    print(next(block))
    print(next(block))

