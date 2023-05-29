# python-sort

Bubble sort adalah salah satu algoritma pengurutan sederhana yang digunakan untuk mengurutkan elemen dalam sebuah list. Algoritma ini bekerja dengan membandingkan pasangan elemen berturut-turut dalam list dan menukar posisinya jika ditemukan elemen yang lebih besar berada di posisi sebelumnya. Proses ini berulang-ulang sampai semua elemen terurut dengan benar.

Berikut adalah penjelasan langkah demi langkah tentang bagaimana bubble sort bekerja dalam Python:

1. Mulai dengan sebuah list yang akan diurutkan.
2. Bandingkan elemen pertama dengan elemen kedua. Jika elemen pertama lebih besar dari elemen kedua, tukar posisi mereka.
3. Lanjutkan langkah sebelumnya, membandingkan elemen kedua dengan elemen ketiga, dan seterusnya, hingga mencapai elemen sebelum terakhir.
4. Setelah satu iterasi selesai, elemen terbesar akan berada di posisi paling akhir dari list.
5. Ulangi langkah-langkah sebelumnya untuk iterasi kedua, ketiga, dan seterusnya, tetapi kali ini hanya sampai elemen sebelumnya dari elemen terakhir pada iterasi sebelumnya. Hal ini dikarenakan setelah setiap iterasi, elemen terbesar akan "naik" ke posisi yang benar.

Contoh :

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
my_list = [5, 2, 8, 12, 1]
bubble_sort(my_list)
print(my_list)
