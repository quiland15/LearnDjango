# Lambda
# anonymous function

# Lambda Function
# fungsi biasa
def kuadrat(angka):
    return angka**2

print(f"\nIni adalah hasil dari fungsi kuadrat = {kuadrat(3)}\n")

# dengan lambda

kuadrat = lambda angka:angka**2

print(f"Hasil kuadrat lambda = {kuadrat(5)}\n")

# 2 argument

pangkat = lambda num,pow : num**pow
print(f"Hasil lambda pangkat = {pangkat(4, 2)}\n")

# Kegunaan lambda itu apa sebenarnya

# 1. Sorting list

dataList = ['otong', 'ucup', 'dudung']
dataList.sort()
print(f"Sorted List = {dataList}\n")

dataList.sort(key=len)
print(f"Sorted List by len = {dataList}\n")

# sort pakai lambda
dataList = ['otong', 'ucup', 'dudung']
dataList.sort(key=lambda nama:len(nama))
print(f"Sorted List by lambda = {dataList}\n")

# filter
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12]
dataAngkaBaru = list(filter(lambda x:x<5,dataAngka))
print(dataAngkaBaru)
# genap kasus
dataGenap = list(filter(lambda x:(x % 2 == 0 ),dataAngka))
print(dataGenap)
# ganjil kasus
dataGanjil = list(filter(lambda x:(x%2 != 0),dataAngka))
print(dataGanjil)
# data kelipatan 3
data3 = list(filter(lambda x:(x % 3 == 0),dataAngka))
print(data3)

# anonymous function

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"\nPangkat 2 = {pangkat2(5)}\n")