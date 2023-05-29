def bubble_sort(arr):
    n = len(arr)
    
    # Iterasi untuk setiap elemen dalam daftar
    for i in range(n):
        
        # Pengecekan elemen dari indeks pertama hingga indeks ke-(n-i-1)
        for j in range(0, n-i-1):
            
            # Jika elemen saat ini lebih besar daripada elemen berikutnya, tukar posisinya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar nilai ujian siswa
nilai_siswa = [78, 65, 90, 82, 70]

# Memanggil fungsi bubble_sort untuk mengurutkan daftar nilai siswa
bubble_sort(nilai_siswa)

# Menampilkan daftar nilai yang telah diurutkan
print("Daftar nilai yang diurutkan:")
for nilai in nilai_siswa:
    print(nilai)