// KODE INI BISA DIJALANKAN LEWAT ONLINE PASCAL COMPILER
// https://www.onlinegdb.com/online_pascal_compiler

program MiniProjectBelanja;

const
  MaksItem = 100;
  HargaMax = 100000.0;

type
  TItem = record
    nama: string; // Menggunakan string tanpa panjang
    jumlah: integer;
    harga: real;
    subtotal: real;
  end;

var
  daftarBelanja: array[1..MaksItem] of TItem;
  i, totalItem: integer;
  totalBiaya: real;

begin
  writeln('Masukkan jumlah item yang dibeli: ');
  readln(totalItem);

  if (totalItem < 1) or (totalItem > MaksItem) then
  begin
    writeln('[!] Jumlah item harus antara 1 hingga ', MaksItem);
    halt;
  end;

  i := 1;
  while i <= totalItem do
  begin
    writeln;
    writeln('Item ke-', i, ':');

    writeln('  Nama item        : ');
    readln(daftarBelanja[i].nama);

    writeln('  Jumlah           : ');
    readln(daftarBelanja[i].jumlah);
    if daftarBelanja[i].jumlah < 0 then
    begin
      writeln('  [!] Jumlah tidak boleh negatif. Ulangi input.');
      continue; // Ulangi input untuk item yang sama
    end;

    writeln('  Harga per item   : ');
    readln(daftarBelanja[i].harga);
    if (daftarBelanja[i].harga < 0) or (daftarBelanja[i].harga > HargaMax) then
    begin
      writeln('  [!] Harga tidak valid. Maksimal: Rp ', HargaMax:0:2);
      continue; // Ulangi input untuk item yang sama
    end;

    daftarBelanja[i].subtotal := daftarBelanja[i].jumlah * daftarBelanja[i].harga;
    inc(i); // Lanjut ke item berikutnya
  end;

  writeln('========================================');
  writeln('            RINCIAN BELANJA             ');
  writeln('========================================');
  totalBiaya := 0;
  for i := 1 to totalItem do
  begin
    writeln(i, '. ', daftarBelanja[i].nama);
    writeln('   Jumlah: ', daftarBelanja[i].jumlah, ' | Harga: Rp ', daftarBelanja[i].harga:0:2, 
            ' | Subtotal: Rp ', daftarBelanja[i].subtotal:0:2);
    totalBiaya := totalBiaya + daftarBelanja[i].subtotal;
  end;

  writeln('========================================');
  writeln('TOTAL BIAYA: Rp ', totalBiaya:0:2);
  writeln('========================================');
end.
