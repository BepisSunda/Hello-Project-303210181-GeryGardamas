file = open('data.txt','r')

x = file.read()
var = x.split('\n')
rental = dict()

for i in var :
    val = i.split(' ')
    key = val[1]
    sewa = int(val[2])
    tanggal = val[0].split("-")
    value = [int(tanggal[1]),sewa]
    if key in rental.keys():
        rental[key] += [value]
    else:
        rental[key] = [value]

def favorit():
    sewaterbanyak = 0
    mobilfavorit= None
    for mobil in rental:
        jumlahsewa = 0
        for i in rental[mobil]:
            jumlahsewa = jumlahsewa + i[1]
        if sewaterbanyak < jumlahsewa:
            sewaterbanyak = jumlahsewa
            mobilfavorit = mobil
    print("Mobil Terfavorit adalah")           
    return mobilfavorit

def report():
    x = True
    while x:
        for mobil in rental:
            print(mobil)
        namamobil = input("Pilih Data Mobil Yang Akan Ditampilkan")

        laporan = dict()
        for mobil in rental:
            laporan[mobil] = 0
            totalsewa = 0
            for sewa in rental[mobil]:
                for i in range(1,13):
                    if sewa[0] == i:
                        totalsewa = totalsewa + sewa[1]
            laporan[mobil] = totalsewa/12

        x = False
        print("Rata-Rata Sewa Dari mobil {}".format(namamobil))                
    return laporan[namamobil]            

def main_program():
    print("=========================================")
    print("[1] Print Nilai Dictionary Rental Mobil")
    print("[2] Cek Mobil Sewa Terfavorit") 
    print("[3] Cek Hasil Rata-Rata Dari Tiap Bulannya")
    print("[4] Hentikan Program")

x = True
while x :
    main_program()
    pilih = input("masukan pilihan :")
    if pilih == "1":
        print("=========================================")
        print("Dictionary Rental Mobil")
        print(rental)
    elif pilih == "2":
        print("=========================================")
        print(favorit())
    elif pilih == "3":
        print("=========================================")
        print(report())
    elif pilih == "4":
        x = False  