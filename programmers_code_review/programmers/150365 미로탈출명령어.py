def solution(n, m, x, y, r, c, k):
    answer = ""

    directions = [
        ("d", 1, 0),
        ("l", 0, -1),
        ("r", 0, 1),
        ("u", -1, 0),
    ]

    dist = abs(x - r) + abs(y - c)

    if dist > k:
        return "impossible"

    if (k - dist) % 2 == 1:
        return "impossible"

    while k > 0:
        for char, dx, dy in directions:
            next_x = x + dx
            next_y = y + dy

            if not (1 <= next_x <= n and 1 <= next_y <= m):
                continue

            remain_k = k - 1
            remain_dist = abs(next_x - r) + abs(next_y - c)

            if remain_dist <= remain_k and (remain_k - remain_dist) % 2 == 0:
                answer += char
                x = next_x
                y = next_y
                k -= 1
                break

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))  # dllrl
print(solution(2, 2, 1, 1, 2, 2, 2))  # dr
print(solution(3, 3, 1, 2, 3, 3, 4))  # impossible