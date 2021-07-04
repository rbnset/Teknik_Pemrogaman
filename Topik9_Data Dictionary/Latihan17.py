# Pengurutan data

warna = {'red': 'merah', 'blue': 'biru', 'green': 'hijau',
         'white': 'putih', 'yellow': 'kuning'}
print('Sebelum diurutkan menurut kunci')
for kunci in warna:
    print('%-6s:%-s' % (kunci, warna[kunci]))

print()
print('Sedudah diurutkan menurut kunci')
daftarkunci = warna.keys()
for kunci in sorted(daftarkunci):
    print('%-6s:%-s' % (kunci, warna[kunci]))
