# vrni seznam koeficientov danega ulomka

def cf(m, n):
    assert m > 0 and n > 0, "m and n must be positive"
    res = []
    if m < n:
        res.append(0)
        m, n = n, m
    while n > 0:
        res.append(m // n)
        m, n = n, m % n
    return res


def fc(l):
    l = l[::-1]
    n = l[0]
    m = 1
    for a in l[1::]:
        m, n = n, a * n + m
    return n, m


if __name__ == '__main__':
    m, n = [int(x) for x in input().split()]
    l = cf(m, n)
    print(l)
