nilai = int(input('Nilai Anda ? :'))
print('Nilai : ', nilai)

if nilai >= 90:
    print('Pertahankan')
elif (nilai >= 80) and (nilai < 90):
    print('Harus lebih baik lagi')
elif (nilai >= 60) and (nilai < 80):
    print('perbanyak belajar')
elif (nilai >= 40) and (nilai < 60):
    print('Jangan keseringan main')
elif nilai < 40:
    print('Kebanyakan bolos...')
else:
    print('Maaf, format nilai tidak sesuai')
