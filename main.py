def standard(A):
    global a
    global b
    global c
    global p
    global q

    plus1 = A.index("+")        # '+'기호의 위치를 찾음
    plus2 = A.index("+", plus1+1)

    a = A[:plus1-3]
    if a == "":     # 이차항의 계수가 1이라서 생략되어 있을 때 이차항의
        a = 1       # 계수 변수인 a를 1로 설정해주는 코드
        a1 = ""  
    else :
        a = int(a) 
        a1 = str(a)        # 이차항의 계수 a


    b = int(A[plus1+1:plus2-1])      # 일차항의 계수 b
    c = int(A[plus2+1:])         # 상수항의 계수 c


    p = float((-1)*(b/(2*a)))
    if (-1)*p >= 0 :
        p1 = "+" + str((-1)*p)    # p가 음수일 때
    else :
        p1 = str((-1)*p)    # p가 양수일 때

    q = float((-1)*((b**2)/(4*a)) + c)
    if q >= 0 :
        q1 = "+" + str(q)
    else :
        q1 = str(q)


    A_s = a1 + "(x"+ p1 + ")^2" + q1        # f(x) = a(x-p)^2 + q
    print(A_s)
    print(f"꼭짓점 : ({p},{q})")


standard("x^2+-2x+1")


def cal(x) :        # 계산해주는 함수
    return a*(x**2) + b*x + c


def maxmin(m,n) :       # m < x < n 일 때 최대최소를 구해주는 함수
    if a > 0 :
        if m<=p<=n :
            min = q
            if p-m > n-p :
                max = cal(m)
            else :
                max = cal(n)
        elif p < m :
            min = cal(m)
            max = cal(n)
        elif p < n :
            min = cal(n)
            max = cal(m)