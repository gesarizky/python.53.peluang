# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
ns = int(input("Masukan Nilai Banyaknya Kejadian (nS) : "))
na = int(input("Masukan Nilai Kejadian (n): "))
n = int(input("Masukan Nilai Banyak Percobaan (N): "))

# Mengkonversi
pa = na / ns
fh = pa * n


# Menampilkan Hasil
print('==========================================================')
print('Maka Nilai Peluang =',pa)
print('Maka Nilai Frekuensi Harapan =',fh)
print('==========================================================')
