from itertools import combinations
from math import prod

with open("day-08/input.txt") as f:
    inputData = list(map(lambda x: tuple(map(int, x.split(","))), f.read().splitlines()))

def distance(a, b, inp):
    return (inp[a][0]-inp[b][0])**2 + (inp[a][1]-inp[b][1])**2 + (inp[a][2]-inp[b][2])**2

def q1() -> int:
    N = 1000
    connections = list(map(set, sorted(combinations(range(len(inputData)), r=2), key=lambda x: distance(*x, inputData))[:N]))

    while True:
        found = False
        for i, conn1 in enumerate(connections):
            for j, conn2 in enumerate(connections):
                if i == j: continue

                if conn1.intersection(conn2):
                    connections = [conn for k, conn in enumerate(connections) if k not in (i, j)]
                    connections.append(conn1.union(conn2))
                    found = True
                    break
            if found:
                break
        if not found:
            break

    return prod(sorted(map(len, connections), reverse=True)[:3])

def q2() -> int:
    connections = list(map(set, sorted(combinations(range(len(inputData)), r=2), key=lambda x: distance(*x, inputData))))

    circuits = [{i} for i in range(len(inputData))]
    for conn in connections:
        # print(d, len(circuits))
        for i, circuit in enumerate(circuits):
            if conn.intersection(circuit):
                circuits[i] |= conn
                break

        while True:
            found = False
            for i, conn1 in enumerate(circuits):
                for j, conn2 in enumerate(circuits):
                    if i == j: continue

                    if conn1.intersection(conn2):
                        circuits = [c for k, c in enumerate(circuits) if k not in (i, j)]
                        circuits.append(conn1.union(conn2))
                        found = True
                        break
                if found:
                    break
            if not found:
                break
        
        if len(circuits) == 1:
            a, b = conn
            return inputData[a][0] * inputData[b][0]


def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
