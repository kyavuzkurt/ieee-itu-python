array = [1, 2, 3, 4, 5]

loop = input("For veya While döngüsü seçiniz: ")

if loop == "For" or loop == "for":
    print("For loop çıktısı:")
    for i in array:
        print(i)
elif loop == "While" or loop == "while":
    print("While loop çıktısı:")
    i = 0
    while i < len(array):
        print(array[i])
        i += 1
else:
    print("Geçersiz döngü seçildi, lütfen For veya While seçiniz")


