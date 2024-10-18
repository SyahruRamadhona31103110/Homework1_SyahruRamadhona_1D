judul = 'REKRUTMEN POLSUSKA PRIA TINGKAT SLTA TAHUN 2024 PT KAI'
print(judul)
nama = input('Masukan Nama : ')
umur = int(input('Masukan Umur : '))
kewarganegaraan = input('Masukan Kewarganegaraan : ')
nilai_ijazah = float(input('Masukan Nilai Ijazah : '))
tinggi_badan = int(input('Masukan Tinggi Badan : '))
biaya_administrasi = float(input('Masukan Biaya Administrasi : '))
jenis_kelamin = input('Masukan Jenis Kelamin : ')
jenis_kelamin_yang_memenuhi = ['pria','Pria','laki laki','Laki laki']
kewarganegaraan_yang_memenuhi = ['indonesia','Indonesia']
hasil = 'SELAMAT ANDA LOLOS KE TAHAP SELANJUTNYA' if umur < 28 and kewarganegaraan in kewarganegaraan_yang_memenuhi and nilai_ijazah >= 8.0 and tinggi_badan >= 170 and biaya_administrasi == 150.000 and jenis_kelamin in jenis_kelamin_yang_memenuhi and kewarganegaraan in kewarganegaraan_yang_memenuhi else 'MOHON MAAF ANDA TIDAK LOLOS KE TAHAP SELANJUTNYA TETAP SEMANGAT'
print(hasil)