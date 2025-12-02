def calculate_taste(team):
    taste = 0
    # 팀에 속한 멤버가 2명 이상일 때만 시너지 계산
    if len(team) > 1:
        # 모든 멤버 쌍(i, j)에 대해 시너지를 더함
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                member1 = team[i]
                member2 = team[j]
                taste += arr[member1][member2] + arr[member2][member1]
    return taste
 
# N/2명의 팀원을 뽑아 맛의 차이를 계산하는 재귀 함수
def find_diff(member_count, start_index, team_A):
    global min_diff
 
    # 기저 조건: A팀 구성이 완료되었을 때
    if member_count == N // 2:
        # B팀 구성하기 (전체 재료에서 A팀 재료를 제외)
        team_B = []
        for i in range(N):
            if i not in team_A:
                team_B.append(i)
 
        # 각 팀의 맛 계산
        taste_A = calculate_taste(team_A)
        taste_B = calculate_taste(team_B)
 
        # 맛의 차이를 구하고 최솟값 갱신
        diff = abs(taste_A - taste_B)
        min_diff = min(min_diff, diff)
        return
 
    # 재귀 호출: 조합 생성
    for i in range(start_index, N):
        team_A.append(i)
        find_diff(member_count + 1, i + 1, team_A)
        team_A.pop() # 백트래킹: 다음 조합을 위해 마지막에 추가한 멤버 제외
 
 
# --- 메인 실행 부분 ---
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    min_diff = float('inf') # 최솟값을 매우 큰 수로 초기화
 
    find_diff(0, 0, [])
 
    print(f'#{tc} {min_diff}')