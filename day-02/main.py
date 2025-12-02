import re

with open("day-02/input.txt") as f:
    inputData = list(map(lambda x: tuple(map(int, x.split("-"))), f.read().strip().split(",")))

def q1() -> int:
    invalid = set()
    for a, b in inputData:
        for i in range(a, b+1):
            if re.match(r"^(\d+)\1$", str(i)):
                invalid.add(i)
    return sum(invalid)

def q2() -> int:
    invalid = set()
    for a, b in inputData:
        for i in range(a, b+1):
            if re.match(r"^(\d+)(\1)+$", str(i)):
                invalid.add(i)
    return sum(invalid)

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
