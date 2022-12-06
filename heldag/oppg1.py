import csv
from pathlib import Path

file = Path(__file__).parent / "adresser.csv"
address_list = []
lists = []

sortby = input("Sort by 1: last name, 2: last name reversed, 3: address, 4: postnr, 5:post place 6: search for postnr \n")

with open(file, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        address_list.append({'name': row[0], 'address': row[1], 'postnr': row[2]})

with open('adresser.txt', encoding="utf-8") as f:
    lines = f.read()
    lines = lines.replace("\n\n",",")
    lines = lines.replace("\n",",")

for line in lines.split(","):
    lists.append(line)

i = 0
while i < len(lists)-2:
    address_list.append({'name': lists[i], 'address': lists[i+1], 'postnr': lists[i+2]})
    i+=3

def sort_by_lastname(address_list):
    return sorted(address_list, key=lambda d: d['name'].split()[-1])

def sort_by_lastname_reversed(address_list):
    return sorted(address_list, key=lambda d: d['name'].split()[-1], reverse=True)

def sort_by_address(address_list):
    return sorted(address_list, key=lambda d: d['address'].split()[1:])

def sort_by_postnr(address_list):
    return sorted(address_list, key=lambda d: d['postnr'].split()[0])

def sort_by_postplace(address_list):
    return sorted(address_list, key=lambda d: d['postnr'].split()[1:])

if sortby == "1":
    output = sort_by_lastname(address_list)
    print(*output,sep='\n')
elif sortby =="2":
    output = sort_by_lastname_reversed(address_list)
    print(*output,sep='\n')
elif sortby =="3":
    output = sort_by_address(address_list)
    print(*output,sep='\n')
elif sortby =="4":
    output = sort_by_postnr(address_list)
    print(*output,sep='\n')
elif sortby =="5":
    output = sort_by_postplace(address_list)
    print(*output,sep='\n')
elif sortby =="6":
    search = input("Search for postnr: ")
    for i in range(len(address_list)):
        if search in address_list[i]["postnr"]:
            output = address_list[i]["name"], address_list[i]["address"], address_list[i]["postnr"]
    print(*output,sep='\n')

print("There are", len(address_list), "addresses in the list")