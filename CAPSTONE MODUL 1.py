# DATA PASIEN RUMAH SAKIT
    
pasien = [['1111','Jason','Kemang','THT','BPJS']]
customers = ['1']
id = len(pasien)+1

while True:
    pilihanMenu = input('''
        WELCOME TO JUARA SURGA HOSPITAL
        
        Main Menu:
        1. Check Profile Data
        2. Registration
        3. Change Profile Data
        4. Delete Profile 
        5. Keluar
        \n
        Choose Menu Number: ''')

    if(pilihanMenu == '1'):
        while True:
            print('\nCheck Profile Menu\n')
            print('--------------------------------------')
            loginID = input('\nMasukan ID: ')
            if(loginID == '0'):
                print('\nDaftar Pasien')
                print('--------------------------------------')
                for i in range(len(pasien)):
                    print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
                    print('--------------------------------------')
                continue
            if loginID in customers:
                for i in range(len(pasien)):
                    print('\nProfile {}'.format(pasien[i][1]))
                    print('--------------------------------------')
                    print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
                    print('--------------------------------------')
                continue
            else:
                break
            
        

            

    if(pilihanMenu == '2'):
        regis = input('\nIngin melakukan registrasi? \n1. Ya \n2. Tidak \nPilihan: ')
        if(regis == '2'):
            continue
        elif(regis == '1'):
            while True:
                print('Silahkan isi pertanyaan dibawah ini\n')
                nik = int(input('Masukan 4 Digit Angka Terakhir NIK (contoh:0011): '))
                nama = input('Masukan Nama Pasien: ')
                alamat = input('Masukan Alamat Pasien: ')
                pelayanan = input('Masukan Pelayanan yang dibutuhkan (contoh: Ortopedi/THT): ')
                asuransi = input('Asuransi yang akan digunakan (contoh: BPJS/SINARMAS/Tidak Ada): ')
                capitalNama = nama.capitalize()
                capitalAlamat = alamat.capitalize()
                upperPelayanan = pelayanan.upper()
                upperAsuransi = asuransi.upper()
                print('\nData Profil Pasien\n')
                print('--------------------------------------')
                print('NIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(nik,capitalNama,capitalAlamat,upperPelayanan,upperAsuransi))
                print('--------------------------------------')
                check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                if(check == '1'):
                    if nik in pasien:
                        print("Pasien sudah terdaftar")
                    else:
                        pasien.append([nik,capitalNama,capitalAlamat,upperPelayanan,upperAsuransi])
                        customers.append([id])
                        print('\nData profil pasien telah di daftarkan\n')
                        print('ID anda : {}'.format(id))
                        break
                elif(check == '2'):
                    continue

    if(pilihanMenu == '3'):
        print('\nDaftar Pasien')
        print('--------------------------------------')
        for i in range(len(pasien)):
            print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
            print('--------------------------------------')
        while True:
            pilihPasien = input('Pilih nomor pasien yang ingin dirubah: ')
            i = len(pilihPasien)+1
            for i in range(len(pasien)):
                pilihData = input('Data yang ingin dirubah: \n1. NIK \n2. Nama \n3. Alamat \n4. Pelayanan \n5. Asuransi \nNomor yang dipilih: ')
                if(pilihData == '1'):
                    nik = input('Masukan 4 Digit Angka Terakhir NIK (contoh:0011): ')
                    pasien[0][0] = nik
                    print('\nData Profil Pasien\n')
                    print('--------------------------------------')
                    for i in range(len(pasien)):
                        print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
                        print('--------------------------------------')
                    check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                    if(check == '1'):
                        print('\nData profil pasien telah terubah\n')
                        break
                elif(pilihData == '2'):
                    nama = input('Masukan Nama Pasien: ')
                    pasien[j][0] = nama
                    print('\nData Profil Pasien\n')
                    print('--------------------------------------')
                    for j in range(len(pasien)):
                        print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(j+1,pasien[j][0],pasien[j][1],pasien[j][2],pasien[j][3],pasien[j][4]))
                        print('--------------------------------------')
                    check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                    if(check == '1'):
                        print('\nData profil pasien telah terubah\n')
                        break
                elif(pilihData == '3'):
                    alamat = input('Masukan Alamat Pasien: ')
                    pasien[j][0] = alamat
                    print('\nData Profil Pasien\n')
                    print('--------------------------------------')
                    for j in range(len(pasien)):
                        print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(j+1,pasien[j][0],pasien[j][1],pasien[j][2],pasien[j][3],pasien[j][4]))
                        print('--------------------------------------')
                    check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                    if(check == '1'):
                        print('\nData profil pasien telah terubah\n')
                        break
                elif(pilihData == '4'):
                    pelayanan = input('Masukan Pelayanan yang dibutuhkan (contoh: Ortopedi/THT): ')
                    pasien[j][0] = pelayanan
                    print('\nData Profil Pasien\n')
                    print('--------------------------------------')
                    for j in range(len(pasien)):
                        print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(j+1,pasien[j][0],pasien[j][1],pasien[j][2],pasien[j][3],pasien[j][4]))
                        print('--------------------------------------')
                    check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                    if(check == '1'):
                        print('\nData profil pasien telah terubah\n')
                        break
                elif(pilihData == '5'):
                    asuransi = input('Asuransi yang akan digunakan (contoh: BPJS/SINARMAS/Tidak Ada): ')
                    pasien[j][0] = asuransi
                    print('\nData Profil Pasien\n')
                    print('--------------------------------------')
                    for j in range(len(pasien)):
                        print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(j+1,pasien[j][0],pasien[j][1],pasien[j][2],pasien[j][3],pasien[j][4]))
                        print('--------------------------------------')
                    check = input('Apakah data pasien sudah sesuai? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
                    if(check == '1'):
                        print('\nData profil pasien telah terubah\n')
                        break
            
                print('\nTidak ada nomor pasien yang anda pilih\n')
                break

    if(pilihanMenu == '4'):
        while True:
            print('\nDaftar Pasien')
            print('--------------------------------------')
            for i in range(len(pasien)):
                print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
                print('--------------------------------------')
            pilihPasien = int(input('Pilih nomor pasien yang ingin dihapus: '))
            hapus = pilihPasien-1
            del pasien[hapus]
            print('\nDaftar Pasien')
            print('--------------------------------------')
            for i in range(len(pasien)):
                print('Pasien {} \nNIK\t\t: {} \nNama\t\t: {} \nAlamat\t\t: {} \nPelayanan\t: {} \nAsuransi\t: {} '.format(i+1,pasien[i][0],pasien[i][1],pasien[i][2],pasien[i][3],pasien[i][4]))
                print('--------------------------------------')
            check = input('Apakah masih ada profile pasien yang ingin dihapus? \n1. Ya \n2. Tidak \nPilih Nomor: ') 
            if(check == '2'):
                break
                

        