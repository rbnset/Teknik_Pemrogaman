# Contoh kamus

kamus = {'anjing': 'dog', 'burung': 'bird', 'harimau': 'tiger', 'merpati': 'dove', 'kambing': 'goat',
         'kelelawar': 'bat', 'kelinci': 'rabbit', 'kera': 'monkey', 'kucing': 'cat', 'sapi': 'cow'}

daftarkunci = kamus.keys()
for kunci in daftarkunci:
    nilai = kamus[kunci]
    print('%-10s:%-10s' % (kunci, nilai))
