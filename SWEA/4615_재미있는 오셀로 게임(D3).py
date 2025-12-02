"""
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며
보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
 
보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다.
6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).
 
4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.
 
"""
# 보드 한변의 길이 M, 돌을 놓는 횟수 M
# * N은 4, 6, 8 중 하나임
# 돌의 색이 1이면 흑 2면 백
# 만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    # 빈 보드 깔아주고
    mid = N//2
    # 초석 깔기위한 보드 중간값 구해주고
    board[mid-1][mid-1] = 2
    board[mid][mid] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1 
    # 초석 깔아주고
 
    for _ in range(M):
        w, e, stone_color = map(int,input().split())
        i_idx = e-1
        j_idx = w-1
        board[i_idx][j_idx] = stone_color
        # 돌 놔주고
        # 가로세로대각선 찾을 수 있는거 확인하는 델타배열
        di = [-1,-1,0,1,1,1,0,-1]
        dj = [0,1,1,1,0,-1,-1,-1]
        if stone_color == 1:
            # 가로, 세로, 대각선에서 뒤집을 수 있는거 찾기
            for i in range(8):
                ki = i_idx+di[i]
                kj = j_idx+dj[i]
                # 8방향 다 체크
                if 0 > ki or ki >= N or kj < 0 or kj >= N or board[ki][kj] == 0 or board[ki][kj] == stone_color :
                    # 만약에 8방향으로 보다 혹시 0보다 작거나 N보다 같거나 크거나, 0이거나 같은 돌 숫자 만나면 컨티뉴
                    continue
                elif board[ki][kj] == 2:
                    # 반대 색깔 돌을 찾으면
                    sweep = False
                    p = 1
                    change_spot = [[ki, kj]]
                    while not sweep:
                        # 뻗어나갈 변수 하나 지정
                        ci = i_idx+di[i] +(di[i] * p)
                        cj = j_idx+dj[i] +(dj[i] * p)
                        if 0 <= cj < N and 0 <= ci < N:
                            # 추가로 뻗어나가기
                            if board[ci][cj] == 2:
                                # 다른색을 만나면 더 뻗어나가기
                                change_spot.append([ci,cj])
                                p += 1
                            elif board[ci][cj] == 1:
                                # 같은색을 만나면 이제 
                                sweep = True
                                while p > 0 :
                                    board[change_spot[p-1][0]][change_spot[p-1][1]] = 1
                                    p -= 1
                            elif board[ci][cj] == 0:
                                break
                        elif 0 > ci or ci >= N or cj < 0 or cj >= N:
                            break
 
        if stone_color == 2:
            # 가로, 세로, 대각선에서 뒤집을 수 있는거 찾기
            for i in range(8):
                ki = i_idx + di[i]
                kj = j_idx + dj[i]
                # 8방향 다 체크
                if 0 > ki or ki >= N or kj < 0 or kj >= N or board[ki][kj] == 0 or board[ki][kj] == stone_color:
                    # 만약에 8방향으로 보다 혹시 0보다 작거나 N보다 같거나 크거나, 0이거나 같은 돌 숫자 만나면 컨티뉴
                    continue
                elif board[ki][kj] == 1:
                    # 반대 색깔 돌을 찾으면
                    sweep = False
                    p = 1
                    change_spot = [[ki, kj]]
                    while not sweep:
                        # 뻗어나갈 변수 하나 지정
                        ci = i_idx + di[i] + (di[i] * p)
                        cj = j_idx + dj[i] + (dj[i] * p)
                        if 0 <= cj < N and 0 <= ci < N:
                            # 추가로 뻗어나가기
                            if board[ci][cj] == 1:
                                # 다른색을 만나면 더 뻗어나가기
                                change_spot.append([ci, cj])
                                p += 1
                            elif board[ci][cj] == 2:
                                # 같은색을 만나면 이제
                                sweep = True
                                while p > 0:
                                    board[change_spot[p-1][0]][change_spot[p-1][1]] = 2
                                    p -= 1
                            elif board[ci][cj] == 0:
                                break
                        elif 0 > ci or ci >= N or cj < 0 or cj >= N:
                            break
 
    bk_cnt = 0
    wt_cnt = 0
 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bk_cnt += 1
            elif board[i][j] == 2:
                wt_cnt += 1
 
    print(f'#{tc} {bk_cnt} {wt_cnt}')               