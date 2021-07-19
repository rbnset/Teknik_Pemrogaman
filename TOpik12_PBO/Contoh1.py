class Ayah:
    def methodAyah(self):
        print('Ini adalah Method Ayah')


class Anak(Ayah):
    def methodAnak(self):
        print('Ini adalah Method Anak')


# Deklarasi objek kelas Ayah
p = Ayah()
p.methodAyah()

# Deklarasi objek kelas Aanak
c = Anak()
c.methodAnak()
c.methodAyah()
