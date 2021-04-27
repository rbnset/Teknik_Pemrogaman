# Penentuan Bialngan Genap dan Ganjil
print('Penentuan Bilangan Genap atau Gannjil')
print('-------------------------------------')
bilangan = int(input('Bilangan : '))

# Penentuan bilangan ganjil atau genap
katagori = 'bilangan ganjil'
if bilangan % 2 == 0:
    katagori = 'bilangan genap'

# Tampilkan hasil
print('Bilangan', bilangan, 'merupakan', katagori)
