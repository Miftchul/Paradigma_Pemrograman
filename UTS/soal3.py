# Data disimpan dalam list (array) berisi dictionary
buku_perpustakaan = []

# Fungsi tambah buku
def tambah_buku(judul, penulis, tahun):
    buku = {
        'judul': judul.strip(),
        'penulis': penulis.strip(),
        'tahun': tahun
    }
    buku_perpustakaan.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan.")

# Fungsi hapus buku
def hapus_buku(judul):
    global buku_perpustakaan
    buku_perpustakaan = [b for b in buku_perpustakaan if b['judul'].lower() != judul.lower()]
    print(f"Buku '{judul}' telah dihapus jika ditemukan.")

# Fungsi cari buku
def cari_buku(judul):
    hasil = [b for b in buku_perpustakaan if judul.lower() in b['judul'].lower()]
    if hasil:
        print("Hasil pencarian:")
        for b in hasil:
            print(f"- {b['judul']} oleh {b['penulis']} ({b['tahun']})")
    else:
        print("Buku tidak ditemukan.")

# Fungsi tampilkan semua buku
def tampilkan_buku():
    if not buku_perpustakaan:
        print("Belum ada buku di perpustakaan.")
    else:
        print("Daftar Buku:")
        for i, b in enumerate(buku_perpustakaan, 1):
            print(f"{i}. {b['judul']} - {b['penulis']} ({b['tahun']})")

# Menu utama (interface CLI)
def menu():
    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Cari Buku")
        print("4. Tampilkan Semua Buku")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            judul = input("Judul: ")
            penulis = input("Penulis: ")
            tahun = input("Tahun: ")
            tambah_buku(judul, penulis, tahun)
        elif pilihan == '2':
            judul = input("Judul yang ingin dihapus: ")
            hapus_buku(judul)
        elif pilihan == '3':
            judul = input("Judul yang dicari: ")
            cari_buku(judul)
        elif pilihan == '4':
            tampilkan_buku()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan aplikasi
menu()
