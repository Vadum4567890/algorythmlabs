from collections import deque

# Зчитуємо вхідні дані з файлу
with open('input.txt', 'r') as file:
    start = tuple(map(int, file.readline().strip().split(',')))
    end = tuple(map(int, file.readline().strip().split(',')))
    rows, cols = map(int, file.readline().strip().split(','))
    matrix = []
    for _ in range(rows):
        row = list(map(int, file.readline().strip().split()))  # Зчитуємо окремі числа в рядку
        matrix.append(row)
# Функція для перевірки, чи можна рухатися в певному напрямку
def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1

queue = deque()
queue.append((start, 0))

# Масив для відстеження відстаней
distances = [[-1 for _ in range(cols)] for _ in range(rows)]
distances[start[0]][start[1]] = 0

# Масив для зберігання напрямків руху
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    (x, y), distance = queue.popleft()

    if (x, y) == end:
        shortest_distance = distance
        break

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y) and distances[new_x][new_y] == -1:
            distances[new_x][new_y] = distance + 1
            queue.append(((new_x, new_y), distance + 1))

# Записуємо результат у файл
with open('output.txt', 'w') as file:
    file.write(str(shortest_distance))

print("Найкоротший шлях:", shortest_distance)
