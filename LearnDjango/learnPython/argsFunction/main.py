# args

# masukkan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 170, 40)

def fungsi(dataList):
    data = dataList.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]

    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong", 100, 120])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]

    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung", 120, 120)

# studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"Hasil = {hasil}")