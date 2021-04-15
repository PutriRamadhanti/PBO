class Kucing:
    '''Dasar kelas untuk semua kucing'''
    jumlah_kucing = 0

    def __init__(self, nama, kelamin, umur):
        self.nama = nama
        self.kelamin = kelamin
        self.umur = umur
        Kucing.jumlah_kucing += 1

    def tampilkan_jumlah(self):
        print("Total kucing:", Kucing.jumlah_kucing)

    def tampilkan_profil(self):
        print("Nama :",self.nama)
        print("Kelamin :",self.kelamin)
        print("Umur :",self.umur)

#membuat objek pertama dari kelas karyawan
kucing1 = Kucing("Tom", "Jantan", "2 tahun")
#membuat objek kedua dari kelas karyawan
kucing2 = Kucing("Angela", "Betina", "11 bulan")

kucing1.tampilkan_profil()
kucing2.tampilkan_profil()

print("Total kucing:", Kucing.jumlah_kucing)

#Putri Ramadhanti
