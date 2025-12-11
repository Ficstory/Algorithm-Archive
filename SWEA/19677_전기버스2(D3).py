
def bus_battery(idx, battery, cnt):
    # 가지치기
    # 재귀 도중 중전카운트가 최솟값 보다 높아지면 쳐내
    global min_cnt
    if cnt > min_cnt:
        return
        
    # 종료조건 : 버스 위치가 N이면 종료
    if idx >= N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    
    # 재귀로 충전한다 안한다를 나눠가지고 마 구해뿌면 된다아이가
    # 충전한다
    bus_battery(idx+1, charge_spot[idx]-1, cnt+1)
    # 충전안한다
    if battery > 0:
        bus_battery(idx+1, battery-1, cnt)        

T = int(input())
for tc in range(1, T+1):
    temp_lit = list(map(int, input().split()))
    N = temp_lit[0]
    # N = 정류장 개수
    charge_spot = temp_lit[1::]
    min_cnt = 999999999
    bus_battery(1, charge_spot[0]-1, 0)

    print(f'#{tc} {min_cnt}')
