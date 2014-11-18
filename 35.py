from itertools import chain
import timeit
from utils import primesfrom2to

# global prime set to collect all primes found so far
def rotate(string, n):
    string = str(string)
    return int(string[n:] + string[:n])

def is_largest_rotation(num):
    rot = [rotate(num, x) for x in range(len(str(num)))]
    return max(rot) == num

def all_rotations_in_primeset(num):
    rot = [rotate(num, x) for x in range(len(str(num)))]
    return all(map(lambda x: x in primeset, rot))

def is_circular_prime(num):
    if is_largest_rotation(num) \
    and num in primeset \
    and all_rotations_in_primeset(num):
        return True
    return False

def all_rotations(num):
    return [rotate(num, x) for x in range(len(str(num)))]

if __name__ == '__main__':
    start = timeit.default_timer()
    primeset = set(primesfrom2to(1000000))
    biggest_circulars = (x for x in primesfrom2to(1000000) if is_circular_prime(x))
    all_circulars = (all_rotations(x) for x in biggest_circulars)
    print len(set(chain.from_iterable(all_circulars)))
    print timeit.default_timer() - start
