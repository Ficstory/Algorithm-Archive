"""
4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
 
격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
 
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
 
단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
 
격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
 
 
[입력]
 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
 
각 테스트 케이스마다 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보가 주어진다.
"""
 
# 일단 완전탐색으로 진행하고 아무데나 지정하고 총 6번 이동하면서 각 칸의 적혀있는 숫자를 차례대로 확인
# 시작 위치를 2중 for문으로 진행할까?
T = int(input())
for tc in range(1, T+1):
 
    arr = [input().split() for _ in range(4)]
    # 일단 인풋 리스트 받아주고
    # 시작점 위치를 찾아서 넣어줄 필요는 없나? 그냥 그대로 하면되나?
    # 일단 하나씩 같은숫자가 있는지 알아보고 없다면 추가하는것
     
    result_set = set()
    def solve(start_i, start_j, current_num):  
 
        # 종료조건
        if len(current_num) == 7:
            result_set.add(current_num)
            return
         
        #가지칠게 있나..없다 
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        # 이동할 곳 찾아주는 반복문
        for k in range(4):
            s_i = start_i - di[k]
            s_j = start_j - dj[k]
 
            if 0 <= s_i < 4 and 0 <= s_j < 4:
                # 이동할 수 있다면 함수 호출
                solve(s_i, s_j, current_num + arr[s_i][s_j])
 
    for i in range(4):
        for j in range(4):
            solve(i, j, arr[i][j])
    
            # 반복문으로 좌표를 호출하고 
 
    answer = len(result_set)
    print(f'#{tc} {answer}')