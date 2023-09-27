T=int(input())
while(T!=0):
    digit=input()
    loop=len(digit)
    numberList=[]
    number=int(digit)
    while(loop!=0):
        divide=number%10
        number=number//10
        numberList.append(divide)
        loop=loop-1
    T=T-1
    for x in numberList:
        print(x, end=' ')
    print()
   
    # print(" ".join(digits), end=' ')
    




