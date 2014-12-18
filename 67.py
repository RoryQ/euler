import io

def text_to_jaggedarray(text):
    l = []
    [l.append(row.split()) for row in text.strip().splitlines()]
    l = [map(int, row) for row in l]
    return l

def max_edges(parent_list, child_list):
    return [parent_list[i] + max(child_list[i], child_list[i+1])
            for i in range(len(parent_list))]

if __name__ == '__main__':
    f = open('p067_triangle.txt')
    triangle = f.readlines()
    triangle = ''.join(triangle)
    puzz = text_to_jaggedarray(triangle)
    prev = puzz[-1]
    for x in reversed(range(len(puzz) -1)):
        prev = max_edges(puzz[x], prev)
    print prev
