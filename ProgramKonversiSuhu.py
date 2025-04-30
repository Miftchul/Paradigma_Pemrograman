def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Pilih konversi (1: C ke F, 2: F ke C): ")

if choice == '1':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    print("Hasil dalam Fahrenheit:", celsius_to_fahrenheit(celsius))
elif choice == '2':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    print("Hasil dalam Celsius:", fahrenheit_to_celsius(fahrenheit))
else:
    print("Pilihan tidak valid")