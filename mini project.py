#sistem pendataan jadwal rilis  game

#tempat menyimpan data  game
data_game = []

while True:
    print("\n=== Sistem Pendataan JAdwal rilis Game ===")
    print("1. Tambah data game")
    print("2. Lihat Data game")
    print("3. ubah data game")
    print("4. hapus data game")
    print("5. keluar")

    pilihan = input("pilih menu (1-5): ")

    #menu 1: tambah data game
    if pilihan == "1":
        print("\n--- tambah data game ---")

        nama = input("nama game: ")
        platform = input("Platform: ")
        tanggal = input(" tanggal rilis: ")

        #data disimpan dalam tuple
        data = (nama, platform, tanggal)
        data_game.append(data)

        print("data game berhasil ditambahkan.")

    #menu 2: lihat data game
    elif pilihan == "2":
        print("\n--- data game ---")

        if len(data_game) == 0:
            print("belum ada data game.")
        else:
            for i,data in enumerate(data_game, start=1):
                print(
                    i,
                    ".nama:", data[0],
                    "| platform:", data[1],
                    "| tanggal:", data[2]
                )

    elif pilihan =="3":
        print("\n--- ubah data game ---")
        if len(data_game) == 0:
            print("belum ada data game.")
        else:
            print("daftar data game:")

            for i,data in enumerate(data_game, start=1):
                print(
                    i,
                    ".nama:", data[0],
                    "| platform:", data[1],
                    "| tanggal:", data [2]
                )

            try:
                nomor =int(input("masukkan nomor data yang ingin diubah: "))

                if nomor >= 1 and nomor <=len(data_game):
                    nama_baru = input("nama game baru: ")
                    platform_baru = input("platform baru: ")
                    tanggal_baru = input("tanggal rilis baru: ")

                    data_baru =(nama_baru,platform_baru,tanggal_baru)
                    data_game[nomor - 1] = data_baru

                    print("data game berhasil diubah.")
                else:
                    print("data tidak ditemukan.")

            except ValueError:
                print("Nomor data harus berupa angka.")


    elif pilihan =="4":
        print("\n--- hapus data game ---")

        if len(data_game) == 0:
            print("Belum ada data game.")
        else:
            print("Daftar Data Game:")

        for i, data in enumerate(data_game, start=1):
            print(
                i,
                ". Nama:", data[0],
                "| Platform:", data[1],
                "| Tanggal:", data[2]
            )

        try:
            nomor = int(input("Masukkan nomor data yang ingin dihapus: "))

            if nomor >= 1 and nomor <= len(data_game):
                data_game.pop(nomor - 1)
                print("Data game berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")

        except ValueError:
            print("Nomor data harus berupa angka.")


    elif pilihan =="5":
        print("program selesai.")
        break

    #pilihan salah
else:
    print("menu tidak tersedia.silakan pilih 1-5.")


    


            

    



        
