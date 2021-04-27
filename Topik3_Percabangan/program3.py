# Penentuan Diskon dengan IF ELSE
print('Penentuan Diskon Belanja')
print('------------------------')

besarPembelian = int(input('Nilai Nominal Pembelian : '))

# Penentuan Diskon
diskon = 0
if besarPembelian >= 200000:
    diskon = 0.05 * besarPembelian
else:
    diskon = 0

besarPembayaran = besarPembelian - diskon

# Tampilkan Hasil
print()
print('Pembelian  = ', besarPembelian)
print('Diskon     = ', diskon)
print('Pembayaran = ', besarPembayaran)
