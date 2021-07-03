# Contoh kamus

kamus = {'anjing': 'dog', 'burung': 'bird', 'harimau': 'tiger', 'merpati': 'dove', 'kambing': 'goat',
         'kelelawar': 'bat', 'kelinci': 'rabbit', 'kera': 'monkey', 'kucing': 'cat', 'sapi': 'cow'}

print('Ketik selesai untuk mengakhiri')
while True:
    kunci = input('Nama Hewan : ')
    kunci = kunci.lower()
    if kunci == 'selesai':
        break
    hasil = kamus.get(kunci, 'saya tidak tahu')
    print('Bahasa Inggrisnya : ', hasil)
    print()
    print('*** Selesai')
