with open("day-01/input.txt") as f:
    inputData = f.readlines()

def q1() -> int:
    res = 0
    c = 50
    for line in inputData:
        d = line[0]
        n = int(line[1:])
        if d == "L":
            c = (c - n) % 100
        else:
            c = (c + n) % 100
        if c == 0:
            res += 1
    return res

# def q2() -> int:
#     res = 0
#     c = 50
#     for line in inputData:
#         d = line[0]
#         n = int(line[1:])
#         if d == "L":
#             while n:
#                 c -= 1
#                 n -= 1
#                 if c == -1:
#                     c = 99
#                 if c == 0:
#                     res += 1

#         else:
#             while n:
#                 c += 1
#                 n -= 1
#                 if c == 100:
#                     c = 0
#                     res += 1

#     return res

def q2() -> int:
    res = 0
    c = 50
    for line in inputData:
        d = line[0]
        n = int(line[1:])
        if d == "L":
            if n >= c:
                res += (n - c) // 100 + (1 if c != 0 else 0)
            c = (c - n) % 100
        else:
            if n >= (100 - c):
                res += (n - (100 - c) + 100) // 100
            c = (c + n) % 100
    return res


def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
