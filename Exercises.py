




"""
# Fibonacci
def fib(n):
    a, b = 0, 1

    if n == 1:
        print(a)
    else:
        print(a, end=' ')
        print(b, end=' ')

    for i in range(2, n):
        c = b + b
        a = b
        b = c
        print(c, end=" ")

print(fib(10))

'''
def fib(n):
    if n <= 2:
        return n
    else:
        return (fib(n-1) + fib(n-2))
    
print(fib(10))
'''