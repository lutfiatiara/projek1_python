print("...............PROJEK 1...............")
print("1. Median ")
print("2. Urutan list(asc/desc) ")
print("3. Usaha energi & pesawat sederhana ")
print("4. Getaran, gelombang, cahaya dan tekanan ")
print("5. Suhu, kalor, dan, pemuaian ")
print("6. Teorema pythagoras ")
print("7. Menghitung luas dan volume bangun(bola, kerucut, prisma segitiga)")
PILIHAN = input("pilih kategori soal yang ingin ditampilkan(1-7): ")

if PILIHAN == "1":
    print("MEDIAN")
    def median(list_angka):
        if n % 2 == 1:
            median = list_angka[n // 2]
        else:
            median = (list_angka[n // 2 - 1] + list_angka[n // 2]) / 2
        return median
    n = int(input("masukan jumlah list angka: "))
    x = [0] * n

    for i in range(n):
        angka = int(input(f"masukkan angka {i + 1}: "))
        x[i] = angka

    print(f"median dari list angka tersebut adalah: {median(x)}")







#2. Urutan list(asc/desc)
#elif PILIHAN == "2":
    #print("URUTAN LIST(ASC/DESC)")


if PILIHAN == "3":
    print("USAHA ENERGI & PESAWAT SEDERHANA")
    print("a. energi potensial")
    print("b. energi mekanik")
    pilihan = input("pilih kategori nomor(a-b): ")   
    if pilihan == "a":
        def energi_potensial(m, g, h):
            energi_potensial = m * g * h
            print(f"besar energi potensial adalah: {energi_potensial} joule")
        m = int(input("masukkan nilai masa(kg): "))
        g = float(input("masukkan nilai gravitasi(9.8 m/s**2): "))
        h = int(input("masukkan nilai ketinggian(meter): "))
        energi_potensial(m, g, h)
    elif pilihan == "b":
        def energi_mekanik(m, v, g, h):
            energi_kinetik = 1/2 * m * v**2
            energi_potensial = m * g * h
            energi_mekanik = energi_kinetik * energi_potensial
            print(f"besar energi mekanik adalah: {energi_mekanik} joule")
        m = int(input("masukkan nilai massa(kg): "))
        v = int(input("masukkan nilai kecepatan(m/s): "))
        g = float(input("masukkan nilai gravitasi(9.8 m/s**2): "))
        h = int(input("masukkan nilai ketinggian benda(meter): "))
        energi_mekanik(m, v, g, h)
    else:
        print("pilihan tidak valid, pilih kategori yang ada(a-b)")

elif PILIHAN == "4":
    print("GETARAN, GELOMBANG, CAHAYA, DAN TEKANAN")
    print("a. cepat rambat gelombang")
    print("b. tekanan")
    pilihan = input("pilih kategori nomor(a atau b): ")
    if pilihan == "a":  
        def cepat_rambat_gelombang(panjang, periode):
            cepat_rambat_gelombang = panjang / periode
            print(f"Cepat rambat gelombang yaitu: {cepat_rambat_gelombang} m/s")
        panjang = int(input("masukkan nilai panjang gelombang(meter): "))
        periode = int(input("masukkan nilai periode(detik): "))
        cepat_rambat_gelombang(panjang, periode)
    elif pilihan == "b": 
        def tekanan(F, A): 
            tekanan = F / A
            print(f"nilai tekanan-nya adalah: {tekanan} N/m**2")
        F = int(input("masukkan nilai gaya(newton): "))
        A = int(input("masukkan nilai luas bidang(A): "))
        tekanan(F, A)
    else:
        print("pilihan tidak valid, pilih kategori yang ada(a atau b)")

elif PILIHAN == "5":
    print("SUHU, KALOR, DAN PEMUAIAN")
    def konverensi_suhu(c,f,k,r):
        c_ke_f = (9/5 * c) + 32
        c_ke_k = c + 273.15
        c_ke_r = 4/5 * c
        f_ke_c = 5/9 * (f - 32)
        f_ke_k = 5/9 * (f - 32) + 273.15
        f_ke_r = (f - 32) * 4/9
        k_ke_c = k - 273.15
        k_ke_f = (k - 273.15) * 9/5 + 32
        k_ke_r = (k - 273.15) * 4/5
        r_ke_c = r * 5/4  
        r_ke_f = (9/4 * r) + 32
        r_ke_k = (5/4 * r) + 273.15
        print("<Celcius>"*5)
        print("celcius ke fahrenheit adalah", c_ke_f,"fahrenheit")
        print("celcius ke kelvin adalah",c_ke_k,"kelvin")
        print("celcius ke reamur adalah",c_ke_r,"reamur")
        print("<Fahremheit>"*5)
        print("fahrenheit ke celcius adalah",f_ke_c,"celcius")
        print("fahrenheit ke kelvin adalah",f_ke_k,"kelvin")
        print("fahrenheit ke reamur adalah",f_ke_r,"reamur")
        print("<Kelvin>"*5)
        print("kelvin ke celcius adalah",k_ke_c,"celcius")
        print("kelvin ke fahrenheir adalah",k_ke_f,"fahrenheit")
        print("kelvin ke reamur adalah",k_ke_r,"reamur")
        print("<Reamur>"*5)
        print("reamur ke celcius adalah",r_ke_c,"celcius")  
        print("reamur ke celcius adalah",r_ke_f,"faHrenheit")
        print("reamur ke celcius adalah",r_ke_k,"kelvin") 
    c = int(input("masukkan suhu celcius: "))
    f = int(input("masukkan suhu faHrenheit: "))
    k = int(input("masukkan suhu kelvin: "))
    r = int(input("masukkan suhu reamur: "))
    konverensi_suhu(c,f,k,r)
    
elif PILIHAN == "6":
    print("TEOREMA PYTHAGORAS")
    def teorema_pythagoras(a,b):
        c = a**2 + b**2
        c_2 = c ** 0.5
        print(f"c nilainya adalah {c}, sedangkan c**2 nilainya adalah {c_2}")
    a = int(input("masukkan panjang sisi a ="))
    b = int(input("masukkan panjang sisi b ="))
    teorema_pythagoras(a,b)

elif PILIHAN == "7":
    print("MENGHITUNG LUAS DAN VOLUME BANGUN(BOLA, KERUCUT, PRISMA SEGITIGA)")
    print("a. bangun ruang bola")
    print("b. bangun ruang kerucut")
    print("c. bangun ruang prisma segitiga")
    PILIHAN = input("pilih kategori(a-c): ")
    if PILIHAN == "a":
        def bola(r):
            luas = 4 * 3.14 * r**2
            volume = (4/3) * 3.14 * r**3
            print("luas bangun ruang bola tersebut adalah:", luas)
            print("volume bangun ruang bola tersebut adalah:", volume)
        r = int(input("masukkan nilai jari-jari = "))    
        bola(r)
    elif PILIHAN == "b":
        def kerucut(r, t, garis_pelukis):
            luas = ((22/7) * r**2)
            volume = (1/3) * (22/7) * r**2 * t
            print("luas bangun ruang kerucut tersebut adalah:", luas)
            print("volume bangun ruang kerucut tersebut adalah:", volume)
        r = int(input("masukkan nilai jari-jari: "))
        t = int(input("masukkan nilai tinggi: "))
        garis_pelukis = int(input("masukkan nilai garis pelukis: "))
        kerucut(r, t, garis_pelukis)
    elif PILIHAN == "c":
        def prisma_segitiga(a, t, sisi1, sisi2, sisi3, tp) :
            luas = 2 * (1/2 * a * t) + (sisi1 + sisi2 + sisi3) * tp   
            volume = (1/2 * a * t) * tp
            print("luas bangun ruang prisma segitiga tersebut adalah:",luas)
            print("volume bangun ruang prisma segitiga tersebut adalah:",volume)
        a = int(input("masukkan nilai alas segitiga: "))
        t = int(input("masukkan nilai tinggi segitiga: "))
        sisi1 = int(input("masukkan nilai sisi1: "))
        sisi2 = int(input("masukkan nilai sisi2: "))
        sisi3 = int(input("masukkan nilai sisi3: "))
        tp = int(input("masukkan nilai tinggi prisma: "))
        prisma_segitiga(a, t, sisi1, sisi2, sisi3, tp)
    else:
        print("pilihan tidak valid, pilihlah kategori yg tersedia()")

else:
    print("pilihan tidak valid silahkan masukkan kategori soal yang ada(1-7)")