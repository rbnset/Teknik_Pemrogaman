# Program himpunan makanan favorit


Nasgor = {'Robin', 'Taufiq', 'Iqbal', 'Bayu', 'Dwi'}
Bakso = {'Galih', 'Taufiq', 'Niken', 'Anggie', 'Dwi'}
Mie = {'Robin', 'Dwi', 'Bayu', 'Nimas'}

Nasgor.add('Argo')
Bakso.remove('Taufiq')

print('Daftar yang menyukai Nasgor : ', Nasgor)
print('Daftar yang menyukai Bakso : ', Bakso)
print('Daftar yang menyukai Mie : ', Mie)
print()


print('Daftar yang menyukai Nasgor dan Bakso : ', (Nasgor & Bakso))
print('Jumlah yang menyukai Nasgor dan Bakso : ', len(Nasgor & Bakso))
print('Daftar yang tidak menyukai Nasgor dan Bakso : ', (Nasgor ^ Bakso))
print('Jumlah yang menyukai Nasgor dan Bakso : ', len(Nasgor ^ Bakso))
print()
print('Daftar yang menyukai Nasgor dan Mie : ', (Nasgor & Mie))
print('Jumlah yang menyukai Nasgor dan Mie : ', len(Nasgor & Mie))
print('Daftar yang tidak menyukai Nasgor dan Mie : ', (Nasgor ^ Mie))
print('Jumlah yang tidak menyukai Nasgor dan Mie : ', len(Nasgor ^ Mie))
print()
print('Daftar yang menyukai Bakso dan Mie : ', (Bakso & Mie))
print('Jumlah yang menyukai Bakso dan Mie : ', len(Bakso & Mie))
print('Daftar yang tidak menyukai Bakso dan Mie : ', (Bakso ^ Mie))
print('Jumlah yang tidak menyukai Bakso dan Mie : ', len(Bakso ^ Mie))
