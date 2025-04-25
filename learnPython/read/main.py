# tutorial membaca file external

print(3*"=", "Membaca file txt", 3*"=")
file = open("data.txt",mode="r")

print(f"Status read : {file.readable()}")
print(f"Status Write : {file.writable()}")
 
# print(file.read()) / membaca keseluruhan

# print(file.readline(), end=" ") #baca baris pertama
# print(file.readline(), end=" ") #bace baris kedua

# baca semua baris sebagai list
# print(file.readlines())


print(f"Apakah file sudah di close: {file.closed}")
file.close()
print(f"Apakah file sudah di close: {file.closed}")

# salah satu teknik membuka file di python

print("\n", 3*"=", "Membaca file txt dengan with", 3*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content, end=" ")
    print(f"Apakah file sudah di close: {file.closed}")