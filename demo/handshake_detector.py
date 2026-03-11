import argparse
from scapy.all import sniff
from scapy.layers.dot11 import Dot11
from scapy.layers.eap import EAPOL


def got_packet(pkt):
    if pkt.haslayer(EAPOL) and pkt.haslayer(Dot11):
        src = pkt[Dot11].addr2
        dst = pkt[Dot11].addr1
        bssid = pkt[Dot11].addr3
        print(f"[+] EAPOL | {src} -> {dst} | BSSID: {bssid}")


def main():
    parser = argparse.ArgumentParser(description="WPA2 Handshake Detector")
    parser.add_argument("-i", "--interface", required=True, help="Monitor mode interface (e.g. wlan0mon)")
    iface = parser.parse_args().interface

    print(f"[*] Sniffing on {iface} — CTRL+C to stop\n")

    try:
        sniff(iface=iface, prn=got_packet, store=False)
    except KeyboardInterrupt:
        print("\n[!] Stopped.")


if __name__ == "__main__":
    main()