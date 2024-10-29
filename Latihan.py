# Data input
gaji_per_jam = float(input("Masukkan gaji per jam Budi: "))
jam_kerja_per_minggu = float(input("Masukkan total jam kerja per minggu: "))
minggu_kerja = 5

# 1. Menghitung pendapatan sebelum pajak
pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja_per_minggu * minggu_kerja

# 2. Menghitung pendapatan setelah pajak
pajak = 0.14 * pendapatan_sebelum_pajak
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak

# 3. Jumlah uang yang akan dihabiskan untuk membeli pakaian dan aksesoris
pengeluaran_baju_aksesoris = 0.10 * pendapatan_setelah_pajak

# 4. Jumlah uang yang akan dihabiskan untuk membeli alat tulis
pengeluaran_alat_tulis = 0.01 * pendapatan_setelah_pajak

# 5. Jumlah uang yang akan disedekahkan
sisa_setelah_belanja = pendapatan_setelah_pajak - (pengeluaran_baju_aksesoris + pengeluaran_alat_tulis)
sedekah = 0.25 * sisa_setelah_belanja

# 6. Jumlah uang yang diterima anak yatim
untuk_anak_yatim = 0.30 * sedekah

# 7. Jumlah uang yang diterima kaum dhuafa
untuk_kaum_dhuafa = 0.70 * sedekah

# Output hasil
print("1. Pendapatan sebelum pajak:", pendapatan_sebelum_pajak)
print("2. Pendapatan setelah pajak:", pendapatan_setelah_pajak)
print("3. Pengeluaran untuk baju dan aksesoris:", pengeluaran_baju_aksesoris)
print("4. Pengeluaran untuk alat tulis:", pengeluaran_alat_tulis)
print("5. Jumlah uang yang disedekahkan:", sedekah)
print("6. Uang yang diterima anak yatim:", untuk_anak_yatim)
print("7. Uang yang diterima kaum dhuafa:", untuk_kaum_dhuafa)
