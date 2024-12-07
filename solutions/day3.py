import re

def day3():
    with open("inputs/day3.txt") as f:
        data = f.read()
    f.close()

    m = re.findall(r'mul\((\d*),(\d*)\)|(do[nt\']{0,3}\(\))', data)
    print(m)
    p1 = sum([int(mul[0])*int(mul[1]) for mul in m if mul[0]!=''])

    i, do = [], 1
    for row in m:

        if row[2]=="don't()": do = 0
        if row[2]=="do()":
            do=1
            continue
        if do==1: i.append(int(row[0])*int(row[1]))
    p2 = sum(i)

    return f"D3P1: {p1}\nD3P2: {p2}"

if __name__ == "__main__":
    print(day3())
