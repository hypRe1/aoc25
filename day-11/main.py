from functools import cache

with open("day-11/input.txt") as f:
    inputData = f.read().splitlines()
G: dict[str, frozenset[str]] = {}
for line in inputData:
    l, r = line.split(":")
    G[l] = frozenset(r.strip().split(" "))


@cache
def n_paths(node):
    if "out" in G[node]:
        return 1

    return sum(n_paths(n) for n in G[node])


@cache
def n_paths_2(node, dac=False, fft=False):
    nexts = G[node]
    if "out" in nexts:
        return int(dac and fft)

    res = 0
    for n in nexts:
        if not dac and n == "dac":
            res += n_paths_2(n, True, fft)
        elif not fft and n == "fft":
            res += n_paths_2(n, dac, True)
        else:
            res += n_paths_2(n, dac, fft)
    return res


def q1() -> int:
    return n_paths("you")


def q2() -> int:
    return n_paths_2("svr")


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
