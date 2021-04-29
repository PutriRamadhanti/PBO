class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

putri = Siswa(16187, "Putri Ramadhanti", "XI MIPA 5")

print(putri.getnis())
putri.setnis(16200)
print(putri.getnis())

#Putri Ramadhanti
