import os

print("Lokasi program berjalan:")
print(os.getcwd())

total_ipk_kelas = 0

with open(r"J:\BUAT KAMPUS\Semester 2\Dasar Pemrograman\Tugas Sesi 12\hasil_ipk.txt", "w") as file:

    while True:
        try:
            jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
            break
        except ValueError:
            print("Input harus berupa angka!")

    file.write("HASIL PERHITUNGAN IPK MAHASISWA\n")
    file.write("=" * 35 + "\n")

    for i in range(jumlah_mahasiswa):

        print(f"\nMahasiswa ke-{i+1}")
        nama_mahasiswa = input("Nama mahasiswa: ")

        while True:
            try:
                jumlah_mk = int(input("Jumlah mata kuliah: "))
                break
            except ValueError:
                print("Input harus berupa angka!")

        total_mutu = 0
        total_sks = 0

        for j in range(jumlah_mk):

            print(f"\nMata kuliah {j+1}")
            nama_mk = input("Nama mata kuliah: ")

            while True:
                try:
                    sks = int(input("Jumlah SKS: "))
                    break
                except ValueError:
                    print("Input SKS harus berupa angka!")

            nilai = input("Nilai huruf (A/B/C/D/E): ").upper()

            if nilai == "A":
                bobot = 4
            elif nilai == "B":
                bobot = 3
            elif nilai == "C":
                bobot = 2
            elif nilai == "D":
                bobot = 1
            else:
                bobot = 0

            mutu = bobot * sks

            total_mutu += mutu
            total_sks += sks

        ipk = total_mutu / total_sks

        print(f"\nIPK {nama_mahasiswa} = {ipk:.2f}")

        file.write(f"{nama_mahasiswa} : {ipk:.2f}\n")

        total_ipk_kelas += ipk

    rata_rata = total_ipk_kelas / jumlah_mahasiswa

    print(f"\nRata-rata IPK kelas = {rata_rata:.2f}")

    file.write("\n")
    file.write(f"Rata-rata IPK kelas : {rata_rata:.2f}\n")

print("\nData berhasil disimpan ke file hasil_ipk.txt")