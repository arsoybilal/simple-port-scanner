import socket
from datetime import datetime

def port_scanner(target_host, ports):
    print("-" * 50)
    print(f"Hedef taranıyor: {target_host}")
    print(f"Tarama başlangıcı: {datetime.now()}")
    print("-" * 50)

    acik_port = 0

    try:
        for port in ports:
    
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) 
            
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: AÇIK")   
                acik_port+=1
            s.close()
        print("-" * 50)    
        print(f"Tarama Tamamlandı!")
        print(f"Taranan port sayısı : {len(target_ports)}")
        print(f"Açık port sayisi : {acik_port}")  
        print("-" * 50)

    except KeyboardInterrupt:
        print("\nKullanıcı tarafından durduruldu.")
    except socket.gaierror:
        print("\nHostname çözülemedi.")
    except socket.error:
        print("\nSunucuya bağlanılamadı.")


target =input("Hedef adresi giriniz :")                          #"scanme.nmap.org" 
user_input = input("Hedef port veya portları (arasında virgül olacak şekilde) giriniz: ")
target_ports = [int(p.strip()) for p in user_input.split(",")]
 #[21, 22, 80, 443, 8080]
port_scanner(target, target_ports)