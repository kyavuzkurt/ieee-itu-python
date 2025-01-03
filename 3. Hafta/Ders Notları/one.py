def func():
    print("one.py içinde func() çalıştırılıyor")

print("one.py içinde top-level çalıştırılıyor")

if __name__ == "__main__":
    print("one.py direkt olarak çalıştırılıyor")
else:
    print("one.py başka bir modül tarafından çağrılıyor")
