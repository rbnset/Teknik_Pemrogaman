# Program pencarian judul buku baru di perpustakaan

def linearSearch(item, my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found


book = ['100 startup', 'daily reader', 'petunjuk ui ux',
        'dont make me think', 'design thingking', 'hooked', 'sapiens', 'sprint']
item = input('Masukkan judul buku terbaru yang ingin kamu cari : ')
itemFound = linearSearch(item, book)
if itemFound:
    print('Yup, buku yang anda cari tersedia di perpustakaan')
else:
    print('Oops, buku yang anda cari belum tersedia')
