# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
    

# N=int(input())
# for i in range(1, N+1):
#     print(fib(i), end=" ")


# Function to calculate the Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]  

    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


N = int(input())

fib_sequence = fibonacci(N)
for num in fib_sequence:
    print(num, end=" ")

