T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # D = 두 열차 사이의 거리
    # A = A 기차의 속력
    # B = B 기차의 속력
    # F = 파리의 속력

    # 두 열차가 만날때까지 시간은?
    # A * time + B * time == D
    # time은?
    time = D / (A+B)
    answer = time * F
    print(f'#{tc} {answer}')