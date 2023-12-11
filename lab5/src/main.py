def max_experience(levels, experience):
    for i in range(levels - 2, -1, -1):
        for j in range(i + 1):
            experience[i][j] += max(experience[i + 1][j], experience[i + 1][j + 1])


    return experience[0][0]

def main():
    # Зчитуємо вхідні дані
    with open("career.in", "r") as file:
        levels = int(file.readline())
        experience = [list(map(int, file.readline().split())) for _ in range(levels)]

    # Знаходимо максимальний досвід
    result = max_experience(levels, experience)

    # Записуємо результат у вихідний файл
    with open("career.out", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
