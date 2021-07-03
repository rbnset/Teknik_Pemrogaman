# Pencarian dengan Binary Search (Pencarian Biner)

def binary_search(angka, listku):
    listku.sort()  # Penyortiran List
    langkah = 0
    ketemu = False
    awal = 0
    akhir = len(listku)-1
    while awal <= akhir and not ketemu:
        tengah = (awal+akhir)//2
        if listku[tengah] == angka:
            ketemu = True
        elif angka > tengah:
            awal = tengah+1
        else:
            akhir = tengah-1
        langkah += 1
    if ketemu:
        print('Angka ditemukan!')
        print('posisi angka yang ditemukan adalah %s' % str(awal+1))
    else:
        print('Angka yang anda masukkan tidak ditemukan!')
    print('Langkah yang sudah di ambil dalam menemukan adalah %s langkah' % langkah)


binary_search(3, [1, 1, 2, 6, 7, 8, 9, 3, 4])
