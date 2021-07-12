# Program untuk menghitung mundue (2) dengan Perlambatan 0.5 detik

import time

print("Apakah anda yakin akan meluncurkan roket?\n")
input("Tekan [Enter] untuk memulai…")

for i in range(10, 0, -1):
    time.sleep(1)
    print(i)

print("Buuzzzzssss!!!!")
print("Roket meluncur!!!")
