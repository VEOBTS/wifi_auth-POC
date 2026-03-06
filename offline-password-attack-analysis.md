# WPA2 Handshake Capture and Analysis 

In this section of the project, the focus on capturing and analyzing Wi‑Fi
authentication traffic in order to understand how WPA2‑Personal networks
authenticate devices. 

# Key Concept: WPA2‑Personal Authentication

WPA2‑Personal networks use a Pre‑Shared Key (PSK) for authentication.
Instead of transmitting the password directly across the network, the
password is processed using a key derivation function (KDF) to generate a
stronger cryptographic key. IN WPA2 this derivation function is PKBDF2 (Password Based Key Derivation Function 2) using HMAC-SHA-1 AS its core algorithm ..The passphrase is converted into a Pairwise Master Key (PMK) using:

PBKDF2‑HMAC‑SHA1
4096 iterations

Conceptually:
PMK = PBKDF2(passphrase, SSID, 4096) 
The passprase is combined with the SSID of the network which is used as the salt, and the algorithm performs 4096 iterations (**amount of times it runs**) to derive a 256-bit key.

Reference\
https://www.rfc-editor.org/rfc/rfc2898

# The Role of the 4‑Way Handshake

When a device connects to a Wi‑Fi network, the router (Access Point) and
the client perform a 4‑Way Handshake.

The handshake confirms that both devices know the correct password and
derives temporary encryption keys.

The handshake exchanges:

• ANonce -- random value from the Access Point\
• SNonce -- random value from the client\
• MIC -- Message Integrity Code\
• MAC addresses of both devices

These values allow both sides to generate the Pairwise Transient Key
(PTK) used to encrypt traffic. as earlier mentioned in [wpa2_handshake_analysis](wpa2_handshake_analysis.md)

Reference\
https://www.rfc-editor.org/rfc/rfc5246

# Lab Environment Setup

To safely study Wi‑Fi authentication, you can create a small wireless lab.
Components:

Router / Access Point\
Client device\
Packet capture software\
Analysis tools

Example setup:
Laptop running Linux to use tools 
USB Wi‑Fi adapter supporting monitor mode\
Local router configured with WPA2

This ensures all testing happens on a network I control.

alternatively you can run a setup using laptop(client+capture) and phone(WPA2 hotspot)

# Capturing Authentication Packets

The next step is capturing authentication packets exchanged during
connection.

Packet captures are stored in PCAP format. 
PCAP files store raw network packets exactly as they appear on the
network.

These files can later be analyzed using packet inspection tools.
Common tools:
Wireshark\
tcpdump\
Aircrack‑ng

Documentation\
https://www.wireshark.org/docs/

# Basic Capture Workflow

General workflow

1.  Start packet capture on the wireless interface using wireshark or tcpdump 
2.  Connect a client device to the Wi‑Fi network (e.g laptop to hotspot)
3.  Observe and filter out only authentication traffic (wireshark provides a GUI for easy interaction/filtering)
4.  Save packets as a PCAP file (.pcap)
5.  Filter the capture for handshake frames such as EAPOL key frames

**These key frames contain the messages exchanged during the WPA2 4-Way Handshake. These frames carry important authentication data including nonce**

Typical Wireshark filters focus on:
• EAPOL frames\
• authentication frames\
• association frames

# Understanding the PCAP File

A PCAP file contains:

Packet header\
Timestamp\
Packet length\
Raw packet data

Within the packet payload we can observe:

EAPOL frames\
Nonce values\
Integrity codes

Reference\
![IMAGE](https://ostinato.org/images/guides/rarp-wireshark.png)
https://www.tcpdump.org/manpages/pcap.3pcap.html

# Parsing PCAP Files Programmatically
Instead of only viewing packets visually, I can analyze them
programmatically.

A small Python tool as later demonstrated will:

• load PCAP files\
• identify handshake packets\
• extract useful metadata and display results for analysis 

Python libraries to be used in development include:
Scapy\
PyShark

Documentation\
-https://scapy.net/ 
-https://pypi.org/project/pyshark/

# Conceptual Password Verification
Once handshake data exists, researchers can demonstrate how password
verification works.

Conceptually:
1.  Take a candidate password
2.  Generate PMK using PBKDF2
3.  Derive PTK using handshake values
4.  Compare calculated MIC with captured MIC
