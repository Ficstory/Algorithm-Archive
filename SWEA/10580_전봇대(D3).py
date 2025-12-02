T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]
 
    cross_count = 0      
    for i, j in line:
        for k in range(N):
            if line[k][0] > i and line[k][1] < j: 
                cross_count += 1
            elif line[k][0] < i and line[k][1] > j:
                cross_count += 1
     
    print(f'#{tc} {int(cross_count/2)}')