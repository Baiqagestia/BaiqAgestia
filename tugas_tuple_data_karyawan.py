# Data karyawan menggunakan tuple (ID, Nama, Jabatan)
karyawan = (
    (101, "Baiq Agestia Cahya Ilami", "Manager"),
    (102, "Siti Aminah", "Supervisor"),
    (103, "Sulis", "Staff"),
)

# Menampilkan data karyawan
print("Data Karyawan:")
for data in karyawan:
    print(f"ID: {data[0]}, Nama: {data[1]}, Jabatan: {data[2]}")




