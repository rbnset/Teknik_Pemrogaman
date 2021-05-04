# Tugas Mandiri Membuat deret aritmatik interval 2 yang diawali dari angka 1. untuk akhir deret silahkan ditentukan sendiri. Hitung juga totalnya. Contoh : 1 3 5 7 dst, Jumlah Total =

print('Masukkan Deret')
print('--------------------------------')

n = int(input('N = '))
hitungan = 1
total = 0

while hitungan <= n:
    print(2 * hitungan - 1, end=' ')
    hitungan = hitungan + 1
    total += hitungan * 2 - 3

print()
print('Jumlah Total : ', total)
