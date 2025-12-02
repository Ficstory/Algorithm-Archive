T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
 
 
    max_val = 0
 
    if N < M:
        # 일단 ai의 길이가 bj의 길이보다 짧으면 ai가 움직이면서 곱을 정해야함
 
        for i in range(M-N+1):
            # 반복문으로 인덱스끼리 더함
            current_val = 0
            for j in range(N):
                current_val += ai[j] * bj[i+j]
            if max_val < current_val:
                max_val = current_val
     
    elif N > M:
        # 일단 ai의 길이가 bj의 길이보다 길면 bj가 움직이면서 곱을 정해야함
 
        for i in range(N-M+1):
            # 반복문으로 인덱스끼리 더함
            current_val = 0
            for j in range(M):
                current_val += bj[j] * ai[i+j]
            if max_val < current_val:
                max_val = current_val
     
    elif N == M :
        current_val = 0
        for i in range(M):
            current_val += ai[i] * bj[i]
            if max_val < current_val:
                max_val = current_val
 
    print(f'#{tc} {max_val}')