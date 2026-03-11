# WPA2 Handshake Detector

A simple Python tool that listens on a wireless interface and detects **WPA2 handshake (EAPOL) frames**.

> When a device connects to a WPA2 network, the router and client exchange special packets called **EAPOL frames**.  
> These packets form the **4-way handshake** used to establish encryption keys.
for more information refer [here](wpa2-handshake-analysis)

# Requirements
- Python 3
- Linux system (Kali, Parrot, Ubuntu, etc.)
- Wireless adapter(external/internal) usually in monitor mode 

# Install Dependencies

```bash
# install libpcap (required for packet capture)
sudo apt install libpcap-dev

# install python packages
pip install -r requirements.txt

```
*to view network interface on device iwconfig and look for something like wlan0/wlan1....*
*sample use case> sudo python3 handshake_detector.py -i wlan0mon*