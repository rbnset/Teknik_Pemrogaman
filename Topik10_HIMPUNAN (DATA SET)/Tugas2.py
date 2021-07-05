# Program Dafar Buku Tersedia di Perpustakaan

Lama = {'Bumi', 'Matahari', 'Negeri Para Bedebah',
        'Sebuah Seni Bersikap Bodo Amat', '100 Starup'}
Baru = {'The Rib King', 'Impostor Syndrom', 'Klara and the Sun'}

Baru.add('The Divines')
Semua = Lama | Baru

print('Buku Lama : ', Lama)
print('Buku Baru : ', Baru)
print('Buku Yang tersedia saat ini : ', Semua, '\njumlah : ', len(Semua))
print()


data = input('Masukkan Judul Buku yang ingin di pinjam : ')
print('Selamat Anda Berhasil Meminjam buku ', data)
print()
Lama.remove(data)
Semua = Lama | Baru

print('=======================================================================================================================================================================')
print('Buku Lama : ', Lama)
print('Buku Baru : ', Baru)
print('Buku Yang tersedia saat ini : ', Semua, '\njumlah : ', len(Semua))
