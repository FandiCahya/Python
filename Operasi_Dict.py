data_list = ['Bambang','Marpok','Ajih']

print(data_list[1])

# dictionary (dict) -> associative array
# identifier -> key
data_dict = {
    'key' : 'value',
    'ba' : 'Bambang',
    'ma' : 'Marpok',
    'aj' : 'Ajih',
    'no' : 100,
    'list' : data_list
}

# Panjang Dict
LENG = len(data_dict)
print(f"Panjang Dictionary : {LENG}")

# Mengecek Key Exist
KEY = "ba"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict : {CHECKKEY}")

# Mengakses dengan get
print(data_dict.get("ba"))
print(data_dict.get("ga","Tidak Ditemukan"))

# Update Data
data_dict["ba"] = "Bambang Anake Sholeh"
print(data_dict)
data_dict["io"] = "Ayon bapake wawan"
print(data_dict)

data_dict.update({"ma":"Markonah"})
print("\nUpdate data Pakai .update\n",data_dict)
data_dict.update({"ha":"Hanoman"})
print("\n",data_dict)

# Mengahapus Data
del data_dict["ha"]
print("\nDelete data\n",data_dict)