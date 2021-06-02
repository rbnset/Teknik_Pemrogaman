# Buat program dengan Python untuk menampilkan :
123456
23456
3456
456
5

n = 5

for col in range(1, n+2):
    print(col, end='')
print()
for row in range(2, n+1):
    print(row, end='')

    for col in range(row, n+1):
        if row >= n:
            break
        print((col+1), end='')
    print()
