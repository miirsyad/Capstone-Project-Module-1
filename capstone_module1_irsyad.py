# Capstone Project Module 1 Purwadhika - Muhammad Irsyad

# DATA SET
inventory = {
    '1B' : {'Nama' : 'Ayam Fillet','Jumlah' : 100, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '2B' : {'Nama' : 'Telur', 'Jumlah' : 50, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '3B' : {'Nama' : 'Bombai', 'Jumlah' : 50, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '4B' : {'Nama' : 'Tempe', 'Jumlah' : 150, 'Satuan' : 'pcs', 'Jenis' : 'Basah'},
    '5B' : {'Nama' : 'Pecay', 'Jumlah' : 100, 'Satuan' : 'kg', 'Jenis' : 'Basah'},

    '1K' : {'Nama' : 'Beras', 'Jumlah' : 500, 'Satuan' : 'kg', 'Jenis' : 'Kering'},
    '2K' : {'Nama' : 'Terigu', 'Jumlah' : 200, 'Satuan' : 'kg', 'Jenis' : 'Kering'},
    '3K' : {'Nama' : 'Saus Teriyaki', 'Jumlah' : 100, 'Satuan' : 'pcs', 'Jenis' : 'Kering'}
}

# Print Semua Inventaris
def printInventory():
    # Header Table
    judulInventory = ['Kode Barang', 'Nama Barang', 'Stok', 'Satuan', 'Jenis']
    outer_keys = list(inventory.keys())

    # Print List Inventaris
    print('==========Daftar Inventaris==========\n')

    # Print Header Table
    print(f'{judulInventory[0]:<20}|{judulInventory[1]:<20}|{judulInventory[2]:<20}|{judulInventory[3]:<20}|{judulInventory[4]:<20}')
    
    # Print tiap key (barang) dari Inventory
    for i in range(len(inventory)):
        print(f'''{outer_keys[i]:<20}|{inventory[outer_keys[i]]['Nama']:<20}|{inventory[outer_keys[i]]['Jumlah']:<20}|{inventory[outer_keys[i]]['Satuan']:<20}|{inventory[outer_keys[i]]['Jenis']:<20}''')

# Print Satu Item di Inventaris
def printData(input_kode):
    print(f'''
        ==========Kode Barang : {input_kode.upper()}==========
        Nama : {inventory[input_kode.upper()]['Nama']}
        Jumlah : {inventory[input_kode.upper()]['Jumlah']}
        Satuan : {inventory[input_kode.upper()]['Satuan']}
        Jenis : {inventory[input_kode.upper()]['Jenis']} ''')
    
# Menu 1: Read
def menampilkanInventaris():
    while True:
        # Tampilan # 1
        print(f'''
    ==========INVENTARIS==========

    1. MENAMPILKAN SEMUA DATA INVENTARIS
    2. MENAMPILKAN DATA INVENTARIS PILIHAN
    3. KEMBALI KE MENU UTAMA
    ''')
        # Input Sub-Menu
        input_1 = input('SILAKAN PILIH [1-3] : ').strip()

        # Kalau input tidak sesuai format
        if input_1.isnumeric() == False:
            print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

        else: 
            input_1 = int(input_1)

            # Print Semua Inventaris
            if input_1 == 1:

                # Kalau inventaris kosong, kasih tau dan gak usah print
                if len(inventory) == 0:
                    print('\nINVENTARIS KOSONG')

                # Read all
                else:
                    printInventory()

            # Print Salah Satu Data
            elif input_1 == 2:

                # Kalau inventaris kosong, kasih tau dan gak usah print
                if len(inventory) == 0:
                    print('\nINVENTARIS KOSONG')
                
                else:
                    # Minta input kode barang
                    input_kode = input('MASUKKAN KODE BARANG : ').strip()
                    
                    # key dari Data Set = Kode Barang
                    outer_keys = list(inventory.keys())

                    # Kalau Kode Barang Gak ada, kasih tau
                    if input_kode.upper() not in outer_keys:
                        print('\nKODE BARANG TIDAK ADA DI INVENTARIS')

                    # Kalau ada, print
                    else:
                        printData(input_kode.upper())

            # Kembali Ke Menu
            elif input_1 == 3:
                break
            
            # Kalau salah pilihan menu
            else:
                print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

# Menu 2: Create
def tambahInventaris():
    tambah = {}
    while True:
        # Tampilan # 2
        print(f'''
    ==========MENAMBAHKAN DATA INVENTARIS==========

    1. TAMBAH DATA
    2. KEMBALI KE MENU UTAMA
    ''')    
        # Input Sub-Menu
        input_2 = input('SILAKAN PILIH [1-2] : ').strip()

        # Kalau input tidak sesuai
        if input_2.isnumeric() == False:
            print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

        else: 
            input_2 = int(input_2)
            # Menambahkan Barang
            if input_2 == 1:
                outer_keys = list(inventory.keys())
                # Nama Baru
                tambah['Nama'] = input('MASUKKAN NAMA BARANG : ').title()

                # Jumlah Barang Baru
                while True:
                    tambah['Jumlah'] = input('MASUKKAN JUMLAH BARANG (ANGKA): ')

                    # Cek Format
                    if tambah['Jumlah'].isnumeric():
                        tambah['Jumlah'] = int(tambah['Jumlah'])
                        break

                    else:
                        print('\nINPUT JUMLAH HARUS NUMERIK')
                        continue

                # Satuan Baru
                tambah['Satuan'] = input('MASUKKAN SATUAN BARANG : ')

                # Ganti Jenis
                while True:
                    tambah['Jenis'] = input('MASUKKAN JENIS BARANG [Basah / Kering]: ').title()

                    # Karena Hanya ada 2 format Jenis, jadi dicek inputnya
                    if tambah['Jenis'].lower() == 'basah' or tambah['Jenis'].lower() == 'kering':
                        break
                    else:
                        print('\nINPUT JENIS HARUS BASAH / KERING')
                        continue
                
                # Checker
                while True:
                    print(f'''
    ==========Nama : {tambah['Nama']}==========
    Jumlah : {tambah['Jumlah']}
    Satuan : {tambah['Satuan']}
    Jenis : {tambah['Jenis']} 
    ''')
                    checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                    
                    # Input checker y
                    if checker.lower() == 'y':
                        counter = 1
                        # buat unique id berdasarkan jenis
                        if tambah['Jenis'].lower() == 'basah':
                            
                            # Generate ID barang basah dengan cara Check jumlah item basah
                            while True:
                                id_baru = str(counter) + 'B'
                                if id_baru in outer_keys:
                                    counter += 1
                                    continue
                                else:
                                    break

                            inventory[str(counter) + 'B'] = tambah
                        
                        elif tambah['Jenis'].lower() == 'kering':

                            # Generate ID barang kering dengan cara Check jumlah item kering
                            while True:
                                id_baru = str(counter) + 'K'
                                if id_baru in outer_keys:
                                    counter += 1
                                    continue
                                else:
                                    break
                            inventory[str(counter) + 'K'] = tambah
                        print('\nData Tersimpan')
                        break

                    # Input checker n
                    elif checker.lower() == 'n':
                        break

                    else:
                        print('INPUT TIDAK SESUAI -> Y/N')
                        continue

            # Kembali ke Menu Utama
            elif input_2 == 2:
                break
                
            # Salah Input Pilihan
            else:
                print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

# Checker untuk Update Nama dan Satuan
def checkUbah(ubahKode, input_baru, kolom):
    while True:
        # Checker
        print(f'''
        ==============================
        {kolom.upper()} LAMA : {inventory[ubahKode.upper()][kolom]}
        {kolom.upper()} BARU : {input_baru}
''')                    
        checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
        
        # Bener
        if checker.lower() == 'y':
            # Ubah ke Kolom Baru
            if kolom == 'Jumlah' :
                inventory[ubahKode.upper()][kolom] = input_baru
            else:
                inventory[ubahKode.upper()][kolom] = input_baru.title()
            
            print('\nData Tersimpan')
            break
        
        # Tidak Benar
        elif checker.lower() == 'n':
            break
        
        # Input tidak sesuai
        else:
            print('INPUT TIDAK SESUAI -> Y/N')
            continue

# Menu 3: Update
def ubahInventaris():
    while True:
        # Tampilan # 3
        print(f'''
    ==========MENGUBAH DATA INVENTARIS==========

    1. UBAH DATA
    2. KEMBALI KE MENU UTAMA
    ''')
        # Input Sub-Menu
        input_3 = input('SILAKAN PILIH [1-2] : ').strip()

        # Kalau input bukan numerik
        if input_3.isnumeric() == False:
            print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

        else: 
            input_3 = int(input_3)
            # Mengubah Data Barang
            if input_3 == 1:
                if len(inventory) == 0:
                    print('\nINVENTARIS KOSONG')
                    continue

                printInventory()
                outer_keys = list(inventory.keys())
                # Input kode barang yang ingin diubah
                ubahKode = input('\nMASUKKAN KODE BARANG : ').strip()

                # Kalau kode barang gak ada
                if ubahKode.upper() not in outer_keys:
                    print('\nBARANG TIDAK ADA')
                
                # Kalau kode barang ada
                else:
                    # Print data dari kode barang yang diminta
                    printData(ubahKode.upper())

                    # Checker
                    while True:
                        checker = input('\nAPAKAH BARANG SUDAH SESUAI (Y/N)? ').strip()
                
                        # Kalau Bener
                        if checker.lower() == 'y':

                            while True:
                                # Tampilan Sub-Menu pilihan yang mau diubah
                                print(f'''
    ==========UBAH DATA==========

    1. NAMA
    2. STOK
    3. SATUAN
    4. JENIS
    5. KEMBALI KE MENGUBAH DATA INVENTARIS
        ''')            
                                # Input Pilihan
                                input_ubah = input('SILAKAN PILIH [1-5] : ').strip()

                                # Check input format
                                if input_ubah.isnumeric() == False:
                                    print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
                                    
                                else: 
                                    input_ubah = int(input_ubah)
                                    # Ubah Nama
                                    if input_ubah == 1:
                                        input_baru = input('SILAKAN MASUKKAN NAMA BARU : ').strip()
                                        
                                        # Function Checker
                                        checkUbah(ubahKode, input_baru, 'Nama')

                                    # Ubah Stok
                                    elif input_ubah == 2:
                                        while True:
                                            input_baru = input('SILAKAN MASUKKAN STOK BARU : ').strip()
                                            # Checker Numerik
                                            if input_baru.isnumeric() == True:
                                                input_baru = int(input_baru)
                                                break
                                            else:
                                                print('\nSTOK HARUS NUMERIK')
                                                continue
                                        
                                        # Function Checker
                                        checkUbah(ubahKode, input_baru, 'Jumlah')

                                    # Ubah Satuan
                                    elif input_ubah == 3:
                                        input_baru = input('SILAKAN MASUKKAN SATUAN BARU : ').strip()

                                        # Function Checker
                                        checkUbah(ubahKode, input_baru, 'Satuan')                           
                                    
                                    # Ubah Jenis
                                    elif input_ubah == 4:

                                        # Checker Untuk Jenis Basah
                                        if 'B' in ubahKode.upper():

                                            while True:
                                                print(f'''
        JENIS LAMA : Basah
        JENIS BARU : Kering
                        ''')
                                                checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                            
                                                # y
                                                if checker.lower() == 'y':
                                                    # Ubah ke Jenis baru
                                                    inventory[ubahKode.upper()]['Jenis'] = 'Kering'
                                                    
                                                    # Ubah Key Baru
                                                    counter = 1
                                                    for i in outer_keys:
                                                        if 'K' in i:
                                                            counter += 1
                                                    counter = str(counter)
                                                    inventory[counter + 'K'] = inventory[ubahKode.upper()]
                                                    del inventory[ubahKode.upper()]

                                                    print('\nData Tersimpan')
                                                    break
                                                # n
                                                elif checker.lower() == 'n':
                                                    break
                                                # tidak sesuai
                                                else:
                                                    print('INPUT TIDAK SESUAI -> Y/N')
                                                    continue

                                        # Checker Untuk Jenis Kering
                                        elif 'K' in ubahKode.upper():

                                            while True:
                                                print(f'''
        JENIS LAMA : Kering
        JENIS BARU : Basah
                        ''')
                                                checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                            
                                                # y
                                                if checker.lower() == 'y':
                                                    # Ubah ke Jenis Baru
                                                    inventory[ubahKode.upper()]['Jenis'] = 'Basah'
                                                    
                                                    # Ubah Key Baru
                                                    counter = 1
                                                    for i in outer_keys:
                                                        if 'B' in i:
                                                            counter += 1
                                                    counter = str(counter)
                                                    inventory[counter + 'B'] = inventory[ubahKode.upper()]
                                                    del inventory[ubahKode.upper()]

                                                    print('\nData Tersimpan')
                                                    break
                                                # n
                                                elif checker.lower() == 'n':
                                                    break
                                                # tidak sesuai
                                                else:
                                                    print('INPUT TIDAK SESUAI -> Y/N')
                                                    continue
                                                    
                                    # Kembali ke Tampilan sub-menu ubah
                                    elif input_ubah == 5:
                                        break
                                    
                                    # Input tidak sesuai
                                    else:
                                        print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
                                        continue
                            break

                        # Input checker n, kembali ke sub-menu ubah
                        elif checker.lower() == 'n':
                            break
                        
                        # input checker bukan y/n
                        else:
                            print('INPUT TIDAK SESUAI -> Y/N')
                            continue
            
            # Kembali ke Menu Utama
            elif input_3 == 2:
                break
            
            # Input tidak sesuai
            else:
                print('\nPILIHAN YANG ANDA MASUKKAN SALAH')      

# Menu 4: Delete
def hapusInventaris():
    while True:
        print(f'''
    MENGHAPUS DATA INVENTARIS

    1. HAPUS DATA
    2. KEMBALI KE MENU UTAMA
        ''')
        # input
        input_4 = input('SILAKAN PILIH [1-2] : ').strip()
        
        if input_4.isnumeric() == False:
            print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

        else: 
            input_4 = int(input_4)
            if input_4 == 1:
                if len(inventory) == 0:
                    print('\nINVENTARIS KOSONG')
                    continue
                printInventory()
                # input kode barang yang ingin dihapus
                outer_keys = list(inventory.keys())
                input_hapus = input('\nMASUKKAN KODE BARANG : ').strip()

                # Kalau kode barang tidak ada
                if input_hapus.upper() not in outer_keys:
                    print('\nBARANG TIDAK ADA')

                # Kalau kode barang ada
                else:
                    while True:
                        # Checker
                        printData(input_hapus.upper())

                        checker = input('\nAPAKAH ANDA AKAN MENGHAPUS DATA DI ATAS (Y/N)? ').strip()
                        
                        # y
                        if checker.lower() == 'y':
                            del inventory[input_hapus.upper()]
                            print('\nDATA SUDAH DIHAPUS')
                            break
                        # n
                        elif checker.lower() == 'n':
                            break
                        # tidak sesuai
                        else:
                            print('INPUT TIDAK SESUAI -> Y/N')
                            continue

            elif input_4 == 2:
                break

            else:
                print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
                continue

#===================================================================================
while True:
    # HOME PAGE
    print(f'''
    ==========GUDANG DAPUR==========

    1. INVENTARIS
    2. MENAMBAHKAN DATA INVENTARIS
    3. MENGUBAH DATA INVENTARIS
    4. MENGHAPUS DATA INVENTARIS
    5. EXIT
    ''')
    input_home = input('SILAKAN PILIH [1-5] : ').strip()

    # Filter format input
    if input_home.isnumeric() == False:
        print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
        
    else: 
        input_home = int(input_home)
        # Menampilkan Data Inventaris
        if input_home == 1:
            # Tampilan # 1
            menampilkanInventaris()

        # Menambahkan Data Inventaris
        elif input_home == 2:
            # Tampilan # 2
            tambahInventaris()

        # Mengubah Data Inventaris
        elif input_home == 3:
            # Tampilan # 3
            ubahInventaris()

        # Menghapus data inventaris
        elif input_home == 4:
            hapusInventaris()

        # Exit Program
        elif input_home == 5:
            break

        # Salah Input
        else:
            print('\nPILIHAN YANG ANDA MASUKKAN SALAH')