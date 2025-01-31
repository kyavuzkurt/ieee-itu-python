secenekler= ["1. Öğrenci Ekle","2. Öğrenci sil","3. Not Ekle","4. Öğrenci Notlarını Görüntüle","5. Ortalama Hesapla","6. Geçme Durumunu Kontrol Et","7. Sınıfın Genel Ortalamasını Hesapla","8. En Yüksek ve En Düşük Notları Bul","9. Çıkış"]
a_not = [85,90,78]
z_not = [92,88,95]
e_not = [75,80,68]
ogrenciler = {
    "Ali": a_not,
    "Zehra": z_not,
    "Efe": e_not
}
print("Öğrenci Not Yönetim Sistemine Hoş Geldiniz!")
while 1:
    a = 0
    for i in secenekler:
        print(i)
    secim=input("Yapmak istediğiniz işlemi seçin:")
    if secim =="1":
        ekle_ad = input("Öğrencinin ismi:")
        bos=[]
        ogrenciler.update({ekle_ad:bos})
        print(f"{ekle_ad} sınıfa eklendi.")
        
    elif secim == "2":
        while 1:
            sil_ad = input("Silinecek öğrenci ismi:")
            if sil_ad in ogrenciler:
                ogrenciler.pop(sil_ad)
                print(f"{sil_ad} sınıftan silindi.")
                break
            else:
                print("Lütfen sınıfta bulunan bir öğrenci ismi yazın.")
                continue

    elif secim == "3":
        while a == 0:
            not_ekle_ad = input("Not eklenecek öğrenci ismi:")
            if not_ekle_ad in ogrenciler:
                if len(ogrenciler.get(not_ekle_ad)) == 3:
                    print("Bu öğrencinin tüm notları girilmiştir.")
                    break
                else:
                    while 1:
                        try:
                            not_ekle = int(input("Eklenecek notu girin:"))
                        except:
                            print("Lütfen geçerli bir not giriniz.")
                            continue
                        else:
                            if not_ekle <= 100:
                                not_ekle_list = ogrenciler.get(not_ekle_ad)
                                not_ekle_list.append(not_ekle)
                                print(f"{not_ekle_ad} isimli öğrenciye {not_ekle} notu eklendi.")
                                a = 1
                                break
                            else:
                                print("Lütfen geçerli bir not giriniz.")
                                continue      
            else:
                print("Lütfen sınıfta bulunan bir öğrenci ismi yazın.")
                continue
    elif secim =="4":
        while 1:
            not_gör_ad = input("Notları görüntülemek istediğiniz öğrenci ismi:")
            if not_gör_ad in ogrenciler:
                not_gör = ogrenciler.get(not_gör_ad)
                print(f"{not_gör_ad} isimli öğrencinin notları:{not_gör}")
                break
            else:
                print("Lütfen sınıfta bulunan bir öğrenci ismi yazın.")
                continue       
    elif secim == "5":
        while 1:
            ort_ad = input("Ortalaması hesaplanacak öğrenci ismi:")
            if ort_ad in ogrenciler:
                ort_not = ogrenciler.get(ort_ad)
                ort = round(sum(ort_not)/3,1)
                print(f"{ort_ad} isimli öğrencinin ortalaması: {ort}")
                break
            else:
                print("Lütfen sınıfta bulunan bir öğrenci ismi yazın.")
                continue
    elif secim == "6":
        while 1:
            geç_ad = input("Geçme durumu kontrol edilecek öğrenci ismi:")
            if geç_ad in ogrenciler:
                ort_not2 = ogrenciler.get(geç_ad)
                ort2 = round(sum(ort_not2)/3,1)
                if ort2 < 65:
                    print(f"{geç_ad} isimli öğrenci, {ort2} ortlaması ile kaldı.")
                    break
                else:
                    print(f"{geç_ad} isimli öğrenci, {ort2} ortlaması ile geçti.")
                    break
            else:
                print("Lütfen sınıfta bulunan bir öğrenci ismi yazın.")
                continue
    elif secim =="7":
        x = []
        for i in ogrenciler:
            x.append(sum(ogrenciler.get(i))/3)
        snf_ort =round(sum(x)/len(x),2)
        print(f"Sınıfın genel ortalaması: {snf_ort}")
    elif secim == "8":
        tüm_notlar = []
        for i in ogrenciler:
            not_list = ogrenciler.get(i)
            tüm_notlar.extend(not_list)
        max = max(tüm_notlar)
        min = min(tüm_notlar)
        print(f"Sınıftaki en yüksek not: {max}")
        print(f"Sınıftaki en düşük not: {min}")
    elif secim == "9":
        print("Çıkış yapılıyor. İyi günler!")
        break
    else:
        print("Lütfen geçerli bir tercih yapınız.")
        continue

