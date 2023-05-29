def selection_sort(arr):
    n = len(arr)
    
    # Iterasi untuk setiap elemen dalam daftar
    for i in range(n):
        
        # Temukan elemen terkecil dalam sisa daftar yang belum diurutkan
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen terkecil dengan elemen pertama dalam sisa daftar yang belum diurutkan
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Daftar angka yang dimiliki Andi
angka_andi = [9, 5, 3, 8, 2]

# Memanggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(angka_andi)

# Menampilkan daftar angka yang telah diurutkan
print("Daftar angka yang diurutkan:")
for angka in angka_andi:
    print(angka)