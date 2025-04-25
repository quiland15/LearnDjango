# type hints untuk fungsi 


# penggunaan type hints
# ini memiliki argument

def fungsiDenganhints(argument:int) -> int:
    output = 10**argument
    return output

hasil = fungsiDenganhints(2)
print(hasil)
# digunakan untuk collaborasi

def display(argument:str):
    print(argument)

display("ucup")