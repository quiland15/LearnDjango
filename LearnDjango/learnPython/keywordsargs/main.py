# **kwargs

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} \n")

fungsi("ucup", 183, 79)

def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} \n")

fungsi(nama = "ucup", tinggi = 183, berat = 75)

# studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        print("Operasi Perkalian")
        for angka in args:
            output *= angka
    return output

hasil = math(1,2,3,4,5,6,7,8,9, option = "tambah")
print(f"Hasil Jumlah {hasil} \n")

hasil = math(1,2,3,4,5,6,7,8,9, option = "kali")
print(f"Hasil kali  = {hasil} \n")