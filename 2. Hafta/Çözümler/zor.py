import json

with open('kitaplar.json', 'r', encoding='utf-8') as f:
    kitaplar = json.load(f)
with open('uyeler.json', 'r', encoding='utf-8') as f:
    uyeler = json.load(f)
with open('oduncler.json', 'r', encoding='utf-8') as f:
    oduncler = json.load(f)


while True:
    print("\n=== Kütüphane Yönetim Sistemine Hoş Geldiniz ===\n")
    print("1. Kitap Yönetimi")
    print("2. Üye Yönetimi")
    print("3. Ödünç Yönetimi")
    print("4. Raporlama")
    print("5. Çıkış\n")
    
    secim = input("Lütfen bir seçenek belirleyin (1-5): ")
    
    if secim == '1':
        # Kitap Yönetimi Menüsü
        while True:
            print("\n--- Kitap Yönetimi ---\n")
            print("1. Kitap Ekle")
            print("2. Kitap Sil")
            print("3. Stok Güncelle")
            print("4. Kitapları Görüntüle")
            print("5. Geri Dön\n")
            
            kitap_secim = input("Seçiminizi yapın (1-5): ")
            
            if kitap_secim == '1':
                # Kitap Ekleme İşlemi
                isim = input("Kitap İsmi: ")
                yazar = input("Yazar: ")
                tur = input("Tür: ")
                try:
                    stok = int(input("Stok Sayısı: "))
                except ValueError:
                    print("Geçerli bir stok sayısı giriniz.")
                    continue
                # Yeni kitap ID'si
                if len(kitaplar) == 0:
                    yeni_id = 1
                else:
                    yeni_id = kitaplar[-1]['id'] + 1
                yeni_kitap = {
                    "id": yeni_id,
                    "isim": isim,
                    "yazar": yazar,
                    "turu": tur,
                    "stok": stok
                }
                kitaplar.append(yeni_kitap)
                # JSON dosyasına yazma
                with open('kitaplar.json', 'w', encoding='utf-8') as f:
                    json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                print(f"{isim} adlı kitap eklendi.")
            
            elif kitap_secim == '2':
                # Kitap Silme İşlemi
                try:
                    silinecek_id = int(input("Silinecek kitabın ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                bulunamadi = True
                for kitap in kitaplar:
                    if kitap['id'] == silinecek_id:
                        kitaplar.remove(kitap)
                        bulunamadi = False
                        break
                if not bulunamadi:
                    with open('kitaplar.json', 'w', encoding='utf-8') as f:
                        json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                    print(f"ID {silinecek_id} olan kitap silindi.")
                else:
                    print("Kitap bulunamadı.")
            
            elif kitap_secim == '3':
                # Stok Güncelleme İşlemi
                try:
                    kit_id = int(input("Stok güncellenecek kitabın ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                for kitap in kitaplar:
                    if kitap['id'] == kit_id:
                        try:
                            yeni_stok = int(input(f"{kitap['isim']} için yeni stok sayısını girin: "))
                            kitap['stok'] = yeni_stok
                            with open('kitaplar.json', 'w', encoding='utf-8') as f:
                                json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                            print("Stok güncellendi.")
                        except ValueError:
                            print("Geçerli bir stok sayısı giriniz.")
                        break
                else:
                    print("Kitap bulunamadı.")
            
            elif kitap_secim == '4':
                # Kitapları Görüntüleme
                print("\n--- Kitaplar ---")
                for kitap in kitaplar:
                    print(f"ID: {kitap['id']}, İsim: {kitap['isim']}, Yazar: {kitap['yazar']}, Tür: {kitap['turu']}, Stok: {kitap['stok']}")
            
            elif kitap_secim == '5':
                # Geri Dön
                break
            else:
                print("Geçersiz seçim. Lütfen 1-5 arasında bir seçenek seçin.")
    
    elif secim == '2':
        # Üye Yönetimi Menüsü
        while True:
            print("\n--- Üye Yönetimi ---\n")
            print("1. Üye Ekle")
            print("2. Üye Sil")
            print("3. Üyeleri Görüntüle")
            print("4. Geri Dön\n")
            
            uye_secim = input("Seçiminizi yapın (1-4): ")
            
            if uye_secim == '1':
                # Üye Ekleme İşlemi
                isim = input("Üyenin Adı: ")
                soyisim = input("Üyenin Soyadı: ")
                telefon = input("Telefon Numarası: ")
                email = input("E-posta Adresi: ")
                # Yeni üye ID'si
                if len(uyeler) == 0:
                    yeni_uye_id = 1
                else:
                    yeni_uye_id = uyeler[-1]['id'] + 1
                yeni_uye = {
                    "id": yeni_uye_id,
                    "isim": isim,
                    "soyisim": soyisim,
                    "telefon": telefon,
                    "email": email
                }
                uyeler.append(yeni_uye)
                # JSON dosyasına yazma
                with open('uyeler.json', 'w', encoding='utf-8') as f:
                    json.dump(uyeler, f, ensure_ascii=False, indent=4)
                print(f"{isim} {soyisim} adlı üye eklendi.")
            
            elif uye_secim == '2':
                # Üye Silme İşlemi
                try:
                    silinecek_uye_id = int(input("Silinecek üyenin ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                bulunamadi = True
                for uye in uyeler:
                    if uye['id'] == silinecek_uye_id:
                        uyeler.remove(uye)
                        bulunamadi = False
                        break
                if not bulunamadi:
                    with open('uyeler.json', 'w', encoding='utf-8') as f:
                        json.dump(uyeler, f, ensure_ascii=False, indent=4)
                    print(f"ID {silinecek_uye_id} olan üye silindi.")
                else:
                    print("Üye bulunamadı.")
            
            elif uye_secim == '3':
                # Üyeleri Görüntüleme
                print("\n--- Üyeler ---")
                for uye in uyeler:
                    print(f"ID: {uye['id']}, İsim: {uye['isim']} {uye['soyisim']}, Telefon: {uye['telefon']}, Email: {uye['email']}")
            
            elif uye_secim == '4':
                # Geri Dön
                break
            else:
                print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek seçin.")
    
    elif secim == '3':
        # Ödünç Yönetimi Menüsü
        while True:
            print("\n--- Ödünç Yönetimi ---\n")
            print("1. Kitap Ödünç Al")
            print("2. Kitap İade Et")
            print("3. Ödünç Kayıtlarını Görüntüle")
            print("4. Geri Dön\n")
            
            odunc_secim = input("Seçiminizi yapın (1-4): ")
            
            if odunc_secim == '1':
                # Kitap Ödünç Alma
                try:
                    uye_id = int(input("Üye ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                # Üyenin varlığı
                for uye in uyeler:
                    if uye['id'] == uye_id:
                        break
                else:
                    print("Üye bulunamadı.")
                    continue
                try:
                    kitap_id = int(input("Ödünç alınacak kitabın ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                # Kitabın varlığı ve stok kontrolü
                for kitap in kitaplar:
                    if kitap['id'] == kitap_id:
                        if kitap['stok'] > 0:
                            break
                        else:
                            print("Kitabın stokta kalmadı.")
                            kitap = None
                            break
                else:
                    kitap = None
                if kitap is None:
                    print("Kitap bulunamadı veya stokta yok.")
                    continue
                # Ödünç kaydı oluşturma
                if len(oduncler) == 0:
                    yeni_odunc_id = 1
                else:
                    yeni_odunc_id = oduncler[-1]['odunc_id'] + 1
                odunc_tarihi = input("Ödünç tarihini girin (YYYY-AA-GG): ")
                yeni_odunc = {
                    "odunc_id": yeni_odunc_id,
                    "uye_id": uye_id,
                    "kitap_id": kitap_id,
                    "odunc_tarihi": odunc_tarihi,
                }
                oduncler.append(yeni_odunc)
                # Stok azaltma
                kitap['stok'] -= 1
                # JSON dosyalarına yazma
                with open('oduncler.json', 'w', encoding='utf-8') as f:
                    json.dump(oduncler, f, ensure_ascii=False, indent=4)
                with open('kitaplar.json', 'w', encoding='utf-8') as f:
                    json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                print(f"Kitap ödünç alındı. Ödünç ID: {yeni_odunc_id}")
            
            elif odunc_secim == '2':
                # Kitap İade Etme
                try:
                    odunc_id = int(input("İade edilecek ödünç kaydının ID'sini girin: "))
                except ValueError:
                    print("Geçerli bir ID giriniz.")
                    continue
                for odunc in oduncler:
                    if odunc['odunc_id'] == odunc_id:
                        if odunc['iade_tarihi'] == "":
                            odunc['iade_tarihi'] = input("İade tarihini girin (YYYY-AA-GG): ")
                            # Kitabın stokunu artırma
                            for kitap in kitaplar:
                                if kitap['id'] == odunc['kitap_id']:
                                    kitap['stok'] += 1
                                    break
                            # JSON dosyalarına yazma
                            with open('oduncler.json', 'w', encoding='utf-8') as f:
                                json.dump(oduncler, f, ensure_ascii=False, indent=4)
                            with open('kitaplar.json', 'w', encoding='utf-8') as f:
                                json.dump(kitaplar, f, ensure_ascii=False, indent=4)
                            print("Kitap iade edildi.")
                        else:
                            print("Bu ödünç kaydı zaten iade edilmiştir.")
                        break
                else:
                    print("Ödünç kaydı bulunamadı.")
            
            elif odunc_secim == '3':
                # Ödünç Kayıtlarını Görüntüleme
                print("\n--- Ödünç Kayıtları ---")
                for odunc in oduncler:
                    print(f"Ödünç ID: {odunc['odunc_id']}, Üye ID: {odunc['uye_id']}, Kitap ID: {odunc['kitap_id']}, Ödünç Tarihi: {odunc['odunc_tarihi']}, İade Tarihi: {odunc['iade_tarihi']}")
            
            elif odunc_secim == '4':
                # Geri Dön
                break
            else:
                print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek seçin.")
    
    elif secim == '4':
        # Raporlama Menüsü
        while True:
            print("\n--- Raporlama ---\n")
            print("1. En Çok Ödünç Alınan Kitaplar")
            print("2. En Aktif Üyeler")
            print("3. Geciken İadeler")
            print("4. Geri Dön\n")
            
            rapor_secim = input("Seçiminizi yapın (1-4): ")
            
            if rapor_secim == '1':
                # En Çok Ödünç Alınan Kitaplar
                kitap_odunc_sayisi = {}
                for odunc in oduncler:
                    kitap_id = odunc['kitap_id']
                    if kitap_id in kitap_odunc_sayisi:
                        kitap_odunc_sayisi[kitap_id] += 1
                    else:
                        kitap_odunc_sayisi[kitap_id] = 1
                # Sıralama
                sirali_odunc = sorted(kitap_odunc_sayisi.items(), key=lambda x: x[1], reverse=True)
                print("\n--- En Çok Ödünç Alınan Kitaplar ---")
                for kitap_id, sayi in sirali_odunc:
                    for kitap in kitaplar:
                        if kitap['id'] == kitap_id:
                            print(f"Kitap: {kitap['isim']} (ID: {kitap_id}), Ödünç Sayısı: {sayi}")
                            break
            
            elif rapor_secim == '2':
                # En Aktif Üyeler
                uye_odunc_sayisi = {}
                for odunc in oduncler:
                    uye_id = odunc['uye_id']
                    if uye_id in uye_odunc_sayisi:
                        uye_odunc_sayisi[uye_id] += 1
                    else:
                        uye_odunc_sayisi[uye_id] = 1
                # Sıralama
                sirali_odunc = sorted(uye_odunc_sayisi.items(), key=lambda x: x[1], reverse=True)
                print("\n--- En Aktif Üyeler ---")
                for uye_id, sayi in sirali_odunc:
                    for uye in uyeler:
                        if uye['id'] == uye_id:
                            print(f"Üye: {uye['isim']} {uye['soyisim']} (ID: {uye_id}), Ödünç Sayısı: {sayi}")
                            break
            
            elif rapor_secim == '3':
                # Geciken İadeler
                iade_tarihi_gir = input("Kontrol edilecek tarihi girin (YYYY-AA-GG): ")
                print(f"\n--- {iade_tarihi_gir} Tarihinden Sonra İade Edilmeyen Kitaplar ---")
                for odunc in oduncler:
                    if odunc['iade_tarihi'] == "" and odunc['odunc_tarihi'] < iade_tarihi_gir:
                        print(f"Ödünç ID: {odunc['odunc_id']}, Üye ID: {odunc['uye_id']}, Kitap ID: {odunc['kitap_id']}, Ödünç Tarihi: {odunc['odunc_tarihi']}")
            
            elif rapor_secim == '4':
                # Geri Dön
                break
            else:
                print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek seçin.")
    
    elif secim == '5':
        # Çıkış
        print("Kütüphane Yönetim Sisteminden çıkılıyor. İyi günler!")
        break
    
    else:
        print("Geçersiz seçim. Lütfen 1-5 arasında bir seçenek seçin.")