import math

def Evc(a, b):
    if b>a:
        c = a
        a = b
        b = c
    while b!=0:
        c = a % b
        a = b
        b = c
    return a

def Evcr(ax, b):
    AX = ax
    B = b
    if b>ax:
        c = ax
        ax = b
        b = c
    x = [1, 0]
    y = [0, 1]
    a = [ax, b]
    while a[1] != 0:
        q = a[0] // a[1]
        c = a[0]
        a[0] = a[1]
        a[1] = c - a[1]*q
        c = x[0]
        x[0] = x[1]
        x[1] = c - x[1]*q
        c = y[0]
        y[0] = y[1]
        y[1] = c - y[1]*q
    if B > AX:
        result = [y[0], x[0]]
    else:
        result = [x[0], y[0]]
    return result

def Euler(x):
    A = []
    for i in range(2, int(x**(math.sqrt(1/2)))):
        if x % i != 0:
            continue
        k = 0
        while x % i == 0:
            x = x//i
            k += 1
        A.append([i,k])
    p = 1
    for i in range(len(A)):
        p = p*(A[i][0]**A[i][1] - A[i][0]**(A[i][1] - 1))

    return p

def L(a,p):
    if a % p == 0:
        return 0
    if a**((p-1)/2) % p == 1:
        return 1
    else:
        return -1
    
def J(a, m):
    A = []
    P = 1
    for i in range(2, int(math.sqrt(m))):
        if a % i != 0:
            continue
        k = 0
        while a % i == 0:
            a = a//i
            k += 1
        P = P*(L(a,i))**k
        A.append([i,k])
    return P

#print(J(119, 45))
while 1==1:
    print('Для вычисления НОДа введите 1')
    print('Для получения линейного представления 2')
    print('Для вычисления функции Эйлера введите 3')
    print('Для вычисления символа Лежандра введите 4')
    print('Для вычисления символа Якоби введите 5')
    h = int(input())
    if h == 1:
        print('Введите число a')
        a = int(input())
        print('Введите число b')
        b = int(input())
        print('НОД:',Evc(a, b))
        print('\n')
    elif h == 2:
        print('Введите число a')
        a = int(input())
        print('Введите число b')
        b = int(input())
        r = Evcr(a,b)
        print('Линейное представление:', Evc(a,b),'=',a,'*','(',r[0],')','+',b,'*','(',r[1],')')
        print('\n')
    elif h == 3:
        print('Введите число')
        x = int(input())
        print('Значение функции Эйлера',Euler(x))
        print('\n')
    elif h == 4:
        print('Введите число')
        a = int(input())
        print('Введите модуль p')
        p = int(input())
        print('L(',a,',',p,')=',L(a,p))
        print('\n')
    elif h == 5:
        print('Введите число a')
        a = int(input())
        print('Введите нечетный модуль m')
        m = int(input())
        print('J(',a,',',m,')=',J(a,m))
        print('\n')



