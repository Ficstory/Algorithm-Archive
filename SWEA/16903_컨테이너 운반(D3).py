T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 컨테이너 수, 트럭수 
    # 예시 3, 2
    weights = list(map(int, input().split()))
    # 컨테이너 3개 1, 5, 3 짜리 무게
    trucks = list(map(int, input().split()))
    # 트럭 적재량 8, 3
    # 트럭당 하나만 갖고 갈 수 있음.
    weights.sort(reverse=True)  # [5, 3, 1]
    trucks.sort(reverse=True)   # [8, 3]
    # 내림차순
     
    max_weight = 0
    n = 0
     
    for i in range(M):
        while i+n <=N-1:
            if weights[i+n] <= trucks[i]:
                max_weight += weights[i+n]
                break
                # 1. 첫번째차가 싣고 갓다 
                # - 그럼 n이 0이 되어야함(i:0)
                # 2. 두번째차가 두번째 짐을 못실었다
                # n + 1 이 돼야함(i:1)
                # 3. 두번째차가 세번째 짐(2) n(+1)을 실었다. 
                # 4. 세번째차가 네번째짐 (3) 
            n += 1
             
 
    print(f'#{tc} {max_weight}')