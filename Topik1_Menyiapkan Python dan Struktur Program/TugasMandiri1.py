# Program Menghitung Luas, Volume dan Keliling dari Balok
print(
    'Program menghitung: \n [1] Luas \n [2] Volume \n [3] Keliling \n [4] Luas, Volume dan Keliling')


def luas(p, l, t):
    L = 2 * ((p*l) + (p*t) + (l*t))
    return L


def volume(p, l, t):
    V = p * l * t
    return V


def keliling(p, l, t):
    k = 4 * (p + l + t)
    return k


pilihan = int(input('Masukan pilihan     : '))

if pilihan == 1:
    p = int(input('Masukan panjang balok : '))
    l = int(input('Masukan lebar balok   : '))
    t = int(input('Masukan tinggi balok  : '))
    luas(p, l, t)
    print('Jadi balok dengan ukuran panjang : {}, lebar : {}, tinggi : {}\nMempunyai luas : {}'.format(
        p, l, t, luas(p, l, t)))

elif pilihan == 2:
    p = int(input('Masukan panjang balok : '))
    l = int(input('Masukan lebar balok   : '))
    t = int(input('Masukan tinggi balok  : '))
    volume(p, l, t)
    print('Jadi balok dengan ukuran panjang : {}, lebar : {}, tinggi : {}\nMempunyai volume : {}'.format(
        p, l, t, volume(p, l, t)))

elif pilihan == 3:
    p = int(input('Masukan panjang balok : '))
    l = int(input('Masukan lebar balok   : '))
    t = int(input('Masukan tinggi balok  : '))
    keliling(p, l, t)
    print('Jadi balok dengan ukuran panjang : {}, lebar : {}, tinggi : {}\nMempunyai keliling : {}'.format(
        p, l, t, keliling(p, l, t)))

elif pilihan == 4:
    p = int(input('Masukan panjang balok : '))
    l = int(input('Masukan lebar balok   : '))
    t = int(input('Masukan tinggi balok  : '))
    print('Jadi balok dengan ukuran panjang : {}, lebar : {}, tinggi : {}\nMempunyai Luas : {} \nMempunyai Volume : {} \nMempunyai Keliling : {} '.format(
        p, l, t, luas(p, l, t), volume(p, l, t), keliling(p, l, t)))


else:
    print('Pilihan tidak tersedia')
