import json
import random
import os
import time
from datetime import datetime 

DataPengguna = "Data.json"

waktu = datetime.now()
hari = waktu.day
bulan = waktu.month
tahun = waktu.year 
tanggal = "{}/{}/{}".format(hari,bulan,tahun)

jam = datetime.now().strftime("%H:%M")

def clean():
    os.system('cls')

def read():
    try :
        with open (DataPengguna , 'r') as DataTampilan:
            cekdata = json.load(DataTampilan)
        return cekdata
    except FileNotFoundError:
        Isidata = []
        with open (DataPengguna , 'w') as DataTampilan:
            json.dump(Isidata , DataTampilan , indent = 4)
        return Isidata

def write(cekdata): 
    with open (DataPengguna , 'w') as DataTampilan:
        json.dump(cekdata , DataTampilan , indent= 4)

def daftar():
    clean()

    choice1 = input("Masukkan Username : ")
    userdata = read()

    for sistem in userdata:
        if sistem["Username"] == choice1 :
            print("Username sudah terdata")
            time.sleep(0.5)
            daftar()

    choice2 = input("Masukkan Password : ")

    Newdata = {
        "Username" : choice1,
        "Password" : choice2
    }

    userdata.append(Newdata)
    write(userdata)
    print("Selamat username anda sudah terdata")
    time.sleep(1)
    clean()
    Log_in()

def Login():
    global user

    clean()
    Ur_Us = input("Masukkan Username anda : ")
    Ur_Pw = input("Masukkan Password anda : ")
    userdata = read()
    status = False
    for sistem in userdata:
        if sistem["Username"] == Ur_Us and sistem["Password"] == Ur_Pw :
            user = sistem["Username"]
            status = True

    if status:
        clean()
        print("Login anda sukses")
        time.sleep(1)
        clean()
        tampilan_menu()
    else : 
        clean()
        print("Login anda gagal")
        time.sleep(0.5)
        clean()
        Login()

def pilihan1():
    clean()
    x = 0
    h = 0
    i = 0

    temp = []
    while x <= 4:
        
        pilihan = [ 
            'PEMAIN BOLA APA YANG BERATNYA 3 KG?',
            'PENYANYI YANG RAMBUTNYA GAK LURUS?',
            'SIAPA PRESIDEN YANG IMUT?',
            'SIAPA PENYANYI YANG GA SUKA NGEBUT?',
            'GUBERNUR APA YANG SUKA NYANYI?',
            'POCONG APA YANG DISAYANG IBU-IBU?',
            'BUAH APA YANG BIKIN WASPADA?'
        ]

        masuk = True

        while masuk:
            a = random.choice(pilihan)

            if a in temp:
                continue
            else:
                temp.append(a)
                print(a)
                masuk = False

        x += 1
        c = input("Masukkan Jawaban Anda: ")
        b = c.lower()
        if a == "PEMAIN BOLA APA YANG BERATNYA 3 KG?":
            if b == "bambang tabung gas":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "PENYANYI YANG RAMBUTNYA GAK LURUS?":
            if b == "ayu keriting":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "SIAPA PRESIDEN YANG IMUT?":
            if b == "kim jong unch":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "SIAPA PENYANYI YANG GA SUKA NGEBUT?":
            if b == "melly goes slow":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "GUBERNUR APA YANG SUKA NYANYI?":
            if b == "biduan kemil":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "POCONG APA YANG DISAYANG IBU-IBU?":
            if b == "pocongan harga":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "BUAH APA YANG BIKIN WASPADA?":
            if b == "buahaya":
                h += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                i += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue

    print("Point yang didapatkan")
    print(f'benar = {h}')
    print(f'salah = {i}')
    time.sleep(3)
    clean()
    tampilan_menu()
    
def pilihan2():
    clean()
    y = 0
    j = 0
    k = 0
    
    temp = []
    while y <= 4:
        pilihan = [ 
            'Panda - panda apa yang bikin seneng?',
            'Malam apa yang paling indah?',
            'Awan apa yang membuatku bahagia?',
            'Tinta apa yang tidak bisa luntur?',
            'Kucing apa yang super romantis?',
            'Micin apa yang rasanya manis?',
            'Cuka apa yang paling manis?'
        ]

        masuk = True

        while masuk:
            a = random.choice(pilihan)

            if a in temp:
                continue
            else:
                temp.append(a)
                print(a)
                masuk = False

        y += 1
        b = input("Masukkan Jawaban Anda: ")
        d =  b.lower()
        if a == "Panda - panda apa yang bikin seneng?":
            if d == "pandangin kamu":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Malam apa yang paling indah?":
            if d == "melamar kamu":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else: 
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Awan apa yang membuatku bahagia?":
            if d == "awanna be with you":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Tinta apa yang tidak bisa luntur?":
            if d == "tintaku padamu":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Kucing apa yang super romantis?":
            if d == "kucingta padamu":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Micin apa yang rasanya manis?":
            if d == "mi cinta you":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue
        elif a == "Cuka apa yang paling manis?":
            if d == "cuka cama kamu":
                j += 1
                print("Selamat Anda Benar")
                time.sleep(0.5)
                clean()
            else:
                k += 1
                print("Maaf Anda Salah")
                time.sleep(0.5)
                clean()
                continue

    print("Point yang didapatkan")
    print(f'benar = {j}')
    print(f'salah = {k}')
    time.sleep(3)
    clean()
    tampilan_menu()

def log_out():
    inp = input('Apakah Anda Ingin Keluar [Ya/Tidak] ? :')
    c = inp.lower()
    
    if c == "Ya"  or c == "ya":
        log_out2()
    else:
        clean()
        tampilan_menu()
        

def log_out2():
    clean()
    print("Terima kasih atas kunjungannya")

def tampilan_menu():
    pesan = ''
    if jam[0:2] >= '0' and jam[0:2] <= '10':
        pesan = 'Selamat Pagi'
    if jam[0:2] >= '11' and jam[0:2] <= '14':
        pesan = 'Selamat Siang'
    if jam[0:2] >= '15' and jam[0:2] <= '17':
        pesan = 'Selamat Sore'
    if jam[0:2] >= '18' and jam[0:2] <= '23':
        pesan = 'Selamat Malam'

    print('{} {} {}, di Tebak-tebakan\n\n============ MENU ============\n\n   [1] TEBAK LUCU\n   [2] TEBAK PERASAAN\n   [3] LOG OUT\n'.format(pesan, user, tanggal))

    pilih = int(input("\n>> Masukkan menu yang anda pilih : "))
    if pilih == 1:
        pilihan1()
    elif pilih == 2:
        pilihan2()
    elif pilih == 3:
        log_out()
    else:
        print('Menu yang anda masukan tidak tersedia!')
        time.sleep(1)
        clean()
        tampilan_menu()

def Log_in():
    print('Selamat Datang!\nSilahkan login atau daftar terlebih dahulu\n\n   [1] Login\n   [2] Daftar')
    Masukkan = input("\n>> Masukan pilihan : ")

    if Masukkan == '1' :
        Login()
    elif Masukkan == '2' :
        daftar()
    else:
        print('Menu yang anda masukan salah!')
        time.sleep(1)
        clean()
        Log_in()

clean()
Log_in()