# Contoh Program Pewarisan 3 :

class Mahasiswa():
    def __init__(self, nama, nim, alamat):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat

    def cek_data_mahasiswa(self):
        print('nama : ', self.nama, '\nnim : ',
              self.nim, '\nalamat : ', self.alamat)


mahasiswa1 = Mahasiswa('irawan', '08122671', 'jakarta barat')
mahasiswa1.cek_data_mahasiswa()

mahasiswa2 = Mahasiswa('riko', '08126672', 'jakarta selatan')
mahasiswa2.cek_data_mahasiswa()
