import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog

# Membuka file catalog.json
with open('files/catalog.json') as f:
    data_json = json.load(f)

# Inisialisasi daftar untuk menyimpan instance objek yang sesuai dengan jenis item
books = []
magazines = []
cds = []
dvds = []

# Iterate melalui setiap item dalam data JSON dan membuat instance objek yang sesuai
for item in data_json:
    source = item['source']
    if source == 'book':
        books.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif source == 'magazine':
        magazines.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']
        ))
    elif source == 'cd':
        cds.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist']
        ))
    elif source == 'dvd':
        dvds.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            genre=item['genre']
        ))

# Menyusun katalog dengan semua item yang sudah dibuat
catalog_all = [books, magazines, cds, dvds]

# Mencari item dengan input tertentu
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

# Menampilkan hasil pencarian
for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')
