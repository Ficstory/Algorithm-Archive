T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    turn_90 = [[0] * N for _ in range(N)]
    turn_180 = [[0] * N for _ in range(N)]
    turn_270 = [[0] * N for _ in range(N)]

    c = 0
    for j in range(N):
        d = 0
        for i in range(N-1, -1, -1):
            turn_90[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    c = 0
    for i in range(N - 1, -1, -1):
        d = 0
        for j in range(N-1, -1, -1):
            turn_180[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    c = 0
    for j in range(N - 1, -1, -1):
        d = 0
        for i in range(N):
            turn_270[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    print(f'#{tc}')
    for i in range(N):
        print(f'{"".join(map(str, turn_90[i]))} {"".join(map(str, turn_180[i]))} {"".join(map(str, turn_270[i]))}')