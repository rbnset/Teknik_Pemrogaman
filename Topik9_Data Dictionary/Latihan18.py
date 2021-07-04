# Pengurutan data

warna = {'red': 'merah', 'blue': 'biru', 'green': 'hijau',
         'white': 'putih', 'yellow': 'kuning'}
print('Sebelum diurutkan menurut nilai')
for kunci in warna:
    print('%-6s:%-s' % (kunci, warna[kunci]))

print()
print('Sedudah diurutkan menurut nilai')
hasil = sorted(warna.items(), )
print(hasil)
for data in hasil:
    print('%-6s:%-s' % (data[1], data[0]))
