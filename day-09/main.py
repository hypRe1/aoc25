from itertools import combinations

with open("day-09/input.txt") as f:
    inputData = list(map(eval, f.read().splitlines()))

def area(b1, b2):
    return (max(b1[0], b2[0]) - min(b1[0], b2[0]) + 1) * (max(b1[1], b2[1]) - min(b1[1], b2[1]) + 1)

def q1() -> int:
    return area(*max(combinations(inputData, r=2), key=lambda x: area(*x)))

def q2() -> int:
    red = inputData
        
    green = []
    for r1, r2 in combinations(red, r=2):
        if r1[0] == r2[0]:
            green.append((r1,r2))
        if r1[1] == r2[1]:
            green.append((r1,r2))

    best = 0
    for (x,y), (u,v) in combinations(red, r=2):
        if x > u:
            x,u=u,x
        if y > v:
            y,v=v,y

        possible = (u-x+1) * (v-y+1)
        if possible > best:
            works = True
            for (p,q), (r,s) in green:
                if p > r:
                    p,r=r,p
                if q > s:
                    q,s=s,q
                
                if p < u and q < v and r > x and s > y:
                    works = False
                    break
            if works:
                best = possible
    return best

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
