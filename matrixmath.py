def add(a,b):
    return [[(a[i][j]+ b[i][j]) for j in range(len(a[0]))] for i in range(len(a))]

def sub(a,b):
    return [[(a[i][j]- b[i][j]) for j in range(len(a[0]))] for i in range(len(a))]

def mul(a,b):
    c = [[0 for i in range(len(a[0]))]for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c

                
