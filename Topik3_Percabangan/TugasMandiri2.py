# Input Nilai
Tugas = int(input('Masukkan Nilai Tugas : '))
Praktikum = int(input('Masukkan Nilai Praktikum : '))
UTS = int(input('Masukkan Nilai UTS : '))
UAS = int(input('Masukkan Nilai UAS : '))

print('Nilai Tugas : ', Tugas)
print('Nilai Praktikum : ', Praktikum)
print('Nilai Tugas : ', UTS)
print('Nilai UAS : ', UAS)

# Komponen Nilai
NilaiGabunggan = 0.2 * Tugas + 0.15 * Praktikum + 0.3 * UTS + 0.35 * UAS
print('Nilai Gabungan Anda adalah', NilaiGabunggan)

# Konversi Nilai
if (NilaiGabunggan > 80) and (NilaiGabunggan <= 100):
    print('Nilai A')
elif (NilaiGabunggan > 66) and (NilaiGabunggan <= 80):
    print('Nilai B')
elif (NilaiGabunggan > 56) and (NilaiGabunggan <= 66):
    print('Nilai C')
elif (NilaiGabunggan > 46) and (NilaiGabunggan <= 56):
    print('Nilai D')
else:
    print('Nilai E')
