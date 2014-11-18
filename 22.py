alphabet = 'abcdefghijklmnopqrstuvwxyz'
scores = zip([x for x in alphabet], xrange(1, 27)) + zip([x for x in alphabet.upper()], xrange(1, 28))
scores = dict(scores)

def scoreof(name):
    return sum([scores[x] for x in name])

f = open('p022_names.txt')
names = f.next()
names = names.split('","')
names[0] = names[0].replace('"', '')
names[-1] = names[-1].replace('"', '')
names.sort()

total = 0
for i in xrange(len(names)):
    total += (i+1) * scoreof(names[i])
    
print total
