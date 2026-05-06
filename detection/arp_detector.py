from scapy.all import sniff, ARP
import time

arp_table = {}

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        src_ip = packet[ARP].psrc
        src_mac = packet[ARP].hwsrc
        if src_ip in arp_table:
            if arp_table[src_ip] != src_mac:
                print(f"[!] ARP SPOOFING DETECTED at {time.strftime('%H:%M:%S')}")
                print(f"    IP:       {src_ip}")
                print(f"    Real MAC: {arp_table[src_ip]}")
                print(f"    Fake MAC: {src_mac}")
        else:
            arp_table[src_ip] = src_mac
            print(f"[+] Learned: {src_ip} -> {src_mac}")

print("[*] ARP Spoof Detector running...")
sniff(filter="arp", prn=detect_arp_spoof, store=0)
