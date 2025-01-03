import one

print("two.py içinde top-level çalıştırılıyor")
one.func()

if __name__ == "__main__":
    print("two.py direkt olarak çalıştırılıyor")
else:
    print("two.py başka bir modül tarafından çağrılıyor")
