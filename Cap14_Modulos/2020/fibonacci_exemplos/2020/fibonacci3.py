def fib2(n):
    'Return a list containing  the Fibonacci series up to n.'
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


x = fib2(100)
print(x)
print(fib2.__doc__)