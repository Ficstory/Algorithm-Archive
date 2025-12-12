"""

1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다.
모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 
부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
"""
# 조합은 순서 상관없이 몇개를 뽑는것
# 따라서 반복에 방문햇는지 안했는지 확인하고
# 반복을 시작할 처음 숫자를 정해주면 됨

def solve(selec_cnt, start, plus):
    global cnt
    if plus > K:
        return
    if selec_cnt == N:
        if plus == K:
            cnt += 1
        return
    # 종료조건
    for i in range(start, 12):
        solve(selec_cnt+1, i+1, plus+A[i])
           

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    cnt = 0
    solve(0, 0, 0)
    print(f'#{tc} {cnt}')