# Tabel perkalian
print('Tabel Perkalian')
print('---------------')
n = int(input('N = '))
print('  ', end='')

for kolom in range(1, n+1):
    print('%3d ' % kolom, end='')

print()

for baris in range(1, n + 1):
    print('%3d ' % baris, end='')

    for kolom in range(1, baris):
        print('%4s' % ' ', end='')

    for kolom in range(baris, n + 1):
        print('%3d ' % (baris * kolom), end='')

    print()
