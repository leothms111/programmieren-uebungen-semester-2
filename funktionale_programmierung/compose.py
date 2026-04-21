def compose(g, f, x):
    return f(g(x))

def increment(x):
    return x + 1

def square(x):
    return x**2

print(compose(increment, square, 2))
print(compose(square, increment, 2))