a = [
    [[('n02105412', 'kelpie', 0.14979276)]], [[('n02093256', 'Staffordshire_bullterrier', 0.7374367)]]
]


b = []
c = []
for i in range(len(a)):
    # print(i)
    b.append(a[i][0][0][0:])
    # print(list(b[i])[1:])
    c.append(list(b[i])[1:])

print(b)
print(c)