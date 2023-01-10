data = {}
# Memuat Class
class Data():
    def __init__(self,nama,nim,uts,uas,tugas,total):

        while True:
            user = input("\n(T)ambah, (U)bah, (H)apus, (L)ihat, (K)eluar: ")
            if user == 'k':
                print("Program Selesai Terima kasih")
                break
            elif user == 't':
                self.tambah()
            elif user == 'l':
                self.tampilkan()
            elif user == 'h':
                self.hapus()
            elif user == 'u':
                self.ubah()

# Menambahkan data
    def tambah(self):
        print("Tambah Data")
        self.nama = input("Nama           : ")
        self.nim = int(input("NIM            : "))
        self.uts = int(input("Nilai UTS      : "))
        self.uas = int(input("Nilai UAS      : "))
        self.tugas = int(input("Nilai Tugas    : "))
        self.total = self.uts*35/100 + self.uas*35/100 + self.tugas*30/100
        data[self.nama] = self.nim, self.uts, self.uas, self.tugas, self.total
# Membuat kelas baru
class Mahasiswa(Data):

# Menampilkan data
    def tampilkan(self):
        print("Tampilkan Data")
        if data.items():
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for z in data.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                    .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)
        else:
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)
        return

# Menghapus data
    def hapus(self):
        print("Hapus Data")
        self.nama = input("Masukkan Nama  : ")
        if self.nama in data.keys():
            del data[self.nama]
        else:
            print("Nama {0} Tidak Ditemukan".format(self.nama))
        return

# Mengubah data
    def ubah(self):
        print("Ubah Data")
        self.nama = input("Masukkan Nama  : ")
        if self.nama in data.keys():
            self.nim = int(input("NIM            : "))
            self.uts = int(input("Nilai UTS      : "))
            self.uas = int(input("Nilai UAS      : "))
            self.tugas = int(input("Nilai Tugas    : "))
            self.total = self.uts*35/100 + self.uas*35/100 + self.tugas*30/100
            data[self.nama] = self.nim, self.uts, self.uas, self.tugas, self.total
        else:
            print("Nama {0} tidak ditemukan".format(self.nama))


# Memanggil fungsi
dataMhs = Mahasiswa("nama","nim","uts","uas","tugas","total")
dataMhs.tambah()
dataMhs.tampilkan()
dataMhs.ubah()
dataMhs.hapus()
dataMhs.tampilkan()