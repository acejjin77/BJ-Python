from collections import deque


def check(begin, target):
    l = len(begin)
    cnt = 0

    for i in range(l):
        if begin[i] != target[i]:
            cnt += 1

        if cnt > 1:
            return False
    return True


def solution(begin, target, words):
    answer = 0
    visited = {begin: 0}

    q = deque(begin)
    while q:
        for word in words:
            now = q.popleft()

            if check(now, word) and word not in visited.keys():
                visited[word] = visited[now] + 1
                q.append(word)

    if target in visited:
        return visited[target]
    return 0

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))