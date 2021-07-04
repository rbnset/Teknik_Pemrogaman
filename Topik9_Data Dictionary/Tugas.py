# Tugas Membuat Kamus Sederhana

kamusIndonesia = {'merah': 'red', 'kuning': 'yellow', 'biru': 'blue',
                  'hijau': 'green', 'hitam': 'black', 'putih': 'white', }

kamusInggris = {'red': 'merah', 'yellow': 'kuning', 'blue': 'biru',
                'green': 'hijau', 'black': 'hitam', 'white': 'putih'}

print('1. Kamus Indonesia-Inggris')
print('2. Kamus Inggris-Indonesia')
pilih = int(input('Masukkan Pilihanmu : '))


if pilih == 1:
    kunci = input('Masukkan Warna dalam bahasa Indoensia : ')
    kunci = kunci.lower()
    hasil = kamusIndonesia.get(kunci, 'saya tidak tahu')
    print('Bahasa Inggrisnya : ', hasil)
elif pilih == 2:
    kunci = input('Masukkan Warna dalam bahasa Inggrisnya : ')
    kunci = kunci.lower()
    hasil = kamusInggris.get(kunci, 'saya tidak tahu')
    print('Bahasa Indoensianya : ', hasil)
else:
    print('Maaf pilihan yang anda masukkan tidak tersedia')
