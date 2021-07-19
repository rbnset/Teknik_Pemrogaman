# Method Overriding :

class induk:
    def cobaOverride(self):
        print('Hi... saya method override di kelas induk')


class turunan(induk):
    def cobaOverride(self):
        print('Hi... saya method override di kelas anak')


# Deklarasi objek Kelas Induk
objectInduk = induk()
objectInduk.cobaOverride()

# Deklarasi objek kelas anak
objectAnak = turunan()
induk.cobaOverride(objectAnak)
