# membuat A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Menggunakan operator ^ pada A
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# Output: {1, 2, 3, 6, 7, 8}
A.symmetric_difference(B)

# Menggunakan operator ^ pada B
# Output: {1, 2, 3, 6, 7, 8}
print(B ^ A)

# Output: {1, 2, 3, 6, 7, 8}
B.symmetric_difference(A)
