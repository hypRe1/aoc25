with open("day-05/input.txt") as f:
    inputData = f.read()

def q1() -> int:
    res = 0
    a,b = inputData.split("\n\n")

    ranges = list(map(lambda x: tuple(map(int, x.split("-"))), a.split("\n")))
    for n in map(int, b.split("\n")):
        fresh = False
        for l, u in ranges:
            if l <= n <= u:
                fresh = True
                break
        if fresh:
            res += 1
    return res


def q2() -> int:
    res = 0
    a,b = inputData.split("\n\n")

    ranges = list(map(lambda x: tuple(map(int, x.split("-"))), a.split("\n")))
    while 1:
        d = False
        for i, (l, u) in enumerate(ranges):
            for j, (l1, u1) in enumerate(ranges):
                if (i == j):
                    continue

                if (l <= l1 <= u) | (l1 <= l <= u1) | (l <= u1 <= u) | (l1 <= u <= u1):
                    ranges[i] = (min(l, l1), max(u, u1))
                    del ranges[j]
                    d = True
                    break
            if d:
                break
        if not d:
            break

    for l, u in ranges:
        res += u - l + 1

    return res

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
