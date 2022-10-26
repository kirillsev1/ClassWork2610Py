def letters(line):
    return sum([1 if line.count(i) and i != ' ' else 0 for i in set(line.lower())])


def letters1(line):
    return len([ch for ch in (set(line.lower())) if line.lower().count(ch) > 1])


if __name__ == '__main__':
    print(letters('aaaAbb'))
