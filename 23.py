def divisorsums(stop):
    ss = [ 0 for k in xrange(stop) ]
    for k in xrange(1, stop):
        for n in xrange(k*2, stop, k):
            ss[n] += k
    return ss

def divisors(stop):
    s = [ [] for k in xrange(stop) ]
    for k in xrange(1, stop):
        for n in xrange(k*2, stop, k):
            s[n].append(k)
    return s

if __name__ == '__main__':
    abundant, twosums, ints = set(), set(), set()
    for i,s in enumerate(divisorsums(28124)):
        if s > i: abundant.add(i)
        ints.add(i)

        for x in abundant:
            if i - x in abundant:
                twosums.add(i)
                break

    nosums = sum(list(ints.difference(twosums)))
    print nosums

    
