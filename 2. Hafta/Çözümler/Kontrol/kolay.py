sayilar = (1,2,3,4,5)
secim=input( "For veya While döngüsü seçiniz:")
if secim == "for":
    print("For loop çıktısı:")
    for num in sayilar:
        print(num)

elif secim== "While":
    print(" While loop çıktısı")
    i=0
    while i < len(sayilar):
        print(sayilar[i])
        i+=1

