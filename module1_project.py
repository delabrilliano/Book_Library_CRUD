listbuku =[
    {'isbn' : '0101',
    'namabuku' : 'it',
    'genre' : 'horror',
    'author' : 'stephen king',
    'jml' : 3,
    'peminjam' : ['anton', 'gunawan', 'bambang'],
    'sisabuku' : 0,
    'synopsis' : 'The story follows the experiences of seven children as they are terrorized by an evil entity that exploits the fears of its victims to disguise itself while hunting its prey.'
    },
   {'isbn' : '0102',
    'namabuku' : 'dracula',
    'genre' : 'horror',
    'author' : 'bram stoker',
    'jml' : 6,
    'peminjam' : ['anton', 'budi'],
    'sisabuku' : 4,
    'synopsis' : 'Dracula, Gothic novel by Bram Stoker, published in 1897, that was the most popular literary work derived from vampire legends and became the basis for an entire genre of literature and film'
    },
    {'isbn' : '0201',
    'namabuku' : 'the russian assassin',
    'genre' : 'action',
    'author' : 'jack arbor',
    'jml' : 1,
    'peminjam' : [],
    'sisabuku' : 1,
    'synopsis' : '''Former KGB assassin Max Austin's peaceful life in Paris is shattered when his mother's imminent death brings him back to a world he only wants to forget.'''
    },
    {'isbn' : '0202',
    'namabuku' : 'agent zero',
    'genre' : 'action',
    'author' : 'jack mars',
    'jml' : 2,
    'peminjam' : ['gunawan'],
    'sisabuku' : 1,
    'synopsis' : '''In this much-anticipated new spy thriller series by Jack Mars, listeners are taken on an action thriller across Europe as presumed-CIA operative Kent Steele, hunted by terrorists, by the CIA, and by his own identity, must solve the mystery of who is after him, of the terrorists pending target - and of the beautiful woman he keeps seeing in his mind.'''
    },
]

def read ():
    while True:
        user_read = input(''' 
Masukkan tampilan yang diinginkan:
1. Tampilkan Seluruh Daftar Buku
2. Jelajahi berdasarkan ISBN
3. Berdasarkan Genre
4. Melihat Data Peminjam Buku
5. Kembali ke Menu Awal
Tampilan yang diinginkan (1-5):  ''')
        if user_read == '1':
                print ('\nBerikut Daftar Buku yang Tersedia di Perpustakaan Kami:')
                print ('ISBN \t| Judul Buku (Buku Tersedia)')
                for i in range(len(listbuku)):
                    print ('{}\t| {} by {} ({})'.format(listbuku[i]['isbn'], listbuku[i]['namabuku'].title(), listbuku[i]['author'].title() ,listbuku[i]['sisabuku']))
                break
        if user_read == '2':
            while True:
                print ('\nISBN \t| Judul Buku (Buku Tersedia)')
                for i in range(len(listbuku)):
                    print ('{}\t| {} by {} ({})'.format(listbuku[i]['isbn'], listbuku[i]['namabuku'].title(), listbuku[i]['author'].title() ,listbuku[i]['sisabuku']))
                user_read2 = input('Masukkan ISBN dari Buku yang anda ingin ketahui: ')
                isbntrue = 0
                for i in range (len(listbuku)):
                    if listbuku[i]['isbn'] == user_read2:
                        isbntrue += 1
                        print ('\nJudul Buku: {} by {} \nGenre: {} \nSynopsis: {}'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['genre'].capitalize(), listbuku[i]['synopsis'].title()))
                    else:
                        continue
                if isbntrue < 1:
                    print('\nBuku dengan ISBN {} tidak ada dalam koleksi kami.'.format(user_read2))
                    break
                break
        if user_read == '3':
            while True:
                user_read3 = input(''' 
Genre yang diinginkan:
1. Horror
2. Action
3. Comedy
4. Non-Fiksi
5. Others
6. Kembali ke Menu Jelajah Buku
Masukkan Genre yang diinginkan (1-6): ''')
                listpilihan = 0
                if user_read3 == '1':
                    print ('\nDaftar Buku Horror: ')
                    print ('Judul Buku (Buku Tersedia)')
                    for i in range (len(listbuku)):
                        if listbuku[i]['genre'] == 'horror' :
                            listpilihan += 1
                            print('{} by {} ({})'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['sisabuku']))
                        else:
                            continue
                    if listpilihan < 1:
                            print ('\nMohon maaf, saat ini perpustakaan tidak memiliki buku dengan genre yang anda pilih.')
                elif user_read3 == '2':
                    for i in range (len(listbuku)):
                        if listbuku[i]['genre'] == 'action' :
                            listpilihan += 1
                            print('{} by {} ({})'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['sisabuku']))
                        else:
                            continue
                    if listpilihan < 1:
                            print ('\nMohon maaf, saat ini perpustakaan tidak memiliki buku dengan genre yang anda pilih.')
                elif user_read3 == '3':
                    for i in range (len(listbuku)):
                        if listbuku[i]['genre'] == 'comedy' :
                            listpilihan += 1
                            print('{} by {} ({})'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['sisabuku']))
                        else:
                            continue
                    if listpilihan < 1:
                            print ('\nMohon maaf, saat ini perpustakaan tidak memiliki buku dengan genre yang anda pilih.')
                elif user_read3 == '4':
                    for i in range (len(listbuku)):
                        if listbuku[i]['genre'] == 'non-fiksi' :
                            listpilihan += 1
                            print('{} by {} ({})'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['sisabuku']))
                        else:
                            continue
                    if listpilihan < 1:
                            print ('\nMohon maaf, saat ini perpustakaan tidak memiliki buku dengan genre yang anda pilih.')
                elif user_read3 == '5':
                    for i in range (len(listbuku)):
                        if listbuku[i]['genre'] == 'others' :
                            listpilihan += 1
                            print('{} by {} ({})'.format(listbuku[i]['namabuku'].title(), listbuku[i]['author'].title(), listbuku[i]['sisabuku']))
                        else:
                            continue
                    if listpilihan < 1:
                            print ('\nMohon maaf, saat ini perpustakaan tidak memiliki buku dengan genre yang anda pilih.')
                elif user_read2 == '6':
                    break
                break   
        if user_read == '4':
                    print ('\nDaftar Buku: ')
                    print ('ISBN \t| Judul Buku')
                    for i in range(len(listbuku)):
                        print ('{}\t| {}'.format(listbuku[i]['isbn'], listbuku[i]['namabuku'].title()))
                    while True:
                        userinput4 = input('Masukkan ISBN untuk buku yang anda ingin ketahui: ')
                        isbntrue = 0
                        for i in range(len(listbuku)):
                            if listbuku[i]['isbn'] == userinput4:
                                isbntrue += 1
                                if len(listbuku[i]['peminjam']) > 0:
                                    print('\nJudul Buku: {} \nPeminjam:'.format(listbuku[i]['namabuku'].title()))
                                    for j in range (len(listbuku[i]['peminjam'])):
                                        print('{}. {}'.format(j+1, listbuku[i]['peminjam'][j].capitalize()))
                                    break
                                else:
                                    print('\nSaat ini buku yang dipilih tidak ada yang meminjam')
                                    break
                            else:
                                continue
                        if isbntrue < 1:
                            print('\nBuku dengan ISBN {} tidak ada dalam koleksi kami.'.format(userinput4))
                        break
        if user_read == '5':
            break

def create ():
    while True:
        user_create = input('''
Masukkan Menu yang diinginkan:
1. Menambahkan Buku Baru
2. Kembali ke Menu Awal
Menu yang diinginkan (1-2): ''')
        if user_create == '1':
            duplicateISBN = 0
            new_book_isbn = input('Masukkan ISBN dari Buku yang Baru: ')
            for i in range (len(listbuku)):
                if listbuku[i]['isbn'] == new_book_isbn:
                    print ('\nBuku Sudah Ada Dalam Koleksi Perpustakaan')
                    duplicateISBN += 1
                    break
                else:
                    continue
            if duplicateISBN == 0:
                new_book_title = input('Masukkan Judul Buku yang Baru: ').lower()
                while True:
                    genre_option = input('''
Pilihlah Genre dari Buku yang Baru:
1. Horror
2. Action
3. Comedy
4. Non-Fiksi
5. Others

Genre Buku (1-5): ''')
                    if genre_option == '1':
                        new_book_genre = 'horror'
                        break
                    elif genre_option == '2':
                        new_book_genre = 'action'
                        break
                    elif genre_option == '3':
                        new_book_genre = 'comedy'
                        break
                    elif genre_option == '4':
                        new_book_genre = 'non-fiksi'
                        break
                    elif genre_option == '5':
                        new_book_genre = 'others'
                        break
                    else:
                        print('\nPilihan Genre Salah Mohon input kembali Nomor Genre yang Sesuai!!!')
                new_book_author = input('Masukkan Pengarang dari Buku yang Baru: ').lower()
                new_book_jml = int(input('Masukkan Jumlah dari Buku Baru: '))
                new_book_synp = input('Masukkan Sinopsis dari Buku Baru: ')
                while True:
                    print('''
Berikut Data Buku Baru yang Akan Disimpan:
ISBN    : {}
Judul   : {}
Genre   : {}
Author  : {}
Jumlah  : {}
Synopsis: {}  '''.format(new_book_isbn, new_book_title.title(), new_book_genre.title(), new_book_author.title(), new_book_jml, new_book_synp.title()))
                    save_option = input('''
Apakah Data Ingin Disimpan? (Y/N): ''').upper()
                    if save_option == 'Y':
                        listbuku.append({'isbn' : new_book_isbn, 'namabuku' : new_book_title, 'genre' : new_book_genre, 'author' : new_book_author, 'jml' : new_book_jml, 'peminjam' : [], 'sisabuku' : new_book_jml, 'synopsis' : new_book_synp})
                        print('\nData Buku Baru Berhasil Disimpan')
                        break
                    elif save_option == 'N':
                        print('\nData Buku Baru Tidak Jadi Disimpan')
                        break
                    else:
                        print('\nInput Salah!!! Mohon Masukkan Input yang Benar (Y/N): ')


        

        elif user_create == '2':
            break    

def update():
    while True:
        user_update = input('''
Masukkan Menu yang diinginkan:
1. Memperbaharui Data Buku Perpustakaan
2. Kembali ke Menu Awal
Menu yang diinginkan (1-2): ''')
        if user_update == '1':
            while True:
                print ('\nBerikut Daftar Buku yang Dimiliki Perpustakaan: ')
                print ('\nISBN \t| Judul Buku (Buku Tersedia)')
                for i in range(len(listbuku)):
                    print ('{}\t| {} by {} ({})'.format(listbuku[i]['isbn'], listbuku[i]['namabuku'].title(), listbuku[i]['author'].title() ,listbuku[i]['sisabuku']))
                ISBNtrue = 0
                index_update = 0
                update_book_isbn = input('Masukkan ISBN dari Buku yang ingin Diperbaharui: ')
                for i in range (len(listbuku)):
                    if listbuku[i]['isbn'] == update_book_isbn:
                        ISBNtrue += 1
                        index_update += i
                        break
                    else:
                        continue
                if ISBNtrue == 0:
                    print('\nBuku Dengan ISBN {} Tidak Ada Dalam Koleksi Perpustakaan Kami'.format(update_book_isbn))
                    break
                elif ISBNtrue > 0:
                    while True:
                        print ('\nBerikut Data Buku dari ISBN yang anda Input:\nJudul Buku: {} by {} \nGenre: {} \nSynopsis: {}'.format(listbuku[index_update]['namabuku'].title(), listbuku[index_update]['author'].title(), listbuku[index_update]['genre'].capitalize(), listbuku[index_update]['synopsis'].title()))
                        user_isbntrue = input('\nApakah Benar Anda Ingin Memperbaharui Data Buku Tersebut? (Y/N): ').upper()
                        while True:
                            if user_isbntrue == 'N':
                                print('Data Buku Tidak Jadi Diperbaharui')
                                break
                            elif user_isbntrue == 'Y':
                                while True:
                                    user_isbntrue_y = input('''
1. Memperbaharui Judul Buku
2. Memperbaharui Genre Buku
3. Memperbaharui Penulis Buku
4. Memperbaharui Jumlah Buku
5. Memperbaharui Sinopsis Buku
6. Memperbaharui Peminjam Buku
7. Selesai Pembaharuan

Silahkan Masukkan Menu Pembaharuan Buku yang Ingin Dijalankan (1-5):
    ''')
                                    if user_isbntrue_y == '1':
                                        update_book_title = input('Silahkan Masukkan Judul Buku yang baru: ').lower()
                                        listbuku[index_update]['namabuku'] = update_book_title
                                        print('Judul Buku telah diperbaharui')
                                        continue
                                    if user_isbntrue_y == '2':
                                        update_book_genre = ''
                                        while True:
                                            update_book_option = input('''
1. Horror
2. Action
3. Comedy
4. Non-Fiksi
5. Others

Genre Buku (1-5): ''')
                                            if update_book_option == '1':
                                                update_book_genre = 'horror'
                                                print('Genre Buku telah diperbaharui')
                                                break
                                            elif update_book_option == '2':
                                                update_book_genre = 'action'
                                                print('Genre Buku telah diperbaharui')
                                                break
                                            elif update_book_option == '3':
                                                update_book_genre = 'comedy'
                                                print('Genre Buku telah diperbaharui')
                                                break
                                            elif update_book_option == '4':
                                                update_book_genre = 'non-fiksi'
                                                print('Genre Buku telah diperbaharui')
                                                break
                                            elif update_book_option == '5':
                                                update_book_genre = 'others'
                                                print('Genre Buku telah diperbaharui')
                                                break
                                            else:
                                                print('\nPilihan Genre Salah Mohon input kembali Nomor Genre yang Sesuai!!!')    
                                        listbuku[index_update]['genre'] = update_book_genre
                                        continue
                                    if user_isbntrue_y == '3':
                                        update_book_author = input('Silahkan Masukkan Penulis Buku yang baru: ').lower()
                                        listbuku[index_update]['author'] = update_book_author
                                        print('Penulis Buku telah diperbaharui')
                                        continue
                                    if user_isbntrue_y == '4':
                                        update_book_jml = int(input('Silahkan Masukkan Jumlah Buku yang baru: '))
                                        if update_book_jml - len(listbuku[index_update]['peminjam']) < 0:
                                            print('Jumlah Buku yang dimasukkan tidak sesuai. Harap periksa jumlah peminjam buku.')
                                            break
                                        elif update_book_jml - len(listbuku[index_update]['peminjam']) >= 0:
                                            listbuku[index_update]['jml'] = update_book_jml
                                            listbuku[index_update]['sisabuku'] = listbuku[index_update]['jml'] - len(listbuku[index_update]['peminjam'])
                                            print('Jumlah Buku telah diperbaharui')
                                            continue
                                    if user_isbntrue_y == '5':
                                        update_book_synp = input('Silahkan Masukkan Sinopsis Buku yang Baru: ').lower()
                                        listbuku[index_update]['synopsis'] = update_book_synp
                                        continue
                                    if user_isbntrue_y == '6':
                                        while True:
                                            update_book_option = input('''
1. Pengembalian Buku
2. Peminjaman Buku
3. Kembali ke Menu Utama

Menu Pembaharuan Peminjam yang Diinginkan (1-3): ''')
                                            if update_book_option == '1' :
                                                if len(listbuku[index_update]['peminjam']) > 0:
                                                    print ('No.Nama Peminjam')
                                                    for j in range (len(listbuku[index_update]['peminjam'])):
                                                        print('{}. {}'.format(j+1, listbuku[index_update]['peminjam'][j].capitalize()))
                                                    while True:
                                                        hapus_peminjam = int(input('Silahkan Masukkan Nomor Peminjam yang Mengembalikan Buku: '))
                                                        if hapus_peminjam <= len(listbuku[index_update]['peminjam']):
                                                            del listbuku[index_update]['peminjam'][hapus_peminjam-1]
                                                            listbuku[index_update]['sisabuku'] = listbuku[index_update]['jml'] - len(listbuku[index_update]['peminjam'])
                                                            print('Pengembalian Buku Berhasil Diinput')
                                                            break
                                                        else:
                                                            print('Nomor Peminjam Tidak Sesuai. Harap Cek Kembali.')
                                                else:
                                                    print('\nSaat ini buku yang dipilih tidak ada yang meminjam')
                                                    break
                                            elif update_book_option =='2':
                                                if listbuku[index_update]['sisabuku'] > 0:
                                                    tambah_peminjam = input('Silahkan Masukkan Nama Peminjam yang Meminjam Buku {}: '.format(listbuku[index_update]['namabuku']))
                                                    listbuku[index_update]['peminjam'].append(tambah_peminjam)
                                                    listbuku[index_update]['sisabuku'] = listbuku[index_update]['jml'] - len(listbuku[index_update]['peminjam']) 
                                                    print('Peminjaman Buku Berhasil Diinput')
                                                    break
                                                else:
                                                    print('Buku Sudah Tidak Tersedia untuk Dipinjam')
                                                    break
                                            elif update_book_option =='3':
                                                break
                                    if user_isbntrue_y == '7':
                                        print('\nData Selesai Diperbaharui!!!\nBerikut Data Buku Setelah Diperbaharui:')
                                        print ('\nJudul Buku: {}\nGenre: {}\nAuthor: {}\nJumlah Buku: {} \nJumlah Peminjam Buku: {}\nSisa Buku: {} \nSynopsis: {}'.format(listbuku[index_update]['namabuku'].title(), listbuku[index_update]['genre'].title(), listbuku[index_update]['author'].title(), listbuku[index_update]['jml'], len(listbuku[index_update]['peminjam']), listbuku[index_update]['sisabuku'] ,listbuku[index_update]['synopsis'].title()))
                                        break
                            else:
                                print('\nInput Salah!!! Mohon Masukkan Input yang Benar (Y/N): ')
                            break
                        break
                    break
        elif user_update == '2':
                break            

def delete():
    while True:
        user_delete = input('''
Masukkan Menu yang diinginkan:
1. Menghapus Data Buku Perpustakaan
2. Kembali ke Menu Awal
Menu yang diinginkan (1-2): ''')
        if user_delete == '1':
            while True:
                print ('\nBerikut Daftar Buku yang Dimiliki Perpustakaan: ')
                print ('\nISBN \t| Judul Buku (Buku Tersedia)')
                for i in range(len(listbuku)):
                    print ('{}\t| {} by {} ({})'.format(listbuku[i]['isbn'], listbuku[i]['namabuku'].title(), listbuku[i]['author'].title() ,listbuku[i]['sisabuku']))
                ISBNtrue = 0
                index_delete = 0
                delete_book_isbn = input('Masukkan ISBN dari Buku yang datanya ingin Dihapus: ')
                for i in range (len(listbuku)):
                    if listbuku[i]['isbn'] == delete_book_isbn:
                        ISBNtrue += 1
                        index_delete += i
                        break
                    else:
                        continue
                if ISBNtrue == 0:
                    print('\nBuku Dengan ISBN {} Tidak Ada Dalam Koleksi Perpustakaan Kami'.format(delete_book_isbn))
                    break
                elif ISBNtrue > 0:
                    print ('\nBerikut Data Buku dengan ISBN {}:'.format(delete_book_isbn))
                    print ('\nJudul Buku: {}\nGenre: {}\nAuthor: {}\nJumlah Buku: {} \nJumlah Peminjam Buku: {}\nSisa Buku: {} \nSynopsis: {}'.format(listbuku[index_delete]['namabuku'].title(), listbuku[index_delete]['genre'].title(), listbuku[index_delete]['author'].title(), listbuku[index_delete]['jml'], len(listbuku[index_delete]['peminjam']), listbuku[index_delete]['sisabuku'] ,listbuku[index_delete]['synopsis'].title()))
                    while True:
                        user_delete_yn = input('\nApakah Anda Yakin Ingin Menghapus Data Buku Tersebut? (Y/N): ').upper()
                        if user_delete_yn == 'Y':
                            del listbuku[index_delete]
                            print('\nData Buku Berhasil Dihapus!')
                            break
                        elif user_delete_yn == 'N':
                            print('Data Buku Tidak Jadi Dihapus')
                            break
                    break
                break
            break
        if user_delete == '2':
             break


                


while True:
    usermenu = input('''
    Selamat Datang di Perpustakaan "PANEN RAYA"
    Silahkan pilih menu yang ingin dijalankan:
    1. Jelajahi Koleksi Buku Perpustakaan
    2. Menambahkan Buku
    3. Update Database Perpustakaan
    4. Menghapus Buku dari Database Perpustakaan
    5. Exit Program 
    
    Menu yang ingin dijalankan: ''')

    if usermenu == '1':
        read()

    elif usermenu =='2':
        create()

    elif usermenu =='3':
        update()
    
    elif usermenu =='4':
        delete()
    
    elif usermenu == '5':
        break
    
    else:
        print('Input Menu Salah!!! Mohon Masukkan Pilihan Menu yang Sesuai! (1-5): ')