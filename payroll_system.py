
# ==========================================
# SISTEM PENGGAJIAN KARYAWAN
# Pemrograman Berorientasi Objek (OOP)
# ==========================================

# Fungsi untuk menampilkan angka dalam Rupiah
def format_rupiah(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")


# ==========================================
# 1. CLASS INDUK (SUPERCLASS)
# ==========================================
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = 0
        self.gaji_pokok = gaji_pokok

    # Getter untuk mengambil gaji pokok
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah gaji pokok
    @gaji_pokok.setter
    def gaji_pokok(self, nilai):
        if nilai <= 0:
            print("PERINGATAN: Gaji pokok harus lebih dari 0!")
        else:
            self.__gaji_pokok = nilai

    # Method menghitung total gaji
    def hitung_gaji_total(self):
        return self.__gaji_pokok

    # Method menampilkan informasi karyawan
    def tampilkan_info(self):
        print("Nama          :", self.nama)
        print("ID Karyawan   :", self.id_karyawan)
        print("Gaji Pokok    :", format_rupiah(self.gaji_pokok))


# ==========================================
# 2. CLASS ANAK - KARYAWAN TETAP
# ==========================================
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # Menghitung gaji pokok + tunjangan
    def hitung_gaji_total(self):
        return self.gaji_pokok + self.tunjangan

    # Menampilkan informasi karyawan tetap
    def tampilkan_info(self):
        print("\n=== KARYAWAN TETAP ===")
        super().tampilkan_info()
        print("Tunjangan     :", format_rupiah(self.tunjangan))
        print("Total Gaji    :", format_rupiah(self.hitung_gaji_total()))


# ==========================================
# 3. CLASS ANAK - KARYAWAN KONTRAK
# ==========================================
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok,
                 jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Menghitung gaji pokok + uang lembur
    def hitung_gaji_total(self):
        total_lembur = self.jam_lembur * self.tarif_lembur
        return self.gaji_pokok + total_lembur

    # Menampilkan informasi karyawan kontrak
    def tampilkan_info(self):
        print("\n=== KARYAWAN KONTRAK ===")
        super().tampilkan_info()

        total_lembur = self.jam_lembur * self.tarif_lembur

        print("Jam Lembur    :", self.jam_lembur, "jam")
        print("Tarif Lembur  :", format_rupiah(self.tarif_lembur))
        print("Total Lembur  :", format_rupiah(total_lembur))
        print("Total Gaji    :", format_rupiah(self.hitung_gaji_total()))


# ==========================================
# 4. MAIN PROGRAM
# ==========================================
if __name__ == "__main__":

    # Membuat objek karyawan
    karyawan_tetap = KaryawanTetap(
        "Budi Santoso", "KT001", 7000000, 1500000
    )

    karyawan_kontrak = KaryawanKontrak(
        "Siti Rahma", "KK001", 4500000, 20, 50000
    )

    # Menyimpan objek ke dalam list
    daftar_karyawan = [karyawan_tetap, karyawan_kontrak]

    # ======================================
    # DEMONSTRASI POLYMORPHISM
    # ======================================
    print("======================================")
    print("      DEMONSTRASI POLYMORPHISM")
    print("======================================")

    for karyawan in daftar_karyawan:
        karyawan.tampilkan_info()

    # ======================================
    # DEMONSTRASI ENCAPSULATION
    # ======================================
    print("\n======================================")
    print("      DEMONSTRASI ENCAPSULATION")
    print("======================================")

    print("\nGaji pokok sebelum diubah:")
    print(format_rupiah(karyawan_tetap.gaji_pokok))

    # Mengubah gaji dengan nilai tidak valid
    print("\nMengubah gaji menjadi -500000:")
    karyawan_tetap.gaji_pokok = -500000

    # Mengubah gaji dengan nilai valid
    print("\nMengubah gaji menjadi 8000000:")
    karyawan_tetap.gaji_pokok = 8000000

    # Menampilkan hasil perubahan
    print("\nData karyawan setelah perubahan:")
    karyawan_tetap.tampilkan_info()
