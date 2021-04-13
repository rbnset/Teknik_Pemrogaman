# Program konversi mata uang

print(
    'Pilih Konversi \n [1] Konversi dari Rupiah Ke Mata Uang Asing \n [2] Konversi dari Mata Uang Asing Ke Rupiah')


def RPtoAUD():
    kurs_rupiah = 11811
    RPtoAUD = rupiah/kurs_rupiah
    return RPtoAUD


def AUDtoRP():
    USAtoRP = asing*11811
    return USAtoRP


def RPtoUSD():
    kurs_rupiah = 14100
    RPtoUSD = rupiah/kurs_rupiah
    return RPtoUSD


def USDtoRP():
    USDtoRP = asing*14100
    return USDtoRP


def RPtoEuro():
    kurs_rupiah = 17800
    RPtoEuro = rupiah/kurs_rupiah
    return RPtoEuro


def EurotoRP():
    EurotoRP = asing*17800
    return EurotoRP


menu = int(input('Masukkan Pilihan : '))


if menu == 1:
    print(
        'Pilih Mata Uang Yang Akan dikonversi \n [1] Rupiah ke Dollar Australia \n [2] Rupiah ke Dolar US \n [3] Rupiah ke Euro')

    pilihan = int(input('Masukkan Pilihan : '))

    if pilihan == 1:
        rupiah = int(input('Masukkan Nominal Rupiah : '))
        RPtoAUD()
        print('{} Rupiah = {} AUD'.format(rupiah, RPtoAUD()))

    elif pilihan == 2:
        rupiah = int(input('Masukkan Nominal Rupiah : '))
        RPtoUSD()
        print('{} Rupiah = {} USD'.format(rupiah, RPtoUSD()))

    elif pilihan == 3:
        rupiah = int(input('Masukkan Nominal Rupiah : '))
        RPtoEuro()
        print('{} Rupiah = {} Euro'.format(rupiah, RPtoEuro()))

    else:
        print('Pilihan tidak tersedia')

if menu == 2:
    print(
        'Pilih Mata Uang Yang Akan dikonversi \n [1] Dollar Australia Ke Rupiah \n [2] Dollar US Ke Rupiah \n [3] Euro Ke Rupiah')

    pilihan = int(input('Masukkan Pilihan : '))

    if pilihan == 1:
        asing = int(input('Masukkan Nominal AUD : '))
        AUDtoRP()
        print('{} AUD = {} Rupiah'.format(asing, AUDtoRP()))

    elif pilihan == 2:
        asing = int(input('Masukkan Nominal USD : '))
        USDtoRP()
        print('{} USD = {} Rupiah'.format(asing, USDtoRP()))

    elif pilihan == 3:
        asing = int(input('Masukkan Nominal Euro : '))
        EurotoRP()
        print('{} Euro = {} Rupiah'.format(asing, EurotoRP()))

    else:
        print('Pilihan tidak tersedia')
else:
    exit()
