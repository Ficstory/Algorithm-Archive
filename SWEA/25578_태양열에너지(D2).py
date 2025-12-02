"""
N*N 크기의 태양광 판넬이 있다. 최근 날씨가 흐려서 태양광 에너지를 잘 모으지 못하게 되었다.
그래서 생각해낸 방법이 있는데 바로 M*M 크기의 렌즈를
태양광 판넬 위에 설치하여 빛을 더 집중시켜 모으는 것이다.
하지만 렌즈를 사용하면 원래 태양광 판넬의 일정부분을 잘라내야 한다.
 
5*5 크기의 태양광 판넬과 2*2 크기의 렌즈가 아래처럼 있다.
태양광 판넬의 각 칸(i,j) 에 모을수 있는 태양광 에너지의 양이 주어지고,
 렌즈의 각 칸(li,lj) 에는 해당 렌즈를 사용하면 더 모을수 있는 태양광 에너지의 양이 주어진다.
"""
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 판넬크기
    # M = 렌즈크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]
 
    answer = [[0] * (N-M+1) for _ in range(N-M+1)]
    for i in range(N-M+1):
 
        for j in range(N-M+1):
            new_energy = 0
            for e1 in range(M):
                for e2 in range(M):
                    new_energy += arr[i+e1][j+e2] + lens[e1][e2]
            answer[i][j] = new_energy
 
    # 4중 반복을 사용해서 구해야 할거같은데
 
    print(f'#{tc}')
    for raw in answer:
        print(" ".join(map(str, raw)))