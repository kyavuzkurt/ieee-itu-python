def count_letters(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

def main():
    text = input("Bir string girin: ")
    upper_count, lower_count = count_letters(text)
    print(f"Büyük harf sayısı: {upper_count}")
    print(f"Küçük harf sayısı: {lower_count}")

if __name__ == "__main__":
    main()