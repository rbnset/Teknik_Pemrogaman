# Pencarian dengan Linear Search (Pencarian Mdoe Linier)

def linierSearch(lists, dicari):
    posisi = 0
    ketemu = False
    while posisi < len(lists) and not ketemu:
        if dicari == lists[posisi]:
            ketemu = True
        posisi += 1
    print('Angka ketemu di index = %i ' % posisi)


lists = []
a = int(input('Masukkan beberapa panjang list yang ingin dibuat = '))
for i in range(a):
    x = int(input('Masukkan angka ke %i untuk list = ' % (i+1)))
    lists.append(x)
dicari = int(input('Masukkan angka yang dicari = '))
linierSearch(lists, dicari)
