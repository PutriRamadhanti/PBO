class siswa:
    #class variabel
    jumlah_siswa = 0
    #konstruktor
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa =+ 1
    #methode
    def viewSiswa(self):
        print("--------------------")
        print("Data Siswa")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Alamat : ", self.alamat)
        print("--------------------")

    def viewNilai(self):
        print("Data Siswa")
        print("Nama : ", self.nama)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("--------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ",rata)
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan : ", keterangan)

#instansiasi objek
siswa1 = siswa("Vita", "XI IPS", "Sleman", [92, 86, 78, 72])
siswa2 = siswa("Ardi", "XI MIPA 7", "Yogyakarta", [96, 86, 52, 70])
#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)
#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)

#Putri Ramadhanti
