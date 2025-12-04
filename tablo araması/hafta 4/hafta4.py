import re
import datetime
import os

LOG_DOSYASI = "ipTables.log"

def ip_vurgula(satir, ip_adresi):
    """Bulunan IP adresini HTML ile sarı arka plan ve kırmızı metinle vurgular."""
    pattern = re.escape(ip_adresi)
    vurgulanan_ip = f"<span style='background-color: yellow; color: red;'>{ip_adresi}</span>"
    
    return re.sub(r'\b' + pattern + r'\b', vurgulanan_ip, satir)

def ip_arama_motoru():
    """Kullanıcıdan alınan IP ve arama kipine göre log dosyasını tarar ve her seferinde yeni bir HTML çıktısı üretir."""
    
    if not os.path.exists(LOG_DOSYASI):
        print(f"\nFATAL HATA: '{LOG_DOSYASI}' dosyası bulunamadı.")
        print(f"Lütfen dosyanın, Python kodunun çalıştığı dizinde olduğundan emin olun.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    HTML_DOSYASI = f"ip_arama_sonuclari_{timestamp}.html"
    
    while True:
        ip_adresi = input("Lütfen aranacak IP adresini giriniz (Örn: 192.168.2.89): ").strip() 
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_adresi):
            break
        else:
            print("Hata: Geçerli bir IP adresi formatı giriniz.")

    while True:
        arama_kipi = input("Arama kipi seçiniz (source/destination/any): ").lower().strip() 
        if arama_kipi in ['source', 'destination', 'any']:
            break
        else:
            print("Hata: Lütfen geçerli bir arama kipi giriniz (source, destination, any).")
            
    eslesen_satirlar = []

    try:
        with open(LOG_DOSYASI, 'r', encoding='utf-8') as log_file: 
            print(f"'{LOG_DOSYASI}' dosyası okunuyor...")
            
            for satir in log_file:
                if not ("SRC=" in satir and "DST=" in satir):
                    continue

                eslesti = False
                
                src_match = re.search(r'SRC=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', satir)
                dst_match = re.search(r'DST=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', satir)
                
                if src_match and dst_match:
                    src_ip = src_match.group(1)
                    dst_ip = dst_match.group(1)
                    
                    if arama_kipi == 'source' and src_ip == ip_adresi: 
                        eslesti = True
                    elif arama_kipi == 'destination' and dst_ip == ip_adresi:
                        eslesti = True
                    elif arama_kipi == 'herhangi biri': 
                        if src_ip == ip_adresi or dst_ip == ip_adresi:
                            eslesti = True

                if eslesti:
                    vurgulanan_satir = ip_vurgula(satir, ip_adresi)
                    eslesen_satirlar.append(vurgulanan_satir)

    except Exception as e:
        print(f"\nDosya okuma sırasında beklenmeyen bir hata oluştu: {e}") 
        return

    try:
        with open(HTML_DOSYASI, 'w', encoding='utf-8') as html_file:
            html_file.write("<!DOCTYPE html>\n")
            html_file.write("<html lang='tr'>\n")
            html_file.write("<head>\n")
            html_file.write(f"<meta charset='UTF-8'>\n")
            html_file.write(f"<title>IP Arama Sonuçları: {ip_adresi} (Kip: {arama_kipi})</title>\n")
            html_file.write("</head>\n")
            html_file.write("<body>\n")
            html_file.write(f"<h1>Aranan IP: {ip_adresi} (Kip: {arama_kipi})</h1>\n")
            html_file.write(f"<h2>Toplam {len(eslesen_satirlar)} sonuç bulundu.</h2>\n")
            
            if eslesen_satirlar:
                html_file.write("<pre>\n") 
                for satir in eslesen_satirlar:
                    html_file.write(satir)
                html_file.write("</pre>\n")
            else:
                html_file.write("<p>Belirtilen IP adresine ve kibe uygun sonuç bulunamadı.</p>\n")
                
            html_file.write("</body>\n")
            html_file.write("</html>\n")

        print(f"\nİşlem tamamlandı. Sonuçlar yeni oluşturulan '{HTML_DOSYASI}' dosyasına yazıldı.")
    except IOError:
        print(f"\nHata: '{HTML_DOSYASI}' dosyasına yazılırken bir I/O hatası oluştu.") 
    except Exception as e:
        print(f"\nHTML yazma sırasında beklenmeyen bir hata oluştu: {e}") 

if __name__ == "__main__":
    ip_arama_motoru()