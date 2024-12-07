def test_report(report:list):
    sign =[]
    for i in range(len(report)-1):
        if 1<= abs(report[i]-report[i+1]) <=3:
            sign+=[(report[i+1]-report[i])/abs(report[i+1]-report[i])]
        else: 
            safe = False
            break
        if not all(x==sign[0] for x in sign):
            safe=False
            break
        else: safe=True
    return safe

def day2():
    with open("inputs/day2.txt") as f:
        data = [[int(p) for p in r.split(' ')] for r in f.read().split('\n')]
    f.close()

    outcomes=[]
    for row in data:
        outcomes+=[test_report(row)]
    p1=sum(outcomes)

    outcomes=[]
    for report in data:
        report_outcomes=[]
        for i in range(len(report)):
            test=report.copy()
            test.pop(i)
            report_outcomes+=[test_report(test)]
        if any(report_outcomes):
            outcomes+=[True]
        else: outcomes+=[False]

    p2=sum(outcomes)
    
    return f"D2P1: {p1}\nD2P2: {p2}"


if __name__ == "__main__":
    print(day2())
