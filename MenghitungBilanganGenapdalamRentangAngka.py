# Program untuk menghitung bilangan genap dalam rentang angka tertentu
start = int(input("Masukkan angka awal: "))
end = int(input("Masukkan angka akhir: "))

even_numbers = []
for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)

print("Bilangan genap dalam rentang tersebut:", even_numbers)