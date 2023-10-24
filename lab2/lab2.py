def can_fit(N, W, H, size):

    sheets_in_row = size // W
    sheets_in_column = size // H
    total_sheets = sheets_in_row * sheets_in_column
    return total_sheets >= N


def min_square_size(N, W, H):
    count = 0
    left = 1
    right = max(W, H) * N

    while left < right:
        count += 1
        mid = (left + right) // 2
        if can_fit(N, W, H, mid):
            right = mid
        else:
            left = mid + 1
    print(count)
    return left


# N, W, H = map(int, input().split())
N = 9000
W = 1000000000
H = 999999999
result = min_square_size(N, W, H)

print(result)


