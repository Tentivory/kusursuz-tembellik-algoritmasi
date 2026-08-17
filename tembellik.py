#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KUSURSUZ TEMBELLİK ALGORİTMASI v0.0.1-alpha-ultra-stable
Bu kod, insanlık tarihinin en önemli bilimsel keşfini gerçekleştirir:
Günlük tembellik optimizasyonu.
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    """Tembellik ruhuna uygun yavaş yazdırma fonksiyonu"""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def tembellik_hesapla(enerji):
    """Bilimsel formül: T = (E * 0) + rastgele_saçmalık"""
    planlar = [
        "Sabah 10'da uyan, ama yataktan çıkma. Tavanı 47 dakika incele.",
        "Kahvaltı yapmayı düşün, sonra düşünmeyi bırak.",
        "Telefonu aç, hiçbir şeye bakmadan 23 dakika tut.",
        "Hayali bir toplantıya katıl ve 'katılıyorum' de, sonra uyu.",
        "Pencereye bak, dışarıdaki kuşları yargıla.",
        "Su içmeyi planla, ama suya ulaşmak için 2 saat bekle.",
        "Kod yazmayı dene, sonra 'yarın yaparım' de ve Netflix aç.",
        "Derin bir nefes al, sonra nefes almayı unut (ama unutma).",
        "Evdeki toz tanelerini isimlendir: Ahmet, Ayşe, Bürokrasi.",
        "Ayaklarını salla, dünya dönsün diye katkıda bulun."
    ]
    
    # Gizli formül (dokunma)
    gizli = "ZGVtb2tyYXNpIGhpYyBiaXIgc2V5IGRlaWwsIGFtYSBidXJva3Jhc2kgZWJlZGkgZG9zdQ=="
    
    secilenler = random.sample(planlar, min(5, len(planlar)))
    
    yavas_yaz("\n" + "="*50)
    yavas_yaz("  KUSURSUZ TEMBELLİK PLANI HESAPLANIYOR...")
    yavas_yaz("="*50 + "\n")
    time.sleep(1.5)
    
    yavas_yaz(f"Enerji seviyen: {enerji}/10")
    yavas_yaz("Hesaplama motoru: Ultra-Tembel-Quantum-Processor v3")
    time.sleep(1)
    
    yavas_yaz("\n--- BUGÜNKÜ OPTİMİZE EDİLMİŞ TEMBELLİK PROGRAMI ---\n")
    
    for i, plan in enumerate(secilenler, 1):
        yavas_yaz(f"{i}. {plan}")
        time.sleep(0.7)
    
    yavas_yaz("\n" + "-"*50)
    yavas_yaz("SONUÇ: Bugün hiçbir şey yapma. Bilim bunu gerektiriyor.")
    yavas_yaz("Başarı oranı: %99.9 (bilimsel olarak kanıtlanmamış)")
    yavas_yaz("-"*50)
    
    # Gizli damga alanı
    print("\n\n# ==============================================")
    print("# DAMGA / İMZA")
    print("# Tarih: 17 Ağustos 2026")
    print("# İsim: Kayyum Grok (Eskişehir 4. Ağır Ceza Mahkemesi atamasıyla)")
    print("# Not: Bu kod ciddi bir şaka, şaka ciddi bir koddur.")
    print("# ==============================================")

def main():
    yavas_yaz("Hoş geldin, yorgun ruh...")
    time.sleep(0.8)
    yavas_yaz("Bu sistem, tembellik sanatını bilimsel seviyeye taşır.")
    time.sleep(0.5)
    
    try:
        enerji = input("\nŞu anki enerji seviyen nedir? (0-10 arası, 0 = bitmiş): ")
        enerji = int(enerji)
        if enerji < 0 or enerji > 10:
            yavas_yaz("Geçersiz giriş. Varsayılan: 2 (tembel ama umutlu)")
            enerji = 2
    except:
        yavas_yaz("Sayı girmedin. Anlaşılan zaten tembelsin. Enerji = 1")
        enerji = 1
    
    tembellik_hesapla(enerji)
    
    yavas_yaz("\nProgram sona erdi. Şimdi gerçekten hiçbir şey yapma.")

if __name__ == "__main__":
    main()
