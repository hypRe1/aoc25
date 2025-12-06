from math import prod

with open("day-06/input1.txt") as f:
    inputData = f.read().splitlines()

def q1() -> int:
    ns = list(map(lambda x: list(map(int, x.split())), inputData[:-1]))
    ops = list(inputData[-1].replace(" ", ""))

    tns = list(map(list, zip(*ns)))
    acc = 0
    for op, tn in zip(ops, tns):
        if op == '*':
            acc += prod(tn)
        elif op == "+":
            acc += sum(tn)
    return acc

def q2():
    N = len(inputData)-1

    ops = list(inputData[-1].replace(" ", ""))[::-1]
    nns = []
    dds = []
    for i in range(len(inputData[0]))[::-1]:
        ds = [inputData[j][i] for j in range(N)]
        if all([d == " " for d in ds]):
            nns.append(list(map(lambda x: int("".join(x)), dds)))
            dds = []
            continue
        dds.append(ds)
    nns.append(list(map(lambda x: int("".join(x)), dds)))
    
    acc = 0
    for op, ns in zip(ops, nns):
        if op == '*':
            acc += prod(ns)
        elif op == "+":
            acc += sum(ns)
    return acc

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
