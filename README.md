# TUGAS-PBO-2
Andi adalah seorang mahasiswa Informatika yang sedang belajar konsep Pemrograman Berorientasi Objek (PBO) menggunakan bahasa pemrograman Python. Ia ingin membuat program sederhana untuk mengelola data mahasiswa di sebuah universitas. Andi memutuskan untuk membuat tiga kelas objek yang saling berhubungan: Mahasiswa, Jurusan, dan Universitas.

Kelas Mahasiswa:
Kelas Mahasiswa memiliki atribut sebagai berikut:
Nama (string)
NIM (string)
Jurusan (objek dari kelas Jurusan)

Kelas Mahasiswa memiliki metode sebagai berikut:
init(self, nama, nim, jurusan): inisialisasi atribut Nama, NIM, dan Jurusan
tampilkan_info(self): menampilkan informasi Nama, NIM, dan nama Jurusan mahasiswa
Kelas Jurusan:
Kelas Jurusan memiliki atribut sebagai berikut:
NamaJurusan (string)
DaftarMahasiswa (daftar objek Mahasiswa)

Kelas Jurusan memiliki metode sebagai berikut:
init(self, nama_jurusan): inisialisasi atribut NamaJurusan dan DaftarMahasiswa
tambah_mahasiswa(self, mahasiswa): menambahkan objek Mahasiswa ke dalam DaftarMahasiswa
tampilkan_daftar_mahasiswa(self): menampilkan daftar mahasiswa yang terdaftar dalam Jurusan
Kelas Universitas:
Kelas Universitas memiliki atribut sebagai berikut:
NamaUniversitas (string)
DaftarJurusan (daftar objek Jurusan)

Kelas Universitas memiliki metode sebagai berikut:
init(self, nama_universitas): inisialisasi atribut NamaUniversitas dan DaftarJurusan
tambah_jurusan(self, jurusan): menambahkan objek Jurusan ke dalam DaftarJurusan
tampilkan_daftar_jurusan(self): menampilkan daftar jurusan yang ada di Universitas

Andi ingin menggunakan programnya untuk mengelola data mahasiswa dan jurusan di Universitas XYZ.

Bantulah Andi untuk mengimplementasikan tiga kelas objek tersebut agar programnya dapat berjalan dengan baik.
