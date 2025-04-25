# write external data
# akan membuat file baru jika tidak ada
# akan menimpa isinya

with open("data.txt",'w', encoding="utf-8") as file:
    file.write("allen")

with open("data.txt",'w', encoding="utf-8") as file:
    file.write("quiland")

# 2. mode append

with open("data1.txt",'w', encoding="utf-8") as file:
    file.write("allen \n")

with open("data1.txt",'a', encoding="utf-8") as file:
    file.write("quiland\n")

with open("data1.txt",'a', encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# mode r+

with open("data1.txt",'r+', encoding="utf-8") as file:
    file.write("menambah dengan r+")