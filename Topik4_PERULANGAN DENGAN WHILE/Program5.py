# menggunakan sentinel untuk mengakhiri penginputan data

cacah = 0
total = 0
data = int(input('Masukkan data. (-1 untuk SELESAI) : '))

while data != -1:
    cacah += 1
    total += data
    data = int(input('Masukkan data. (-1 untuk SELESAI) : '))

# Menghitung rata-rata
jumlah_total = total
rerata = total / cacah

print('Jumlah Total = ', jumlah_total)
print('Rata-rata = ', rerata)
