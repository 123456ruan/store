def NxN():
    for i in range(9, 0, -1):
        for j in range(1, i + 1):
            print(j, "x", i, "=", (i * j), "\t", end="")
        print()

NxN()