# Program ini menerima input berupa sebuah bilangan bulat dari user
# Kemudian program akan menampilkan sebuah pola yang terdiri dari # yang terbentuk dari perulangan for
# Pertama, perulangan for pertama dilakukan dengan menggunakan variabel i yang akan berjalan sebanyak inp kali
# Selanjutnya, perulangan for kedua dilakukan dengan menggunakan variabel j yang juga akan berjalan sebanyak inp kali
# Setiap perulangan for kedua selesai, maka akan ada pindah baris (newline) yang dicetak dengan menggunakan perintah print()
# Sehingga akan terbentuk pola # sebanyak inp x inp kali

inp = int(input("Masukkan sebuah bilangan bulat: "))
for i in range(inp):
    for j in range(inp):
        print("#", end=" ")
    print()