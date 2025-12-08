T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(-N,N+1):
        for j in range(-N,N+1):
            if (i**2) + (j**2) <= N**2:
                cnt += 1  
    print(f'#{tc} {cnt}')
