from collections import deque
 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
 
types = {
    # 상하좌우 순서로 기록
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}
 
def bfs(R, C):
    q = deque([(R, C)])  # 후보군
    visited[R][C] = 1  # 출발점 초기화
 
    while q:  # 후보군이 없을 때 까지(더 이상 방문할 수 있는 곳이 없으면 종료)
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]
 
        for dir in range(4):  # 상하좌우 확인
            # 출구가 없으면 다음 방향 확인 (continue)
            if dirs[dir] == 0:
                continue
 
            # 다음 좌표
            new_y = now_y + dy[dir]
            new_x = now_x + dx[dir]
 
            # 범위 밖이면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue
 
            # 못가는 못이면 pass
            if graph[new_y][new_x] == 0:
                continue
 
            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue
 
            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]
 
            # 현재 상좌 -> next_dirs가 하우 가 안뚫렸으면 못간다
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue
 
            # 현재 하우 -> next_dirs의 상좌 가 안뚫렸으면 못간다
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue
 
            # L 시간 이후는 볼 필요 없다
            if visited[now_y][now_x] + 1 > L:
                continue
 
            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는 지 기록
    visited = [[0] * M for _ in range(N)]
 
    bfs(R, C)
    cnt = 0
    # L 시간 이하로 방문한 모든 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
 
    print(f'#{tc} {cnt}')