# membuat set baru
my_set = {1, 2, 3}
print(my_set)

# bila kita hilangkan tanda # dari baris 9 akan muncul error TypeError
# my_set[0]

# menambah satu anggota
# output: {1,2,3,4}
my_set.add(4)
print(my_set)

# menambah beberapa anggota
# set akan menghilangkan duplikasi
# output: {1,2,3,4,5,6}
my_set.update([3, 4, 5, 6])
print(my_set)
