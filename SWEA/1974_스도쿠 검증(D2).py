"""
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고,
 3 x 3 크기의 작은 격자 또한,
1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때,
위와 같이 겹치는 숫자가 없을 경우,
1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.
"""
 
T = int(input())
for tc in range(1, T + 1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
 
    # 어떻게 검사할것인가?
    # 9칸안에 1~ 9까지의 수가 다 있는가?
    # 숫자 하나씩 다 있는가?
    # 셋으로 담으면 길이가 9인가?
    # 셋으로 가자
    # 그럼 가로축으로 한번 세로축으로 한번 반복을 돌려야 겠네
 
    answer = True
 
    for i in range(9):
        path = []
        for j in range(9):
            path.append(sdoku[i][j])
            test = set(path)
        if len(test) < 9:
            answer = False
 
    for j in range(9):
        path = []
        for i in range(9):
            path.append(sdoku[i][j])
            test = set(path)
        if len(test) < 9:
            answer = False
 
    for w in range(3):
        for v in range(3):
            path = []
            for i in range(3):
                for j in range(3):
                    path.append(sdoku[3*w+i][3*v + j])
            test = set(path)
            if len(test) < 9:
                answer = False
 
    print(f'#{tc} {int(answer)}')
 
 
 
 
 
# 10
# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9