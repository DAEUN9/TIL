def solution(key, lock):
    target = find_target(lock)
    print(target)
    if check(target[0], target[1], lock, key):
        return True
    for i in range(3):
        key = rotate(key)
        if check(target[0], target[1], lock, key):
            return True

    return False


def find_target(lock):
    target = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                return [i, j]
    return target


def rotate(key):
    return list(map(list, zip(*key[::-1])))


def check(target_x, target_y, lock, key):
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j]:
                if match_lock(i, j, target_x, target_y, lock, key):
                    return True
    return False


def match_lock(start_r, start_c, target_x, target_y, lock, key):
    a, b = start_r - target_x, start_c - target_y
    for i in range(len(lock)):
        for j in range(len(lock)):
            if not lock[i][j]:
                if 0 <= i + a < len(key) and 0 <= j + b < len(key) and key[i + a][j + b]:
                    continue
                return False
    return True

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))