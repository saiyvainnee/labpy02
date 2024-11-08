
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
