# Pencarian Sequential
# Program pencarian beruntun

a = [10, 4, 2, 3, 7, 1, 6, 8]
cari = input('Masukkan nilai yang dicari : ')
ketemu = False
for i in range(0, len(a)):
    if cari == a[i]:
        ketemu = True
        break
    if ketemu:
        print('Nilai : ', cari, 'berhasil ditemukan')
    else:
        print('Nilai : ', cari, 'tidak ditemukan')
