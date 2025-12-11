# idx = 직원의 번호
# selec_work = 이미 골랐던 일은 다시 안고르도록 저장할 리스트
# persent 누적 확률

def work(idx, selec_work, percent):
    global max_percent
    # 전역변수 설정
    if percent <= max_percent:
        return 
    # 확률이 기존 최댓값보다 작으면 쳐내고

    if idx == N:
        if max_percent < percent:
            max_percent = percent
        return
    # 종료조건 : 직원인덱스가 3이 되면 종료

    for i in range(N):
        if i not in selec_work:
            # 골랐던 일거리가 아닐때
            new_percent = percent * (arr[idx][i]/100.0)
            # 확률 누적
            selec_work.append(i)
            work(idx+1, selec_work, new_percent)
            # 재귀호출 인덱스 +1, 골랐던 일, 누적 확률
            selec_work.pop()
            # 다른거 고르기 위해 골랐던 마지막거 없애주고
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # i 인덱스는 직원의 번호 j인덱스는 일 번호
    max_percent = 0.0
    # 최댓값 받아줄 변수 설정
    work(0,[],1.0)
    # 함수 호출
    print(f'#{tc} {(max_percent) * 100:.6f}')
    # 소수점 7자리에서 반올림하여 출력