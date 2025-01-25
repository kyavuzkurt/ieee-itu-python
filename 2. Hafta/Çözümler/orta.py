sinif = {
    "Ali": [85.0, 90.0, 78.0],
    "Zehra": [92.0, 88.0, 95.0],
    "Efe": [75.0, 80.0, 68.0]
}

while True:
    print("\nÖğrenci Not Yönetim Sistemine Hoş Geldiniz!\n")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Not Ekle")
    print("4. Öğrenci Notlarını Görüntüle")
    print("5. Ortalama Hesapla")
    print("6. Geçme Durumunu Kontrol Et")
    print("7. Sınıfın Genel Ortalamasını Hesapla")
    print("8. En Yüksek ve En Düşük Notları Bul")
    print("9. Çıkış\n")
    
    secim = input("Seçiminizi yapın (1-9): ")
    
    if secim == '1':
        isim = input("Öğrenci ismi: ")
        if isim in sinif:
            print(f"{isim} zaten mevcut.")
        else:
            sinif[isim] = []
            print(f"{isim} sınıfa eklendi.")
    
    elif secim == '2':
        isim = input("Silinecek öğrenci ismi: ")
        if isim in sinif:
            del sinif[isim]
            print(f"{isim} sınıftan silindi.")
        else:
            print(f"{isim} bulunamadı.")
    
    elif secim == '3':
        isim = input("Not eklenecek öğrenci ismi: ")
        if isim in sinif:
            try:
                not_degeri = float(input("Eklenecek notu girin: "))
                sinif[isim].append(not_degeri)
                print(f"{isim} isimli öğrenciye {not_degeri} notu eklendi.")
            except ValueError:
                print("Geçerli bir not değeri girin.")
        else:
            print(f"{isim} bulunamadı.")
    
    elif secim == '4':
        isim = input("Notları görüntülemek istediğiniz öğrenci ismi: ")
        if isim in sinif:
            print(f"{isim} isimli öğrencinin notları: {sinif[isim]}")
        else:
            print(f"{isim} bulunamadı.")
    
    elif secim == '5':
        isim = input("Ortalaması hesaplanacak öğrenci ismi: ")
        if isim in sinif and sinif[isim]:
            toplam = 0
            sayac = 0
            for notu in sinif[isim]:
                toplam += notu
                sayac += 1
            ortalama = toplam / sayac
            ortalama = round(ortalama, 2)
            print(f"{isim} isimli öğrencinin ortalaması: {ortalama}")
        else:
            print(f"{isim} için not bulunamadı veya liste boş.")
    
    elif secim == '6':
        isim = input("Geçme durumu kontrol edilecek öğrenci ismi: ")
        if isim in sinif and sinif[isim]:
            toplam = 0
            sayac = 0
            for notu in sinif[isim]:
                toplam += notu
                sayac += 1
            ortalama = toplam / sayac
            ortalama = round(ortalama, 2)
            if ortalama >= 60:
                print(f"{isim} isimli öğrenci, {ortalama} ortalama ile geçti. ")
            else:
                print(f"{isim} isimli öğrenci, {ortalama} ortalama ile kaldı. ")
        else:
            print(f"{isim} için not bulunamadı veya liste boş.")
    
    elif secim == '7':
        toplam = 0
        sayac = 0
        for notlar in sinif.values():
            for notu in notlar:
                toplam += notu
                sayac += 1
        if sayac > 0:
            genel_ortalama = toplam / sayac
            genel_ortalama = round(genel_ortalama, 2)
            print(f"Sınıfın genel ortalaması: {genel_ortalama}")
        else:
            print("Sınıfta not bulunmuyor.")
    
    elif secim == '8':
        en_yuksek = -float('inf')
        en_dusuk = float('inf')
        for notlar in sinif.values():
            for notu in notlar:
                if notu > en_yuksek:
                    en_yuksek = notu
                if notu < en_dusuk:
                    en_dusuk = notu
        if en_yuksek != -float('inf') and en_dusuk != float('inf'):
            print(f"Sınıftaki en yüksek not: {en_yuksek}")
            print(f"Sınıftaki en düşük not: {en_dusuk}")
        else:
            print("Sınıfta not bulunmuyor.")
    
    elif secim == '9':
        print("Çıkış yapılıyor. İyi günler!")
        break
    
    else:
        print("Geçersiz seçim. Lütfen 1-9 arasında bir seçenek seçin.")