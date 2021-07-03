# Operator untuk kamus

# Hasil True
kamus1 = {'a': 1}
kamus1 = {'a': 1, 'b': 2}
kamus2 = {'b': 2, 'a': 1}
kamus3 = {'A': 1, 'a': 2}
kamus1 == kamus2


# Hasil True
kamus1 = {'a': 1}
kamus1 = {'a': 1, 'b': 2}
kamus2 = {'b': 2, 'a': 1}
kamus3 = {'A': 1, 'a': 2}
'b' in kamus1


# Hasil False
kamus1 = {'a': 1}
kamus1 = {'a': 1, 'b': 2}
kamus2 = {'b': 2, 'a': 1}
kamus3 = {'A': 1, 'a': 2}
'c' in kamus1
