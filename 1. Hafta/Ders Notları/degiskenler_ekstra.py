# var değişkeni 42 olarak başlatılıyor.
var = 42
print(f"Step 1: {var} (type: {type(var)})")

# var değişkeni bir fonksiyon olarak değiştiriliyor.
def var(x):
    return x ** 2

print(f"Step 2 var(5): {var(5)} (type: {type(var)})") 

# var değişkeni bir sınıf olarak değiştiriliyor.
class var:
    def __init__(self, value):
        self.value = value

    def multiply(self, factor):
        return self.value * factor

# var değişkeni bir sınıfın bir örneği olarak değiştiriliyor.
instance = var(10)
print(f"Step 3: {instance.multiply(3)} (type: {type(var)})")

# var değişkeni kendi kendini dinamik olarak değiştiriliyor.
def dynamic_method(self, new_value):
    self.value = new_value

setattr(var, "change_value", dynamic_method) 

instance.change_value(99)
print(f"Step 4: {instance.value} (type: {type(var)})")
