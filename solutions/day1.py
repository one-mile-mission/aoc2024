def day1():
    with open('inputs/day1.txt') as f:
        data = f.read().replace('   ','\n').split('\n')
    f.close()

    l=data[0::2]
    l.sort()
    r=data[1::2]
    r.sort()
    p1=sum([abs(int(l)-int(r)) for l,r in zip(l,r)])
    oc = {li:r.count(li) for li in set(l)}
    p2=sum([int(li)*oc[li] for li in l])
    return f"D1P1: {p1}\nD1P2: {p2}"

if __name__ == '__main__':
    print(day1())