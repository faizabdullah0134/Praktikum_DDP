# Program ini akan menghitung rata-rata dari sejumlah angka yang diinput oleh pengguna
# Pertama, perintah input() akan meminta pengguna untuk memasukkan sebuah nilai, yang kemudian disimpan di dalam variabel inp
# Variabel inp akan dikonversi menjadi tipe integer dengan menggunakan fungsi int()
# Selanjutnya, variabel total diinisialisasi dengan nilai 0. Variabel ini akan digunakan untuk menyimpan jumlah dari semua angka yang diinput
# Kemudian, perintah for akan memulai looping dengan mengiterasi variabel i dengan nilai-nilai yang ditentukan oleh fungsi range()
# Fungsi range() akan mengembalikan sebuah objek yang menyimpan urutan angka dari 0 hingga inp-1
# Setiap iterasi, perintah input() akan meminta pengguna untuk memasukkan sebuah angka, yang kemudian disimpan di dalam variabel nilai
# Variabel nilai juga akan dikonversi menjadi tipe integer dengan menggunakan fungsi int()
# Selanjutnya, nilai dari nilai akan ditambahkan ke dalam total
# Setelah semua iterasi selesai, looping akan berakhir dan program akan melanjutkan ke perintah selanjutnya
# Kemudian, variabel ratarata dihitung dengan mengelompokkan jumlah dari semua angka yang diinput dengan banyaknya angka tersebut (inp)
# Terakhir, perintah print() akan mencetak hasil dari ratarata ke layar

inp = int(input("Masukkan banyaknya angka: "))
total = 0
for i in range(inp):
    nilai = int(input("Masukkan angka: "))
    total += nilai
 
ratarata = total / inp

print("Rata rata = ", ratarata)