def f(n):
    while True:
        if n ==1:
            return 1
        elif n % 2 == 0: #짝수
            n = n/2
        elif n % 2 == 1:
            n = 3*n + 1

def pf(n):
    while True:
        if n ==1:
            print('1')
            return 1
        elif n % 2 == 0: #짝수
            n = n/2
            print(n)
        elif n % 2 == 1:
            n = 3*n + 1
            print(n)


pf(10000)



a = int(input('Collatz conjecture'))


for i in range(a, a+1000):
    temp = f(i)
    if temp == 1:
        print(i, ' <-- 콜라즈 추측 성립')
    else:
        print('오류 발생')
        break
    
        




