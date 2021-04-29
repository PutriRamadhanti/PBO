class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #decorator
    @property
    def nis(self):
        pass

    #getter
    @nis.getter
    def nis(self):
        return self.__nis

    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis

putri = Siswa(16187, "Putri Ramadhanti", "XI MIPA 5")

print(putri.nis)
putri.nis = 16200
print(putri.nis)

#Putri Ramadhanti
