T=int(input())
while(T!=0):
    x1, y2  = input().split()
    x=int(x1)
    y=int(y2)
    sum=0
    if x>y:
        for num in range(y+1,x):
            if num%2==1:
                sum+=num
        print(sum)
    if y>x:
        for num in range(x+1,y):
            if num%2==1:
                sum+=num
        print(sum)       
    T=T-1
