import re
from pulp import *

with open("day-10/input.txt") as f:
    inputData = f.read().splitlines()


def q1() -> int:
    res = 0
    for line in inputData:
        y = re.findall(r"\[([.#]+)\]", line)[0]
        N = len(y)
        final_state = int("".join(["1" if x == "#" else "0" for x in y]), 2)
        buttons = list(map(lambda x: eval(x + ","), re.findall(r"\(([\d,]+)\)", line)))

        better_buttons = []
        for b in buttons:
            s = [False] * N
            for a in b:
                s[a] = not s[a]
            better_buttons.append(int("".join(["1" if n else "0" for n in s]), 2))

        states = [(0, 0)]
        seen = {0}
        while states:
            curr, steps = states.pop(0)
            found = False
            steps += 1
            for b in better_buttons:
                next = curr ^ b
                if next in seen:
                    continue
                seen.add(next)
                if next == final_state:
                    found = True
                    res += steps
                    break
                states.append((next, steps))
            if found:
                break

    return res


def q2():
    res = 0
    for line in inputData:
        buttons = list(map(lambda x: eval(x + ","), re.findall(r"\(([\d,]+)\)", line)))
        joltage_requirements = tuple(
            map(int, re.findall(r"\{([\d,]+)\}", line)[0].split(","))
        )
        prob = LpProblem("myProblem", LpMinimize)

        button_variables = [
            LpVariable(
                f"b_{i}", 0, min(joltage_requirements[x] for x in b), cat="Integer"
            )
            for i, b in enumerate(buttons)
        ]

        for i, x in enumerate(joltage_requirements):
            prob += lpSum([v for v, b in zip(button_variables, buttons) if i in b]) == x
            
        objective = lpSum(button_variables)
        prob += objective
        prob.solve(PULP_CBC_CMD(msg=0))
        res += int(value(objective))
    return res


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
