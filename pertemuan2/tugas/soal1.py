# Program ini akan mencetak angka dari 100 hingga 1 dengan kelipatan 2, yaitu 100, 98, 96, dst
# Perintah for akan mengiterasi variabel i dengan nilai-nilai yang ditentukan oleh fungsi range()
# Fungsi range() akan mengembalikan sebuah objek yang menyimpan urutan angka dari 100 hingga 1, dengan kelipatan 2 (karena ada argumen ketiga yaitu -2)
# Setiap iterasi, perintah print() akan mencetak nilai dari i, diikuti oleh karakter koma dan spasi (karena ada argumen end=", ")
# Setelah semua iterasi selesai, looping akan berakhir dan program akan berakhir juga

for i in range(100, 1, -2):
    print(i, end=", ")