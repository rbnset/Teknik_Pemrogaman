setA = {'Hijau', 'Biru', 'Ungu', 'Merah'}
setB = {'Merah', 'Kuning', 'Putih', 'Hijau', 'Hitam'}
setC = setA & setB
print(setC)
setC = setB.intersection(setA)
print(setC)
setC = setA.intersection(setB)
print(setC)
