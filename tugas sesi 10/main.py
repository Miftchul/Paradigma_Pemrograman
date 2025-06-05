# Fakta ayah(OrangTua, Anak)
ayah_facts = {
    ('joko', 'andi'),
    ('andi', 'bambang')
}

# Fakta ibu(OrangTua, Anak)
ibu_facts = {
    ('sari', 'andi'),
    ('siti', 'bambang')
}

# Aturan kakek(X, Z)
def kakek(X, Z):
    # kakek(X, Z) :- ayah(X, Y), (ayah(Y, Z); ibu(Y, Z)).
    for Y_ayah in [y for (parent, y) in ayah_facts if parent == X]:
        if (Y_ayah, Z) in ayah_facts or (Y_ayah, Z) in ibu_facts:
            return True
    return False

# Query otomatis saat program dijalankan
def main():
    if kakek('joko', 'bambang'):
        print('Joko adalah kakek dari Bambang')
    else:
        print('Bukan kakek')

if __name__ == "__main__":
    main()