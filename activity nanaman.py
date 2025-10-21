rows = int(input("No. of rows: "))
columns = int(input("No. of columns: "))

for r in range(1, rows + 1):
    for c in range(1, columns + 1):
        print(f"{r * c:6}", end=" ")
    print()
    # What I did here is that first nag initiate to multiply row and column then add spacing inbetween
    