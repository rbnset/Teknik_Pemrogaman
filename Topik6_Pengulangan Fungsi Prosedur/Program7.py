def luas_persegi(panjang, lebar):
    return panjang*lebar


def keliling_persegi(panjang, lebar):
    return 2*(panjang+lebar)


def menu():
    print('1. Luas Persegi')
    print('2. Kelling Persegi')
    pilih = int(input('Masukkan angka pilihan = '))
    if pilih == 1:
        panjang = int(input('Masukkan panjang = '))
        lebar = int(input('Masukkan lebar = '))
        print('Luas persegi = ', keliling_persegi(panjang, lebar))
    elif pilih == 2:
        panjang = int(input('Masukkan panjang = '))
        lebar = int(input('Masukkan Lebat = '))
        print('Keliling persegi = ', keliling_persegi(panjang, lebar))
    else:
        print('Todak ada  pilihan')
    ans = 'Y'
    ans = str(input('Do you want again (Y/N)?'))
    if ans == 'y' or ans == 'Y':
        menu()
    else:
        print('Terima Kasih')


menu()
