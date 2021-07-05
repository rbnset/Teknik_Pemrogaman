setA = {'Hijau', 'Biru', 'Ungu', 'Merah'}
setB = {'Merah', 'Kuning', 'Putih', 'Hijau', 'Hitam'}
setC = setA ^ setB
print(setC)
setC = setA.symmetric_difference(setB)
print(setC)
setC = setB.symmetric_difference(setA)
print(setC)
