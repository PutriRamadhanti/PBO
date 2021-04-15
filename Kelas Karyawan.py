class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, alamat, gaji, umur):
        self.nama = nama
        self.alamat = alamat
        self.gaji = gaji
        self.umur = umur
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :",self.nama)
        print("Alamat :",self.alamat)
        print("Gaji :",self.gaji)
        print("Umur :",self.umur)

#membuat objek pertama dari kelas karyawan
karyawan1 = Karyawan("Susi", "Ngestiharjo", 3000000, 23)
#membuat objek kedua dari kelas karyawan
karyawan2 = Karyawan("Kevin", "Kuncen", 5000000, 26)
#membuat objek ketiga  dari kelas karyawan
karyawan3 = Karyawan("Rizki", "Bugisan", 4500000, 24)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()

print("Total karyawan:", Karyawan.jumlah_karyawan)

#Putri Ramadhanti

