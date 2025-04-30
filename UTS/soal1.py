# Pendekatan Imperatif
inventory = []

def tambah_barang(nama, stok, harga):
    inventory.append({'nama': nama, 'stok': stok, 'harga': harga})

def kurangi_stok(nama, jumlah):
    for barang in inventory:
        if barang['nama'] == nama:
            barang['stok'] -= jumlah

def tampilkan_laporan():
    for barang in inventory:
        print(f"{barang['nama']} - Stok: {barang['stok']} - Harga: {barang['harga']}")

# Penggunaan
tambah_barang("Mouse", 10, 150000)
kurangi_stok("Mouse", 2)
tampilkan_laporan()
print("Imperatif selesai")



# Pendekatan OOP
class Barang:
    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.stok = stok
        self.harga = harga

    def kurangi_stok(self, jumlah):
        self.stok -= jumlah

    def tampilkan_info(self):
        print(f"{self.nama} - Stok: {self.stok} - Harga: {self.harga}")

class Inventaris:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def tampilkan_laporan(self):
        for barang in self.daftar_barang:
            barang.tampilkan_info()

# Penggunaan
gudang = Inventaris()
mouse = Barang("Mouse", 10, 150000)
gudang.tambah_barang(mouse)
mouse.kurangi_stok(2)
gudang.tampilkan_laporan()
print("OOP selesai")
