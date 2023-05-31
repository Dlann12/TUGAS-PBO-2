class Mahasiswa:  # Class Mahasiswa
    def __init__(self, nama, nim, jurusan):  # atribut didalamnya
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):  # memuat agar atribut didalam class bekerja
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:  # class jurusan
    def __init__(self, nama_jurusan):  # atribut didalam classs ini
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):  # function untuk menambahkan mahasiswa
        self.DaftarMahasiswa.append(
            mahasiswa
        )  # masukkan append sebagai kode penambahan

    def tampilkan_daftar_mahasiswa(
        self,
    ):  # function untuk menampilkan daftar mahasiswa setelah nanti ditambahkan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for (
            mahasiswa
        ) in (
            self.DaftarMahasiswa
        ):  # melakukan perulangan sampai daftar dalam mahasiswa habis
            print("- Nama:", mahasiswa.nama)
            print("  NIM :", mahasiswa.nim)


class Universitas:  # class universitas
    def __init__(self, nama_universitas):  # atribut diidalamnya
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):  # function menambahkan jurusan
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):  # funtion untuk menampilkan jurusan
        print("Daftar Jurusan di", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("- Nama Jurusan:", jurusan.NamaJurusan)


universitas_xyz = Universitas("XYZ University")  # Membuat objek Universitas
jurusan_ti = Jurusan("Teknik Informatika")  # Membuat objek Jurusan
universitas_xyz.tambah_jurusan(jurusan_ti)

mahasiswa_1 = Mahasiswa(
    "Fadlan Dwi Febrio", "G1A022051", jurusan_ti
)  # Membuat objek Mahasiswa 1
mahasiswa_2 = Mahasiswa("Andi ", "1SD112B", jurusan_ti)  # Membuat objek Mahasiswa 2

jurusan_ti.tambah_mahasiswa(mahasiswa_1)  # Menambahkan Mahasiswa 1
jurusan_ti.tambah_mahasiswa(mahasiswa_2)  # Menambahkan Mahasiswa 2

jurusan_ti.tampilkan_daftar_mahasiswa()  # Menampilkan daftar mahasiswa yang terdaftar
