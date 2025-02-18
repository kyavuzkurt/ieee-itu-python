from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class Kitap(ABC):
    """Abstract base class for all book types"""
    def __init__(self, isbn: str, baslik: str, yazar: str, stok: int):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.stok = stok

    @abstractmethod
    def check_out(self) -> bool:
        """Abstract method for borrowing a book"""
        pass

    @abstractmethod
    def iade_et(self) -> bool:
        """Abstract method for returning a book"""
        pass

class KurguEser(Kitap):
    """Fiction book subclass"""
    def check_out(self) -> bool:
        if self.stok > 0:
            self.stok -= 1
            return True
        return False

    def iade_et(self) -> bool:
        self.stok += 1
        return True

class Ansiklopedi(Kitap):
    """Encyclopedia subclass"""
    def check_out(self) -> bool:
        if self.stok > 0:
            self.stok -= 1
            return True
        return False

    def iade_et(self) -> bool:
        self.stok += 1
        return True

class Uye:
    """Member class to track user information"""
    def __init__(self, uye_id: str, ad: str):
        self.uye_id = uye_id
        self.ad = ad
        self.odunc_kitaplar: List[Kitap] = []

    def kitap_odunc_al(self, kitap: Kitap) -> bool:
        """Borrow a book and add to member's list"""
        if kitap.check_out():
            self.odunc_kitaplar.append(kitap)
            return True
        return False

    def kitap_iade_et(self, kitap: Kitap) -> bool:
        """Return a book and remove from member's list"""
        if kitap in self.odunc_kitaplar:
            kitap.iade_et()
            self.odunc_kitaplar.remove(kitap)
            return True
        return False

class Kutuphane:
    """Main library management system"""
    def __init__(self):
        self.kitaplar: Dict[str, Kitap] = {}
        self.uyeler: Dict[str, Uye] = {}

    def kitap_ekle(self, kitap: Kitap):
        """Add new book to library"""
        self.kitaplar[kitap.isbn] = kitap

    def uye_kaydet(self, uye: Uye):
        """Register new member"""
        self.uyeler[uye.uye_id] = uye

    def odunc_al(self, isbn: str, uye_id: str) -> bool:
        """Handle book checkout process"""
        if isbn not in self.kitaplar or uye_id not in self.uyeler:
            return False
            
        kitap = self.kitaplar[isbn]
        uye = self.uyeler[uye_id]
        return uye.kitap_odunc_al(kitap)

    def iade_et(self, isbn: str, uye_id: str) -> bool:
        """Handle book return process"""
        if isbn not in self.kitaplar or uye_id not in self.uyeler:
            return False
            
        kitap = self.kitaplar[isbn]
        uye = self.uyeler[uye_id]
        return uye.kitap_iade_et(kitap)

    def stok_durumu(self, isbn: str) -> Optional[int]:
        """Check stock status for a book"""
        if isbn in self.kitaplar:
            return self.kitaplar[isbn].stok
        return None

# Örnek Kullanım
if __name__ == "__main__":
    # Kütüphane örneği oluştur
    kutuphane = Kutuphane()

    # Kitaplar oluştur
    kurgu_kitap = KurguEser("978-1", "Suç ve Ceza", "Dostoyevski", 3)
    ansiklopedi = Ansiklopedi("978-2", "Dünya Tarihi", "John Smith", 2)

    # Kitapları kütüphaneye ekle
    kutuphane.kitap_ekle(kurgu_kitap)
    kutuphane.kitap_ekle(ansiklopedi)

    # Üyeler oluştur
    uye1 = Uye("U001", "Ahmet Yılmaz")
    uye2 = Uye("U002", "Ayşe Demir")

    # Üyeleri kütüphaneye kaydet
    kutuphane.uye_kaydet(uye1)
    kutuphane.uye_kaydet(uye2)

    # Kitap ödünç alma işlemleri
    print(f"Stok durumu (Suç ve Ceza): {kutuphane.stok_durumu('978-1')}")  # 3
    
    # Ahmet bir kitap ödünç alıyor
    kutuphane.odunc_al("978-1", "U001")
    print(f"Stok durumu (Suç ve Ceza): {kutuphane.stok_durumu('978-1')}")  # 2
    
    # Ayşe bir kitap ödünç alıyor
    kutuphane.odunc_al("978-1", "U002")
    print(f"Stok durumu (Suç ve Ceza): {kutuphane.stok_durumu('978-1')}")  # 1

    # Ahmet kitabı iade ediyor
    kutuphane.iade_et("978-1", "U001")
    print(f"Stok durumu (Suç ve Ceza): {kutuphane.stok_durumu('978-1')}")  # 2

    # Olmayan bir kitap için stok kontrolü
    print(f"Olmayan kitap stok durumu: {kutuphane.stok_durumu('999-9')}")  # None
    