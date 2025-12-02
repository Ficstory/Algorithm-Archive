T = int(input())
 
 
def cooking(idx, current_taste, calory):
    global max_taste
 
    # 1. 종료 조건
    if calory > L:
        return
 
    if idx == N:
        # 칼로리가 제한 이하여야만 도달하며, 여기서 최대값을 갱신
        max_taste = max(max_taste, current_taste)
        return
 
    # 2. 재귀 탐색
 
    # A. 현재 재료(idx)를 선택하는 경우
    # 다음 탐색은 idx+1 재료로 이동
    cooking(idx + 1, current_taste + food[idx][0], calory + food[idx][1])
 
    # B. 현재 재료(idx)를 선택하지 않는 경우
    # 다음 탐색은 idx+1 재료로 이동
    cooking(idx + 1, current_taste, calory)
 
for tc in range(1, T+1):
    N, L = map(int,input().split())
    # 총 재료의 수, 제한 칼로리
    food = [list(map(int, input().split())) for _ in range(N)]
    calorys = []
    for i in range(N):
        calorys.append(food[i][1])
 
    max_taste = 0
    visited = [False] * N
    cooking(0,0,0)
    print(f'#{tc} {max_taste}')