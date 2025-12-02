# 미리 팩토리얼과 2의 거듭제곱을 계산해둡니다. (N <= 9)
fact = [1] * 10
pow2 = [1] * 10
for i in range(1, 10):
    fact[i] = fact[i-1] * i
    pow2[i] = pow2[i-1] * 2
 
def solve (idx, left_scale, right_scale, remaining_sum):
    global cnt
    # 새로운 가지치기 조건
    # 남은 추를 모두 오른쪽에 올려도 왼쪽이 더 무거우면,
    # 남은 추들에 대한 모든 경우의 수를 한번에 계산하고 종료한다.
    if left_scale >= right_scale + remaining_sum:
        remaining_count = N - idx
        cnt += pow2[remaining_count] * fact[remaining_count]
        return
 
    # 종료조건 : 모든 무게추를 다올렸을 때
    # 가지 쳐내지지 않고 다올리는거 성공하면 카운트 1
    if idx == N:
        cnt +=1
        return
     
    for i in range(N):
        if not visited[i]:
            # i번째 무게추를 아직 사용하지 않았다면
            # i번째 무게추를 사용했다고 표시
            visited[i] = True             
            solve(idx+1, left_scale+weights[i], right_scale,  remaining_sum - weights[i])
            # 가지치기 : 오른쪽이 높아지면 쳐냄
            if right_scale + weights[i] <= left_scale:
                solve(idx+1, left_scale, right_scale + weights[i],  remaining_sum - weights[i])
            visited[i] = False
        # 백트래킹 : 다음 반복 전에 방문횟수 초기화
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int,input().split()))
 
    # 남은 추의 총합을 계산하기 위해 전체 합을 미리 구해둠
    total_sum = sum(weights)
 
    cnt = 0
    visited = [False] * N
     
    solve(0, 0, 0, total_sum)
 
    print(f'#{tc} {cnt}')