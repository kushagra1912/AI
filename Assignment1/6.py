sal = int(input())

if sal <= 10000:
    print(sal+sal*0.2+sal*0.8)
elif sal <= 20000:
    print(sal+sal*0.25+sal*0.9)
elif sal > 20000:
    print(sal+sal*0.3+sal*0.95)