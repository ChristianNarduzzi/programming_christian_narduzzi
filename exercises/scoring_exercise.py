def scoring(a, b):
    s = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            s += 1
        else:
            s += 0
    return s
a = input('insert the first sequence')
b = input('insert the second sequence')
if len(a) != len(b):
    print('are not equal')
else:
    print(scoring(a, b))
