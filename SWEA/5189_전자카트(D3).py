"""
골프장 관리를 위해 전기 카트로 사무실에서
출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고
 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며,
 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나
통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며
각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
"""

def solve(room, idx, plus):
    global min_sum
    if plus >= min_sum:
        return
    if idx == N:
        total_plus = plus + arr[room][0]
        if total_plus < min_sum:
            min_sum = total_plus

    for i in range(1, N):
        if visited[i] == False:
            visited[i] = True
            solve(i, idx+1, plus+arr[room][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999999999999
    visited = [False] * N
    visited[0] = True
    solve(0,1, 0)

    print(f'#{tc} {min_sum}')