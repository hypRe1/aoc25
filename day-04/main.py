with open("day-04/input.txt") as f:
    inputData = f.read().splitlines()

def q1() -> int:
    a = 0
    paper = set()
    for i, r in enumerate(inputData):
        for j, ch in enumerate(r):
            if ch == "@":
                paper.add(i+j*1j)
    
    for p in paper:
        n = 0
        for d in (1+0j, -1+0j, 0-1j, 0+1j, 1+1j, 1-1j, -1+1j, -1-1j):
            if (p + d) in paper:
                n += 1
        if n < 4:
            a += 1

    return a

def q2() -> int:
    a = 0
    paper = set()
    for i, r in enumerate(inputData):
        for j, ch in enumerate(r):
            if ch == "@":
                paper.add(i+j*1j)
    
    nn = -1
    while nn != 0:
        to_be_removed = set()
        nn = 0
        for p in paper:
            n = 0
            for d in (1+0j, -1+0j, 0-1j, 0+1j, 1+1j, 1-1j, -1+1j, -1-1j):
                if (p + d) in paper:
                    n += 1
            if n < 4:
                to_be_removed.add(p)
                nn += 1
                a += 1
        paper.difference_update(to_be_removed)
    
    return a

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
