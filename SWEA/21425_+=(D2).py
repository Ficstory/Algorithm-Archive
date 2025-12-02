"""
C, C++, Python, Java 등의 언어에는 += 연산자가 있다.
정수형 변수 x, y가 있을 때 “x += y”를 하면 x에 저장된 값이
(기존에 x에 저장되어 있던 값) + (기존에 y에 저장되어 있던 값)으로 바뀐다.
 
현재 x에 저장된 값은 A, y에 저장된 값은 B이다.
당신은 “x += y” 또는 “y += x” 연산을 원하는 순서대로 원하는 만큼 수행하여,
 x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하려고 한다.
 연산을 합쳐서 최소 몇 번 수행해야 하는지 계산하는 프로그램을 작성하라.
 
"""
 
T = int(input())
for tc in range(1, T+1):
    A, B, N = map(int,input().split())
    cnt = 0
    if A >= B :
        # 아니 왓다갓다 해야하는데..
        while True:
            cnt += 1
            B += A
            if B > N:
                break
            cnt += 1
            A += B
            if A > N:
                break
    elif B > A :
        while True:
            cnt += 1
            A += B
            if A > N:
                break
            cnt += 1
            B += A
            if B > N:
                break
 
    print(cnt)