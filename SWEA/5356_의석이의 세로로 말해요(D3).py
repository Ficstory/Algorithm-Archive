T = int(input())
for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    result = []
    # 제일 짧은 줄
    max_len = 0
    for i in words:
        if len(i) > max_len:
            max_len = len(i)
    for i in range(max_len):
        for j in range(5):
            if len(words[j]) < i+1:
                continue
            result.append(words[j][i])
    print(f'#{tc} {"".join(map(str, result))}')