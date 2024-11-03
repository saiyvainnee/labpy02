Tugas P6
Nama Sayidina Ramadhan
Kelas TI.24.A.1
Nim:312410112
## Tiket Bioskop
Program tiket bioskop ini adalah program untuk menghitung harga Tiket bioskop. Konsepnya adalah jika user memiliki kartu member maka user akan mendapatkan diskon 20%

![image](https://github.com/user-attachments/assets/b33dcfb1-7dcb-49a4-9d87-43a387cdd5ec)
## Program akan Meminta user untuk menginputkan tipe tiket

```python
Masukkan tipe tiket (reguler/vip): vip
Apakah Anda memiliki kartu member? (ya/tidak): tidak
total harga yang harus dibayar: Rp100000.00
Masukkan tipe tiket (reguler/vip): vip
Apakah Anda memiliki kartu member? (ya/tidak): ya
total harga yang harus dibayar: Rp80000.00
PS C:\Users\SAYIDINA RAMADHAN\Desktop\vscode sayi>\
```

```python
# Mengambil input dari pengguna
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

# Menentukan harga tiket
harga_reguler = 50000
harga_vip = 100000

# Menghitung harga tiket berdasarkan tipe
if tipe_tiket == 'reguler':
    harga_tiket = harga_reguler
elif tipe_tiket == 'vip':
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

# Menghitung total harga dengan diskon jika memiliki kartu member
diskon = 0.2 if status_member == 'ya' else 0
total_harga = harga_tiket * (1 - diskon)

# Menampilkan hasil
print(f"total harga yang harus dibayar: Rp{total_harga:.2f}")
```
## Penjelasan
Deskripsi Program
Program ini dirancang untuk menghitung total harga tiket berdasarkan jenis tiket yang dibeli (reguler atau VIP) dan apakah pembeli memiliki kartu member. Berikut adalah langkah-langkah rinci dari program ini:

Definisi Harga Tiket:

Kita menetapkan harga dasar untuk dua jenis tiket:
Harga Tiket Reguler: Rp35.000
Harga Tiket VIP: Rp90.000
Input Pengguna:

Jenis Tiket: Program meminta pengguna untuk memasukkan jenis tiket yang diinginkan. Input diubah menjadi huruf kecil dan dihilangkan spasi untuk menjaga konsistensi.
Status Member: Pengguna juga diminta untuk mengkonfirmasi apakah mereka memiliki kartu member dengan cara yang sama.
Menentukan Harga Tiket:

Jika pengguna memilih tiket reguler, maka harga tiket akan diatur menjadi Rp35.000.
Jika pengguna memilih tiket VIP, harga tiket akan diatur menjadi Rp90.000.
Jika input tidak valid (tidak "reguler" atau "VIP"), program akan mencetak pesan kesalahan dan mengatur harga tiket menjadi 0.
Menghitung Diskon untuk Member:

Jika pengguna adalah member (jawaban "ya") dan tiket yang dipilih valid, diskon sebesar 20% dari harga tiket akan dihitung.
Jika pengguna bukan member atau tiket yang dipilih tidak valid, total harga tetap sama dengan harga tiket tanpa diskon.
Menampilkan Total Harga:

Jika harga tiket valid (harga tiket lebih dari 0), program akan mencetak total harga yang harus dibayar, diformat hingga dua desimal. Jika tidak, tidak ada output harga.

## 2. Kalkulator Sederhana
Program ini adalah program Kalkulator sederhana yang berfungsi untuk menghitung dua angka sesuai dengan operasi hitung yang dipilih.

```python
def kalkulator():
  """Fungsi ini membuat kalkulator sederhana"""

  # Meminta input dari pengguna
  angka1 = float(input("Masukkan angka pertama: "))
  angka2 = float(input("Masukkan angka kedua: "))
  operator = input("Masukkan operator (+, -, *, /): ")

  # Melakukan operasi berdasarkan operator yang dipilih
  if operator == '+':
    hasil = angka1 + angka2
  elif operator == '-':
    hasil = angka1 - angka2
  elif operator == '*':
    hasil = angka1 * angka2
  elif operator == '/':
    if angka2 == 0:
      print("Tidak dapat membagi dengan nol")
    else:
      hasil = angka1 / angka2
  else:
    print("Operator tidak valid")

  # Menampilkan hasil
  if 'hasil' in locals():
    print("Hasil:", hasil)

kalkulator()
```
