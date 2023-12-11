def boyer_moore_search(haystack, needle):
    if not needle:
        return []

    m, n = len(needle), len(haystack)
    if m > n:
        return []

    indexes = []
    last_occurrence = {needle[i]: i for i in range(m)}
    i = m - 1

    while i < n:
        j = m - 1
        while j >= 0 and haystack[i] == needle[j]:
            i -= 1
            j -= 1

        if j == -1:
            indexes.append(i + 1)

        char_shift = max(1, m - 1 - last_occurrence.get(haystack[i], -1))
        suffix_shift = m - j if j != 0 else 1

        i += max(char_shift, suffix_shift)

    return indexes

haystack = "aba aba  aba     aba"
needle = "aba"
result = boyer_moore_search(haystack, needle)
print(f"Indexes of '{needle}' in '{haystack}': {result}")
