# Membuat Piramida
print('Pembuatan Piramida')
print('---------------------------')

n = int(input('n = '))

for baris in range(1, n+1):
    # Tampilkan karakter spasi
    for kolom in range(1, 2*(n-baris)+2):
        print(' ', end='')
    # Tampilkan bintang (*)
    for indeks in range(1, baris+1):
        print(' * ', end=' ')  # simbol *
    print()  # pindah baris
