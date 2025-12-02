T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_fly_cut = 0
    for i in range(N):
        for j in range(N):
            di = [-1, 1, 0, 0]
            dj = [0, 0, 1, -1]
 
            fly_cut = arr[i][j]
            for k in range(1, M):
                for c in range(4):
                    ik = i + di[c] * k
                    jk = j + dj[c] * k
                    if 0 <= ik < N and 0 <= jk < N:
                        fly_cut += arr[ik][jk]
            if fly_cut > max_fly_cut :
                max_fly_cut = fly_cut
 
            di = [-1, -1, 1, 1]
            dj = [-1, 1, 1, -1]
 
            fly_cut = arr[i][j]
            for k in range(1, M):
                for c in range(4):
                    ik = i + di[c] * k
                    jk = j + dj[c] * k
                    if 0 <= ik < N and 0 <= jk < N:
                        fly_cut += arr[ik][jk]
            if fly_cut > max_fly_cut :
                max_fly_cut = fly_cut
 
    print(f'#{tc} {max_fly_cut}')
    