def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    def __fibonacci(n_1, n_2, n):
        result = n_1 + n_2
        print(f"n: {n} n-1: {n_1} n-2: {n_2} result: {result}")
        if n == 1:
            return
        return __fibonacci(n_1=result, n_2=n_1, n=n-1)

    __fibonacci(n_1=1, n_2=0, n=n)



def test_fibonacci():
    fibonacci(5)

def test_factorial():
    res = factorial(4)
    print( res )

if __name__ == "__main__":
    #test_factorial()
    test_fibonacci()