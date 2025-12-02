T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    # n = 점원 수
    # b = 선반 높이
 
    ky = list(map(int, input().split()))
    # 직원 키
    ky.sort()
    # 구해야할 것은 직원들의 키를 얼마나 모아야 선반높이에 도달할 수 있는가?
    
    # 방문배열
    min_tower = 99999999999999999
 
    def solve(idx, high):
        global min_tower
        # 가지치기
        if high >= min_tower:
            return
         
        if idx == N:
            if high >= B:
                # 2-2. 그리고 현재 탑이 이전에 찾은 최소 탑보다 낮은가?
                if high < min_tower:
                    min_tower = high
            return
     
        solve(idx + 1, high + ky[idx])
        solve(idx + 1, high)
                 
    solve(0, 0)
    answer = min_tower - B
    print(f'#{tc} {answer}')