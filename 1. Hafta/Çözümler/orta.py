a1 = float(input("1. Sayıyı giriniz: "))
a2 = float(input("2. Sayıyı giriniz: "))


print(f"Toplam: {a1 + a2}")
print(f"Çarpım: {a1 * a2}")
print(f"Fark: {a1 - a2}")
if a2 != 0:
    print(f"Bölüm: {a1 / a2}")
else:
    print("Bölüm işlemi yapılamaz")
