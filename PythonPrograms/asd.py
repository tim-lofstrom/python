


def solve1(n):

    if n == 0:
        return n
    else:
        print "first:" + str(solve(n-1))
        return n


def solve(n):

    if n == 0:
        return n
    else:
        print "second" + str(solve1(n-1))
        return n
        



solve(5)










def bounce(n):

    i = list(reversed(range(0,n)))
    j = range(1,n)
    t = i + j

    for l in t:
        print l,

bounce(5)






















