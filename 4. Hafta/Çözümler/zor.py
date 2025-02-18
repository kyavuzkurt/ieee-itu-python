from abc import ABC, abstractmethod
from collections import deque
import matplotlib.pyplot as plt

# Strateji Pattern için soyut arayüz
class RotaStratejisi(ABC):
    """Rota hesaplama algoritmaları için temel arayüz"""
    @abstractmethod
    def rota_hesapla(self, harita, baslangic, hedef):
        """Soyut metot: Türetilen sınıflarda implemente edilmeli"""
        pass

class Konum:
    """Harita üzerindeki bir lokasyonu ve bağlantıları temsil eder"""
    def __init__(self, isim, x=0, y=0):
        self.isim = isim  # Konum adı
        self.x = x        # X koordinatı (görselleştirme için)
        self.y = y        # Y koordinatı (görselleştirme için)
        self.komsular = {}  # {Konum: maliyet} şeklinde komşuluk ilişkileri
    
    def baglanti_ekle(self, komsu, maliyet=1):
        """Bu konuma yeni bir komşu ekler (graph edge)"""
        self.komsular[komsu] = maliyet

class Harita:
    """Tüm konumları ve bağlantıları yöneten ana sınıf"""
    def __init__(self):
        self.konumlar = {}  # {isim: Konum} şeklinde konum kaydı
        self.strateji = None  # Aktif rota bulma stratejisi
    
    def set_strateji(self, strateji):
        """Çalışma zamanında rota stratejisi değiştirmek için"""
        self.strateji = strateji
    
    def konum_ekle(self, konum):
        """Haritaya yeni bir konum ekler (graph node)"""
        self.konumlar[konum.isim] = konum
    
    def baglanti_ekle(self, kaynak, hedef, maliyet=1, iki_yonlu=True):
        """İki konum arasında bağlantı oluşturur (graph edge)"""
        if kaynak not in self.konumlar or hedef not in self.konumlar:
            raise ValueError("Konumlar haritada bulunmalı")
        # Çift yönlü bağlantı için her iki konuma da ekleme yap
        self.konumlar[kaynak].baglanti_ekle(self.konumlar[hedef], maliyet)
        if iki_yonlu:
            self.konumlar[hedef].baglanti_ekle(self.konumlar[kaynak], maliyet)
    
    def rota_bul(self, baslangic, hedef):
        """Seçili stratejiyi kullanarak rota hesaplar"""
        if not self.strateji:
            raise RuntimeError("Rota stratejisi seçilmedi")
        return self.strateji.rota_hesapla(self, baslangic, hedef)

    def visualize(self):
        """Haritayı matplotlib ile görselleştirme"""
        plt.figure(figsize=(12, 8))
        
        # Kenarları çiz
        drawn_edges = set()
        for konum in self.konumlar.values():
            for komsu, maliyet in konum.komsular.items():
                if (komsu.isim, konum.isim) not in drawn_edges:
                    plt.plot([konum.x, komsu.x], [konum.y, komsu.y], 
                            'grey', linestyle='dotted', alpha=0.7)
                    plt.text((konum.x+komsu.x)/2, (konum.y+komsu.y)/2+2, 
                            str(maliyet), color='blue', fontsize=8)
                    drawn_edges.add((konum.isim, komsu.isim))
        
        # Düğümleri çiz
        for konum in self.konumlar.values():
            plt.scatter(konum.x, konum.y, s=300, color='red', zorder=5)
            plt.text(konum.x, konum.y+15, konum.isim, 
                    ha='center', va='bottom', fontsize=10, weight='bold')
        
        plt.title("Türkiye Şehir Bağlantı Haritası\n(Dijkstra vs BFS Rota Optimizasyonu)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

class Dijkstra(RotaStratejisi):
    """Dijkstra Algoritması: Maliyet optimizasyonlu en kısa yol"""
    def rota_hesapla(self, harita, baslangic, hedef):
        baslangic_konum = harita.konumlar[baslangic]
        hedef_konum = harita.konumlar[hedef]
        
        # Başlangıç maliyetlerini sonsuz, kaynağı 0 yap
        maliyetler = {konum: float('inf') for konum in harita.konumlar.values()}
        maliyetler[baslangic_konum] = 0
        
        oncekiler = {}  # Optimal yol için geri izleme
        islenmemis = list(harita.konumlar.values())  # İşlenmemiş düğümler
        
        while islenmemis:
            # En düşük maliyetli düğümü seç
            suanki_konum = min(islenmemis, key=lambda k: maliyetler[k])
            
            if maliyetler[suanki_konum] == float('inf'):
                break  # Ulaşılamayan düğümler için çık
            
            # Komşuların maliyetlerini güncelle
            for komsu, maliyet in suanki_konum.komsular.items():
                yeni_maliyet = maliyetler[suanki_konum] + maliyet
                if yeni_maliyet < maliyetler[komsu]:
                    maliyetler[komsu] = yeni_maliyet
                    oncekiler[komsu] = suanki_konum  # Yolu kaydet
            
            islenmemis.remove(suanki_konum)  # İşlendi olarak işaretle
        
        # Hedefe giden yolu geri oluştur
        yol = []
        suanki = hedef_konum
        while suanki != baslangic_konum:
            yol.insert(0, suanki.isim)
            if suanki not in oncekiler:  # Yol bulunamadı
                return None, float('inf')
            suanki = oncekiler[suanki]
        yol.insert(0, baslangic_konum.isim)  # Başlangıcı ekle
        
        return yol, maliyetler[hedef_konum]

class BFS(RotaStratejisi):
    """Genişlik Öncelikli Arama: En az aktarmalı yol"""
    def rota_hesapla(self, harita, baslangic, hedef):
        baslangic_konum = harita.konumlar[baslangic]
        hedef_konum = harita.konumlar[hedef]
        
        # BFS için kuyruk ve ziyaret edilenler seti
        kuyruk = deque()
        kuyruk.append((baslangic_konum, [baslangic_konum.isim]))
        ziyaret_edilen = set()
        
        while kuyruk:
            suanki_konum, yol = kuyruk.popleft()
            
            if suanki_konum == hedef_konum:
                # Aktarma sayısı = düğüm sayısı - 1
                return yol, len(yol)-1
            
            if suanki_konum in ziyaret_edilen:
                continue
            ziyaret_edilen.add(suanki_konum)
            
            # Tüm komşuları kuyruğa ekle
            for komsu in suanki_konum.komsular:
                if komsu not in ziyaret_edilen:
                    yeni_yol = yol + [komsu.isim]
                    kuyruk.append((komsu, yeni_yol))
        
        return None, float('inf')  # Yol bulunamadı

# Test senaryosu ve örnek kullanım
if __name__ == "__main__":
    # Gerçekçi koordinatlar (yaklaşık)
    harita = Harita()
    harita.konum_ekle(Konum("Istanbul", x=-20, y=60))
    harita.konum_ekle(Konum("Ankara", x=50, y=50))
    harita.konum_ekle(Konum("Izmir", x=-30, y=-30))
    harita.konum_ekle(Konum("Antalya", x=20, y=-40))
    harita.konum_ekle(Konum("Bursa", x=10, y=20))
    harita.konum_ekle(Konum("Konya", x=30, y=0))
    harita.konum_ekle(Konum("Adana", x=80, y=-20))
    harita.konum_ekle(Konum("Trabzon", x=100, y=70))
    
    # Bağlantıları ve maliyetleri ekle
    harita.baglanti_ekle("Istanbul", "Ankara", 450)    # Istanbul-Ankara arası maliyet
    harita.baglanti_ekle("Istanbul", "Bursa", 150)     # Istanbul-Bursa arası maliyet  
    harita.baglanti_ekle("Istanbul", "Izmir", 480)     # Istanbul-Izmir arası maliyet
    harita.baglanti_ekle("Ankara", "Konya", 260)       # Ankara-Konya arası maliyet
    harita.baglanti_ekle("Ankara", "Trabzon", 780)     # Ankara-Trabzon arası maliyet
    harita.baglanti_ekle("Izmir", "Antalya", 420)      # Izmir-Antalya arası maliyet
    harita.baglanti_ekle("Antalya", "Konya", 320)      # Antalya-Konya arası maliyet
    harita.baglanti_ekle("Konya", "Adana", 340)        # Konya-Adana arası maliyet
    harita.baglanti_ekle("Bursa", "Ankara", 380)       # Bursa-Ankara arası maliyet
    harita.baglanti_ekle("Bursa", "Izmir", 330)        # Bursa-Izmir arası maliyet
    harita.baglanti_ekle("Adana", "Trabzon", 890)      # Adana-Trabzon arası maliyet
    

    # Dijkstra testi (En düşük maliyet)
    harita.set_strateji(Dijkstra())
    yol, maliyet = harita.rota_bul("Istanbul", "Trabzon")
    print(f"Dijkstra ile en kısa yol: {yol}, Toplam maliyet: {maliyet}")
    
    # BFS testi (En az aktarma)
    harita.set_strateji(BFS())
    yol, aktarma = harita.rota_bul("Istanbul", "Trabzon")
    print(f"BFS ile en az aktarmalı yol: {yol}, Aktarma sayısı: {aktarma}")

    # Görselleştirme
    harita.visualize()