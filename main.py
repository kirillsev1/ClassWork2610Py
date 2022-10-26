import time

def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        time1 = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        time2 = time.time() - initial_time
        print(f2.__name__ if time1 > time2 else f1.__name__)
    return f

def letters(line):
    return sum([1 if line.count(i) and i != ' ' else 0 for i in set(line.lower())])

def letters1(line):
    return len([ch for ch in (set(line.lower())) if line.lower().count(ch) > 1])

function = worktime(letters, letters1)
function('aaaBBnns')
