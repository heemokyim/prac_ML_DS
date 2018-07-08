# lambda
def f(x, y):
    return x + y

print(f(1, 4))

f_lamda = lambda x, y: x + y
print(f_lamda(7, 9))


# map & reduce
ex = [1, 2, 3, 4, 5]
f_l = lambda x : x ** 5
print(list(map(f_l, ex)))

f_2 = lambda x, y: x * y
print(list(map(f_2, ex, ex)))

print(
    list(map(
        lambda x: x ** 3 if x % 2 == 0 else x, # possible filter
        ex
    ))
)
# but list comprehension이 가능해 이렇게 안써도 됨
print([v ** 3 for v in ex if v % 2 == 0])


# reduce function
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

def factorial(n):
    return reduce(
        lambda x, y: x * y,
        range(1, n+1)
    )

print(factorial(10))