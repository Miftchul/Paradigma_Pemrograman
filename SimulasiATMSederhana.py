saldo = 1000000  # Saldo awal

def cek_saldo():
    print("Saldo Anda: Rp", saldo)

def tarik_tunai(jumlah):
    global saldo
    if jumlah > saldo:
        print("Saldo tidak mencukupi!")
    else:
        saldo -= jumlah
        print("Penarikan berhasil! Sisa saldo: Rp", saldo)

def setor_tunai(jumlah):
    global saldo
    saldo += jumlah
    print("Setoran berhasil! Saldo baru: Rp", saldo)

while True:
    print("\nATM Sederhana")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        cek_saldo()
    elif pilihan == '2':
        jumlah = int(input("Masukkan jumlah penarikan: "))
        tarik_tunai(jumlah)
    elif pilihan == '3':
        jumlah = int(input("Masukkan jumlah setoran: "))
        setor_tunai(jumlah)
    elif pilihan == '4':
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi!")