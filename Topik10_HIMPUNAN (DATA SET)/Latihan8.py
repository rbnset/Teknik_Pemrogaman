setA = {'Hijau', 'Biru', 'Ungu', 'Merah'}
setB = {'Merah', 'Kuning', 'Putih', 'Hijau', 'Hitam'}
setC = setA | setB
print(setC)
setC = setA.union(setB)
print(setC)
setC = setB.union(setA)
print(setC)
