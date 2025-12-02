# heapq에 가중치를 기준으로 원소를 삽입 or 제거
from heapq import heappop, heappush
 
# start : 시작 정점 번호
def prim(start):
    # 우선순위큐(최소힙)
    heap = []
    # 중복체크배열
    # MST[i] = 1 : i번 정점은 MST에 포함(이전에 골랐음)
    # MST[i] = 0 : i번 정점은 MST에 미포함(이전에 고른적없음)
    MST = [0] * (V+1)
 
    # 최소 비용
    min_w = 0
 
    # 정점을 선택한 횟수
    v_cnt = 0
 
    # 힙에 시작정점을 추가하고 반복 시작
    # (가중치, 정점번호) 형태로 힙에 추가, 이때 힙의 우선순위 선정 기준은 튜플의 첫번째 원소, 시작정점은 가중치 0
    heappush(heap, (0, start))
 
    # 선택한 정점의 개수가 V보다 작으면 아직 신장트리 완성X
    # 큐안에 뭔가 남아 있어야 남아있는 가중치중에 작은거 선택
    while v_cnt < V+1 and heap:
        # w : 가중치(힙안에서 최소였던)
        # v : 정점번호
        w, v = heappop(heap)
 
        # 내가 이전에 v번 정점을 선택한적이 있다면
        if MST[v]:
            # 건너뜀
            continue
 
        # v가 이전에 선택한적 없는 정점 번호라면 MST에 추가
        MST[v] = 1
        # 가중치 합 누적
        min_w += w
        # 선택횟수 + 1
        v_cnt += 1
 
        # v를 새로 MST에 추가했으니
        # v에서 새로 갈수 있는 정점들의 정보도 heap에 추가
        for nv, nw in g[v]:
            # nv : v에서 갈수 있는 정점 번호
            # nw : 그 가중치
 
            # nv정점을 이전에 고른적 있으면 건너뛴다.
            if MST[nv] == 1:
                continue
 
            # v => nv 로 가는 간선 정보 추가
            # 이때 가중치는 nw
            heappush(heap, (nw, nv))
 
    # while이 종료되면 최소신장트리 완성
    return min_w
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    # V : 정점의 개수
    # E : 간선의 개수
 
    g = [[] for _ in range(V+1)]  # 인접리스트
    for i in range(E):
        s, e, w = map(int, input().split())
        g[s].append((e, w))
        g[e].append((s, w))
 
    anwser = prim(1)
    print(f'#{tc} {anwser}')