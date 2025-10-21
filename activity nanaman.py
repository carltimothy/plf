row = int(input("No. of rows: "))
col = int(input("No. of columns: "))

for r in range(1, row + 1):
    for c in range(1, col + 1):
        print(f"{r * c:6}", end=" ")
    print()
    # What I did here is that first nag initiate to multiply row and column then add spacing inbetween
    