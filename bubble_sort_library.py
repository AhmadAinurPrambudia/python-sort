def bubble_sort_books(books):
    n = len(books)
    
    # Iterasi untuk setiap elemen dalam daftar
    for i in range(n):
        
        # Pengecekan elemen dari indeks pertama hingga indeks ke-(n-i-1)
        for j in range(0, n-i-1):
            
            # Jika jumlah halaman buku saat ini lebih besar daripada jumlah halaman buku berikutnya, tukar posisinya
            if books[j]["jumlah_halaman"] > books[j+1]["jumlah_halaman"]:
                books[j], books[j+1] = books[j+1], books[j]

# Daftar buku yang perlu diurutkan
daftar_buku = [
    {"judul": "Harry Potter and the Sorcerer's Stone", "penulis": "J.K. Rowling", "jumlah_halaman": 320},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "jumlah_halaman": 281},
    {"judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "jumlah_halaman": 180},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "jumlah_halaman": 432},
    {"judul": "1984", "penulis": "George Orwell", "jumlah_halaman": 328}
]

# Memanggil fungsi bubble_sort_books untuk mengurutkan daftar buku berdasarkan jumlah halaman
bubble_sort_books(daftar_buku)

# Menampilkan daftar buku yang telah diurutkan berdasarkan jumlah halaman secara ascending
print("Daftar buku yang diurutkan berdasarkan jumlah halaman secara ascending:")
for buku in daftar_buku:
    print("Judul:", buku["judul"])
    print("Penulis:", buku["penulis"])
    print("Jumlah Halaman:", buku["jumlah_halaman"])
    print()