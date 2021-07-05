# membuat set baru
my_set = {1, 2, 3, 4, 5}
print(my_set)

# menghapus 4 dengan discard
# output: {1, 2, 3, 5}
my_set.discard(4)
print(my_set)

# menghapus 5 dengan remove
# output : {1, 2, 3}
my_set.remove(5)
print(my_set)

# anggota yang mau dihapus tidak ada dalam set
# discard tidak akan memunculkan error
# output: {1, 2, 3}
my_set.discard(6)
