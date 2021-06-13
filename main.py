def standard(A):        # 표준형으로 바꿔주는 함수
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
    print("표준형 : " + A_s)
    print(f"꼭짓점 : ({p},{q})")




def cal(x) :        # 계산해주는 함수
    return a*(float(x)**2) + b*float(x) + c




def maxmin(m,n) :       # m ≤ x ≤ n 일 때 최대최소를 구해주는 함수
    if a > 0 :
        if float(m)<=p and p<=float(n) :
            min = q
            if p-float(m) > float(n)-p :
                max = cal(m)
            else :
                max = cal(n)
        elif p < float(m) :
            min = cal(m)
            max = cal(n)
        elif p > float(n) :
            min = cal(n)
            max = cal(m)
    if a < 0 :
        if float(m)<=p and p<=float(n) :
            max = q
            if p-float(m) > float(n)-p :
                min = cal(m)
            else :
                min = cal(n)
        elif p < float(m) :
            max = cal(m)
            min = cal(n)
        elif p > float(n) :
            max = cal(n)
            min = cal(m)
    print(f"최솟값 : {min}, 최댓값 : {max}")



A = input("f(x)를 입력하시오.")
B = input("x의 범위를 입력하시오. (예 : m ≤ x ≤ n 이면 m,n 을 입력)")
m = B[:B.index(",")]
n = B[B.index(",")+1:]
standard(A)
maxmin(m,n)