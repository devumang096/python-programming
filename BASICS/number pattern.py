#print the pattern
 #     1
 #    12
 #   123
 #  1234
 # 12345
rows = 6
for i in range(1, rows):
    a = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(a, end=' ')
            a += 1
    print("")