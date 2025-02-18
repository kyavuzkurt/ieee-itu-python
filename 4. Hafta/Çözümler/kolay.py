from abc import ABC, abstractmethod
from typing import Dict, List

class EnvanterEsyasi(ABC):
    def __init__(self, ad: str, agirlik: float, dayaniklilik: int):
        self.ad = ad
        self.agirlik = agirlik
        self.dayaniklilik = dayaniklilik

    @abstractmethod
    def kullan(self):
        pass

    @abstractmethod
    def bilgi(self) -> str:
        pass

class Silah(EnvanterEsyasi):
    def __init__(self, ad: str, agirlik: float, dayaniklilik: int, hasar: int):
        super().__init__(ad, agirlik, dayaniklilik)
        self.hasar = hasar

    def kullan(self):
        self.dayaniklilik = max(self.dayaniklilik - 5, 0)
        print(f"{self.ad} kullanıldı! Kalan dayanıklılık: {self.dayaniklilik}")

    def bilgi(self) -> str:
        return f"Silah: {self.ad} | Hasar: {self.hasar} | Ağırlık: {self.agirlik}kg"

class Zirh(EnvanterEsyasi):
    def __init__(self, ad: str, agirlik: float, dayaniklilik: int, koruma: int):
        super().__init__(ad, agirlik, dayaniklilik)
        self.koruma = koruma

    def kullan(self):
        self.dayaniklilik = max(self.dayaniklilik - 3, 0)
        print(f"{self.ad} kullanıldı! Kalan dayanıklılık: {self.dayaniklilik}")

    def bilgi(self) -> str:
        return f"Zırh: {self.ad} | Koruma: {self.koruma} | Ağırlık: {self.agirlik}kg"

class Oyuncu:
    def __init__(self, ad: str, max_agirlik: float):
        self.ad = ad
        self.max_agirlik = max_agirlik
        self.envanter: List[EnvanterEsyasi] = []
        
    def agirlik_hesapla(self) -> float:
        return sum(esya.agirlik for esya in self.envanter)
    
    def esya_ekle(self, esya: EnvanterEsyasi):
        if self.agirlik_hesapla() + esya.agirlik > self.max_agirlik:
            print("Ağırlık limiti aşıldı! Eşya eklenemedi.")
            return
        self.envanter.append(esya)
        print(f"{esya.ad} envantere eklendi.")
    
    def esya_cikar(self, esya_ad: str):
        for esya in self.envanter:
            if esya.ad == esya_ad:
                self.envanter.remove(esya)
                print(f"{esya_ad} envanterden çıkarıldı.")
                return
        print("Eşya bulunamadı.")
    
    def esya_kullan(self, esya_ad: str):
        for esya in self.envanter:
            if esya.ad == esya_ad:
                esya.kullan()
                if esya.dayaniklilik <= 0:
                    self.esya_cikar(esya_ad)
                return
        print("Eşya bulunamadı.")
    
    def envanter_goster(self):
        print(f"\n{self.ad} Envanteri:")
        print(f"Toplam Ağırlık: {self.agirlik_hesapla()}/{self.max_agirlik}kg")
        for esya in self.envanter:
            print(f"- {esya.bilgi()}")

# Örnek Kullanım
if __name__ == "__main__":
    # Oyuncu oluşturma
    oyuncu = Oyuncu("GiantDad", 200.3)
    
    # Eşya ekleme
    kilic = Silah("Zweihander", 10.0, 200, 130)
    zirh = Zirh("Dev Zırhı", 50.0, 280, 372.8)
    
    # Envanter yönetimi
    oyuncu.esya_ekle(kilic)
    oyuncu.esya_ekle(zirh)
    
    # Envanter görüntüleme
    oyuncu.envanter_goster()
    
    # Eşya kullanımı
    oyuncu.esya_kullan("Zweihander")
    oyuncu.esya_kullan("Dev Zırhı")
    
    # Dayanıklılık testi
    for _ in range(5):
        oyuncu.esya_kullan("Zweihander")
    
    oyuncu.esya_cikar("Dev Zırhı")
    oyuncu.envanter_goster()