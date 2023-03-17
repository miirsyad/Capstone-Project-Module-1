# Capstone Project Module 1 Purwadhika - Muhammad Irsyad


# DATA SET
inventory = {
    '1B' : {'Nama' : 'Ayam Fillet','Qty' : 100, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '2B' : {'Nama' : 'Telur', 'Qty' : 50, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '3B' : {'Nama' : 'Bombai', 'Qty' : 50, 'Satuan' : 'kg', 'Jenis' : 'Basah'},
    '4B' : {'Nama' : 'Tempe', 'Qty' : 150, 'Satuan' : 'pcs', 'Jenis' : 'Basah'},
    '5B' : {'Nama' : 'Pecay', 'Qty' : 100, 'Satuan' : 'kg', 'Jenis' : 'Basah'},

    '1K' : {'Nama' : 'Beras', 'Qty' : 500, 'Satuan' : 'kg', 'Jenis' : 'Kering'},
    '2K' : {'Nama' : 'Terigu', 'Qty' : 200, 'Satuan' : 'kg', 'Jenis' : 'Kering'},
    '3K' : {'Nama' : 'Saus Teriyaki', 'Qty' : 100, 'Satuan' : 'pcs', 'Jenis' : 'Kering'}
}

# Print Semua Inventaris
def printInventory():
    judulInventory = ['Kode Barang', 'Nama Barang', 'Stok', 'Satuan', 'Jenis Satuan']
    outer_keys = list(inventory.keys())

    # Print List Inventaris
    print('Daftar Inventaris\n')

    print(f'{judulInventory[0]:<20}|{judulInventory[1]:<20}|{judulInventory[2]:<20}|{judulInventory[3]:<20}|{judulInventory[4]:<20}')
    for i in range(len(inventory)):
    
        print(f'''{outer_keys[i]:<20}|{inventory[outer_keys[i]]['Nama']:<20}|{inventory[outer_keys[i]]['Qty']:<20}|{inventory[outer_keys[i]]['Satuan']:<20}|{inventory[outer_keys[i]]['Jenis']:<20}''')

# Print Satu Item di Inventaris
def printBaris(input_kode):
    judulInventory = ['Kode Barang', 'Nama Barang', 'Stok', 'Satuan', 'Jenis Satuan']
    print(f'{judulInventory[0]:<20}|{judulInventory[1]:<20}|{judulInventory[2]:<20}|{judulInventory[3]:<20}|{judulInventory[4]:<20}')
    print(f'''{input_kode.upper():<20}|{inventory[input_kode.upper()]['Nama']:<20}|{inventory[input_kode.upper()]['Qty']:<20}|{inventory[input_kode.upper()]['Satuan']:<20}|{inventory[input_kode.upper()]['Jenis']:<20}''')

# Menu 1: Read
def menampilkanInventaris():
    while True:
                # Tampilan # 1
                print(f'''
    INVENTARIS

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

                        # Read
                        else:
                            printInventory()

                    # Print Salah Satu Data
                    elif input_1 == 2:
                        # Kalau inventaris kosong, kasih tau dan gak usah print
                        if len(inventory) == 0:
                            print('\nINVENTARIS KOSONG')
                        
                        else:
                            # Minta input kolom unik
                            input_kode = input('MASUKKAN KODE BARANG : ').strip()
                            
                            # key dari Data Set = Kode Barang
                            outer_keys = list(inventory.keys())

                            # Kalau Kode Barang Gak ada, kasih tau
                            if input_kode.upper() not in outer_keys:
                                print('\nKODE BARANG TIDAK ADA DI INVENTARIS')

                            # Kalau ada, print
                            else:
                                print()
                                printBaris(input_kode.upper())

                    # Kembali Ke Menu
                    elif input_1 == 3:
                        break
                    
                    # Kalau salah pilihan menu
                    else:
                        print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

# Menu 2: Create
def tambahInventaris():

    while True:
            # Tampilan # 2
            print(f'''
    MENAMBAHKAN DATA INVENTARIS

    1. TAMBAH DATA
    2. KEMBALI KE MENU UTAMA
    ''')    
            # Input Sub=Menu
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
                    tambahNama = input('MASUKKAN NAMA BARANG : ')
                    while True:
                        # Jumlah Barang Baru
                        tambahQty = input('MASUKKAN JUMLAH BARANG (ANGKA): ')

                        # Cek Format
                        if tambahQty.isnumeric():
                            tambahQty = int(tambahQty)
                            break
                        else:
                            print('\nINPUT JUMLAH HARUS NUMERIK\n')
                            continue

                    # Satuan Baru
                    tambahSatuan = input('MASUKKAN SATUAN BARANG : ')
                    while True:
                        # Ganti Jenis
                        tambahJenis = input('MASUKKAN JENIS BARANG [Basah / Kering]: ')

                        # Karena Hanya ada 2 Jenis format, jadi dicek inputnya
                        if tambahJenis.lower() == 'basah' or tambahJenis.lower() == 'kering':
                            break
                        else:
                            print('\nINPUT JENIS HARUS BASAH / KERING\n')
                            continue

                    print(f'''
    Nama : {tambahNama}
    Qty : {tambahQty}
    Satuan : {tambahSatuan}
    Jenis : {tambahJenis}
    ''')
                        
                    # Checker
                    checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                    
                    # Kalau Bener
                    if checker.lower() == 'y':
                        # buat unique id berdasarkan jenis
                        if tambahJenis.lower() == 'basah':
                            counter = 1
                            
                            while True:
                                id_baru = str(counter) + 'B'
                                if id_baru in outer_keys:
                                    counter += 1
                                    continue
                                else:
                                    break
 
                            inventory[str(counter) + 'B'] = {'Nama' : tambahNama.title(),'Qty' : tambahQty, 'Satuan' : tambahSatuan.title(), 'Jenis' : tambahJenis.title()}
                            
                        
                        elif tambahJenis.lower() == 'kering':
                            counter = 1

                            while True:
                                id_baru = str(counter) + 'K'
                                if id_baru in outer_keys:
                                    counter += 1
                                    continue
                                else:
                                    break
                            inventory[str(counter) + 'K'] = {'Nama' : tambahNama.title(),'Qty' : tambahQty, 'Satuan' : tambahSatuan.title(), 'Jenis' : tambahJenis.title()}
                            
                        print('\nData Tersimpan')
                        continue
                        # Input checker bukan y
                    else:
                        continue
                    

                # Kembali ke Menu Utama
                elif input_2 == 2:
                    break
                    
                # Salah Input Pilihan
                else:
                    print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

# Menu 3: Update
def ubahInventaris():
    while True:
                # Tampilan # 3
                print(f'''
    MENGUBAH DATA INVENTARIS

    1. UBAH DATA
    2. KEMBALI KE MENU UTAMA
            ''')
                # Input Sub-Menu
                input_3 = input('SILAKAN PILIH [1-2] : ').strip()
                if input_3.isnumeric() == False:
                    print('\nPILIHAN YANG ANDA MASUKKAN SALAH')

                else: 
                    input_3 = int(input_3)
                    # Mengubah Data Barang
                    if input_3 == 1:
                        outer_keys = list(inventory.keys())
                        # Input kode barang yang ingin diubah
                        ubahKode = input('MASUKKAN KODE BARANG : ').strip()

                        # Kalau kode barang gak ada
                        if ubahKode.upper() not in outer_keys:
                            print('\nBARANG TIDAK ADA')
                        
                        # Kalau kode barang ada
                        else:
                            print()

                            # Print data dari kode barang yang diminta
                            printBaris(ubahKode.upper())

                            # Checker
                            checker = input('\nAPAKAH BARANG SUDAH SESUAI (Y/N)? ').strip()
                    
                            # Kalau Bener
                            if checker.lower() == 'y':
                                pass
                                # Input checker bukan y
                            else:
                                continue

                            
                            while True:
                                # Tampilan Sub-Menu pilihan yang mau diubah
                                print(f'''
    UBAH DATA

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

                                        # Checker
                                        print(f'''
            NAMA LAMA : {inventory[ubahKode.upper()]['Nama']}
            NAMA BARU : {input_baru}
                ''')                    
                                        checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                    
                                        # Kalau Bener
                                        if checker.lower() == 'y':
                                            # Langsung Input Key Baru
                                            inventory[ubahKode.upper()]['Nama'] = input_baru.title()
                                            
                                            print('\nData Tersimpan')

                                    # Ubah Stok
                                    elif input_ubah == 2:
                                        input_baru = input('SILAKAN MASUKKAN STOK BARU : ').strip()

                                        # Checker Numerik

                                        if input_baru.isnumeric() == True:
                                            input_baru = int(input_baru)
                                        else:
                                            print('\nSTOK HARUS NUMERIK')
                                            continue
                                        
                                        # Checker
                                        print(f'''
            STOK LAMA : {inventory[ubahKode.upper()]['Qty']}
            STOK BARU : {input_baru}
                ''')
                                        checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                    
                                        # Kalau Bener
                                        if checker.lower() == 'y':
                                            # Langsung Input Key Baru
                                            inventory[ubahKode.upper()]['Qty'] = input_baru
                                            
                                            print('\nData Tersimpan')

                                    # Ubah Satuan
                                    elif input_ubah == 3:
                                        input_baru = input('SILAKAN MASUKKAN SATUAN BARU : ').strip()

                                        # Checker
                                        print(f'''
            SATUAN LAMA : {inventory[ubahKode.upper()]['Satuan']}
            SATUAN BARU : {input_baru}
                ''')
                                        checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                    
                                        # Kalau Bener
                                        if checker.lower() == 'y':
                                            # Langsung Input Key Baru
                                            inventory[ubahKode.upper()]['Satuan'] = input_baru
                                            
                                            print('\nData Tersimpan')
                                    
                                    # Ubah Jenis
                                    elif input_ubah == 4:

                                        # Checker Untuk Jenis Basah
                                        if 'B' in ubahKode.upper():

                                                print(f'''
            JENIS LAMA : Basah
            JENIS BARU : Kering
                        ''')
                                                checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                            
                                                # Kalau Bener
                                                if checker.lower() == 'y':
                                                    # Langsung Input Key Baru
                                                    inventory[ubahKode.upper()]['Jenis'] = 'Kering'
                                                    counter = 1
                                                    for i in outer_keys:
                                                        if 'K' in i:
                                                            counter += 1
                                                    counter = str(counter)
                                                    inventory[counter + 'K'] = inventory[ubahKode.upper()]
                                                    del inventory[ubahKode.upper()]

                                                    print('\nData Tersimpan')

                                        # Checker Untuk Jenis Kering
                                        elif 'K' in ubahKode.upper():

                                                print(f'''
            JENIS LAMA : Kering
            JENIS BARU : Basah
                        ''')
                                                checker = input('APAKAH SUDAH SESUAI (Y/N)? ').strip()
                            
                                                # Kalau Bener
                                                if checker.lower() == 'y':
                                                    # Langsung Input Key Baru
                                                    inventory[ubahKode.upper()]['Jenis'] = 'Basah'
                                                    counter = 1
                                                    for i in outer_keys:
                                                        if 'B' in i:
                                                            counter += 1
                                                    counter = str(counter)
                                                    inventory[counter + 'B'] = inventory[ubahKode.upper()]
                                                    del inventory[ubahKode.upper()]

                                                    print('\nData Tersimpan')

                                        else:
                                            print('\nJENIS TIDAK SESUAI')
                                            continue
                                    # Kembali ke Tampilan # 3
                                    elif input_ubah == 5:
                                        break

                                    else:
                                        print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
                                        continue
                    
                    # Kembali ke Menu Utama
                    elif input_3 == 2:
                        break

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
                        # input kode barang yang ingin dihapus
                        outer_keys = list(inventory.keys())
                        input_hapus = input('MASUKKAN KODE BARANG : ').strip()

                        # Kalau kode barang tidak ada
                        if input_hapus.upper() not in outer_keys:
                            print('\nBARANG TIDAK ADA')

                        # Kalau kode barang ada
                        else:
                            # Checker
                            print(f'''
        Nama : {inventory[input_hapus.upper()]['Nama']}
        Qty : {inventory[input_hapus.upper()]['Qty']}
        Satuan : {inventory[input_hapus.upper()]['Satuan']}
        Jenis : {inventory[input_hapus.upper()]['Jenis']}
        ''')
                            checker = input(f'APAKAH ANDA AKAN MENGHAPUS DATA DI ATAS (Y/N)? ').strip()
                            
                            # Kalau Bener
                            if checker.lower() == 'y':
                                del inventory[input_hapus.upper()]
                                print('\nDATA SUDAH DIHAPUS')

                    elif input_4 == 2:
                        break

                    else:
                        print('\nPILIHAN YANG ANDA MASUKKAN SALAH')
                        continue


#===================================================================================

while True:
    # HOME PAGE
    print(f'''
    GUDANG DAPUR

    1. INVENTARIS
    2. MENAMBAHKAN DATA INVENTARIS
    3. MENGUBAH DATA INVENTARIS
    4. MENGHAPUS DATA INVENTARIS
    5. EXIT
    ''')
    input_home = input('SILAKAN PILIH [1-5] : ').strip()

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