def calculate_s(x, N):
    s=0
    for i in range(0, N+1, 2):
        s+=x**i
    return s-1
X, N=map(int, input().split())

result=calculate_s(X, N)
print(result)
