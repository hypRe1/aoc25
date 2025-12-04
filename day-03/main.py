with open("day-03/input.txt") as f:
    inputData = f.read().splitlines()

def q1() -> int:
    r = 0
    for line in inputData:
        i, a = max(list(enumerate(line[:-1])), key=lambda x: x[1])
        b = max(line[i+1:])
        r += int(a)*10+int(b)
    return r

def q2() -> int:
    r = 0
    for line in inputData:
        l = 0
        for u in range(11, 0, -1):
            l, a = max(list(enumerate(line))[l:-u], key=lambda x: x[1])
            l += 1
            r += int(a + '0'*(u))
        r += int(max(line[l:]))
    return r

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
