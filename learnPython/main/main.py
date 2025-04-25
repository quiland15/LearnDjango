# __main__

print(f"nilai __name__ pada main.py = '{__name__}'")
# __name__ pada file program external

import main.package.fungsi as fungsi

# __name__ == "__main__" jika ada dalam program utama

# contoh penggunaan main

# deklarasi

def fungsiTambah(a,b):
    return a + b

# fungsi utama

if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsiTambah(angka1, angka2)
    print(f"Hasil Tambah = {hasil}")

# import package
import package