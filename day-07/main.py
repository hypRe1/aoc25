from functools import cache

with open("day-07/input.txt") as f:
    inputData = f.read().splitlines()

def q1() -> int:
    a = 0
    for i, row in enumerate(inputData):
        for j, ch in enumerate(row):
            if ch == "S":
                beams = {j}
            
            if ch == "^" and j in beams:
                beams.remove(j)
                beams.add(j-1)
                beams.add(j+1)
                a += 1
    return a

@cache
def q2_rec(i, j):
    if i + 1 == len(inputData):
        return 1
    if inputData[i+1][j] == "^":
        return q2_rec(i+1,j-1)+q2_rec(i+1,j+1)
    else:
        return q2_rec(i+1,j)

def q2() -> int:
    for i, row in enumerate(inputData):
        for j, ch in enumerate(row):
            if ch == "S":
                s = (i, j)

    return q2_rec(*s)

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
