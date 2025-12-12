"""
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 
각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 
지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면
이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
"""
# 우, 하 로만 이동할 수 있음
def solve (i_idx, j_idx, plus):
    global min_sum
    # 가지치기
    if plus >= min_sum:
        return
    # 종료조건
    if i_idx == N-1 and j_idx == N-1:
        if plus < min_sum:
            min_sum = plus
        return
    
    # 재귀호출
    # 만약에 idx i
    # 팝을 해야하나?
    di = [1,0]
    dj = [0,1]
    for i in range(2):
        ki = i_idx+di[i]
        kj = j_idx+dj[i]
        if ki <= N-1 and kj <= N-1:
            solve(ki, kj, plus+arr[ki][kj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999999999999
    solve(0,0,arr[0][0])    
    
    print(f'#{tc} {min_sum}')
