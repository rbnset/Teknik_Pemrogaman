#  Contoh Program Pewarisan 2 :

class Bapak(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def berjalan(self):
        print('Berjalan ke depan')

    def berlari(self):
        print('Berlari dengan cepat')

# Class Anak turunan dari class Bapak


class Anak(Bapak):
    pass


b = Bapak('Wiragan', 170, 68)
print()

print('Nama : ', b.nama)
print('Tinggi : ', b.tinggi, 'cm')
print('Berat : ', b.berat, 'kg')
b.berjalan()
b.berlari()

# Objek dari class Anak memiliki seluruh yang dimiliki class Bapak
a = Anak('Mustofa', 140, 32)
print()
print('Nama : ', a.nama)
print('Tinggi : ', a.tinggi, 'cm')
print('Berat : ', a.berat, 'kg')
a.berjalan()
a.berlari()
