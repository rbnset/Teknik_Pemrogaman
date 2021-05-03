awal = int(input('Masukkan saldo awal\t: '))
sisa = awal  # Bila tidak ada pengeluaran

while (True):
    pengeluaran = int(
        input('Masukkan pengeluaran hari ini (-1 untuk keluar) : '))

    if pengeluaran == -1:  # untuk berhenti
        print('Sisa saldo = ', sisa)  # sisa bila diberhentikan
        break
    sisa = sisa - pengeluaran
    if sisa < 0:
        print('Saldo tidak cukup')
        print('Sisa saldo ', sisa + pengeluaran)
        break
