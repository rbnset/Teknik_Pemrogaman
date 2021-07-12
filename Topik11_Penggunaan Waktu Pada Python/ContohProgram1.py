# Program selisih jam

#  judul
# mencari durasi dari 2 waktu
# kamus
# jamawaljam = int
# jamakhirjam = int
# jamawalmenit = int
# jamakhirmenit = int
# jamawaldetik = int
# jamakhirdetik = int
# deskripsi
print(">>>>>>>>>>>>>>>>>>SELAMAT DATANG<<<<<<<<<<<<<<<<<<<<")
print("Masukan dalam format 24jam")
print("--------------------------")
jamawaljam = int(input("masukan jam awal: "))
jamawalmenit = int(input("masukan menit awal: "))
jamawaldetik = int(input("masukan detik awal: "))
print("\t\t\t\t\t ")
jamakhirjam = int(input("masukan jam akhir: "))
jamakhirmenit = int(input("masukan menit akhir: "))
jamakhirdetik = int(input("masukan detik akhir: "))
detikawal = jamawaljam * 3600 + jamawalmenit * 60 + jamawaldetik
detikakhir = jamakhirjam * 3600 + jamakhirmenit * 60 + jamakhirdetik

if(detikawal < detikakhir):
    durasi = detikakhir - detikawal
else:
    durasi = (detikakhir+24*3600)-detikawal

# konversi
jamdurasijam = durasi/3600
jamdurasimenit = (durasi % 3600)/60
jamdurasidetik = durasi % 60

# konversi (am 00.00-11.59 pm 12.00-23.59)

print("durasinya %d jam %d menit %d detik" %
      (jamdurasijam, jamdurasimenit, jamdurasidetik))
