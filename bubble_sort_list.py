def bubble_sort_descending(arr):
    n = len(arr)
    
    # Iterasi untuk setiap elemen dalam daftar
    for i in range(n):
        
        # Pengecekan elemen dari indeks pertama hingga indeks ke-(n-i-1)
        for j in range(0, n-i-1):
            
            # Jika elemen saat ini lebih kecil daripada elemen berikutnya, tukar posisinya
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar angka yang ingin diurutkan
angka = [42, 19, 33, 8, 55]

# Memanggil fungsi bubble_sort_descending untuk mengurutkan daftar angka
bubble_sort_descending(angka)

# Menampilkan daftar angka yang telah diurutkan secara descending
print("Daftar angka yang diurutkan secara descending:")
for nilai in angka:
    print(nilai)