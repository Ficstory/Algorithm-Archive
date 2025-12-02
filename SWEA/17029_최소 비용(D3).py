from heapq import heappop,heappush
 
T = int(input())
def dijkstra():
 
    heap = []
 
    heappush(heap,(0,0,0))
 
    D[0][0] = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
 
    while heap:
        fuel, i, j = heappop(heap)
        if fuel > D[i][j]:
            continue
 
        for c in range(4):
            nr, nc = i+di[c], j+dj[c]
            if 0 <= nr < N and 0 <= nc < N :
                if arr[nr][nc] > arr[i][j] :
                    extra_fuel = arr[nr][nc] - arr[i][j]
                    new_fuel = fuel + 1 + extra_fuel
                else:
                    new_fuel = fuel + 1
 
                if new_fuel < D[nr][nc]:
                    D[nr][nc] = new_fuel
                    heappush(heap, (new_fuel, nr, nc))
 
    return D[N-1][N-1]
 
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    D = [[INF] * (N) for _ in range(N)]
    answer = dijkstra()
    print(f'#{tc} {answer}')