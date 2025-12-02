from heapq import heappush, heappop
 
def dijkstra(start):
    heap = []
    # 빈배열 하나 만들어주고
    heappush(heap, (0,start))
 
    D[start] = 0
 
    while heap:
        w, e = heappop(heap)
        # 무게와 정점을 받아와 줍니다.
        if w > D[e]:
            continue
 
        for ne, nw in JIDO[e]:
            new_dis = w + nw
            if new_dis < D[ne]:
                D[ne] = new_dis
                heappush(heap,(new_dis,ne))
    return D[N]
 
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    JIDO = [[] for _ in range(N+1)]
    for i in range(E):
        S, V, W = map(int,input().split())
        JIDO[S].append((V,W))
 
    # 그다음에는 최솟값 찾아줄 배열
    INF = float('inf')
    D = [INF] * (N+1)
    answer = dijkstra(0)
    print(f'#{tc} {answer}')