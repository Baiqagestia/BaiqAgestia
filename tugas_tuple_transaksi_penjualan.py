
print("\n===== SELAMAT DATANG USER [BAIQ AGESTIA CAHYA ILAMI] =====")

# List untuk menyimpan transaksi (ID Transaksi, ID Produk, Jumlah)
transaksi_penjualan = [
    (1001, "P001", 2),
    (1002, "P002", 5),
    (1003, "P001", 1),
]

# Menampilkan daftar transaksi
print("\nData Transaksi Penjualan:")
print("="*50)
for transaksi in transaksi_penjualan:
    print(f"ID Transaksi: {transaksi[0]}, ID Produk: {transaksi[1]}, Jumlah: {transaksi[2]}")


# DENGAN USER INPUT
print("="*50)

# List untuk menyimpan transaksi
transaksi_penjualan = []

# Menentukan jumlah transaksi yang akan dimasukkan
jumlah_transaksi = int(input("\nMasukkan jumlah transaksi baru: "))

# Loop untuk input data transaksi
for i in range(jumlah_transaksi):
    print(f"\nMasukkan data transaksi ke-{i+1}:")
    id_transaksi = input("ID Transaksi: ")
    id_produk = input("ID Produk: ")
    jumlah = int(input("Jumlah: "))

    # Menyimpan transaksi dalam tuple dan menambahkannya ke list
    transaksi_penjualan.append((id_transaksi, id_produk, jumlah))


# Menampilkan daftar transaksi yang telah dimasukkan
print("\nData Transaksi Penjualan Baru:")
print("="*50)
for transaksi in transaksi_penjualan:
    print(f"ID Transaksi: {transaksi[0]}, ID Produk: {transaksi[1]}, Jumlah: {transaksi[2]}")
print("="*50) 
