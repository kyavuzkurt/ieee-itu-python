def toplama(a, b):
    sonuc = a + b
    if sonuc.is_integer():
        return int(sonuc)
    else:
        return float(sonuc)

def cikarma(a, b):
    sonuc = a - b
    if sonuc.is_integer():
        return int(sonuc)
    else:
        return float(sonuc)

def carpma(a, b):
    sonuc = a * b
    if sonuc.is_integer():
        return int(sonuc)
    else:
        return float(sonuc)

def bolme(a, b):
    if b == 0:
        return "İşlem yapılamaz"
    sonuc = a / b
    if sonuc.is_integer():
        return int(sonuc)
    else:
        return float(sonuc)

def main():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    while True:
        islem = input("İşlem seçin: ")
        
        if islem == "1":
            a = float(input("İlk sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", toplama(a, b))
        elif islem == "2":
            a = float(input("İlk sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", cikarma(a, b))
        elif islem == "3":
            a = float(input("İlk sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", carpma(a, b))
        elif islem == "4":
            a = float(input("İlk sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            print("Sonuç: ", bolme(a, b))
        elif islem == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz işlem")

if __name__ == "__main__":
    main()