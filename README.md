# Wi-Fi Authentication Research

This project explores Wi-Fi authentication principles, focusing on how devices authenticate with an Access Point (AP), the progression of security standards from WPA2 to WPA3, and the practical analysis of network traffic.

## Project Structure & Documentation

This repository is structured to guide you from foundational concepts of Wi-Fi authentication to practical demonstrations. The documentation is split across several Markdown files, logically building upon each other.

### 1. WPA2 Concepts and Limitations
* **[WPA2 Handshake Analysis](scenarios/wpa2-handshake-analysis.md)**: Explains the fundamental concepts of WPA2-Personal networks, specifically focusing on the 4-Way Handshake. It details how devices authenticate using a Pre-Shared Key (PSK) and how encryption keys (PTK, GTK) are generated without transmitting the actual password over the air.
* **[Offline Password Attack Analysis](scenarios/offline-password-attack-analysis.md)**: Builds upon the 4-Way Handshake analysis by exploring its primary vulnerability. It explains how capturing the 4-Way Handshake packets allows attackers to perform offline dictionary attacks to guess the PSK, detailing the lab setup and packet capture workflow needed to demonstrate this conceptual weakness.

### 2. The WPA3 Evolution
* **[WPA3 and SAE Authentication](scenarios/wpa3-sae-authentication.md)**: Introduces WPA3 as the solution to WPA2's offline dictionary attack vulnerabilities. It details Simultaneous Authentication of Equals (SAE) and the Dragonfly key exchange, explaining how Password Authenticated Key Exchange (PAKE) proves knowledge of a password without transmitting hash values that can be cracked offline, while also introducing Forward Secrecy.
* **[Dragonfly Attack Research](scenarios/dragonfly-attack-research.md)**: While WPA3 is highly secure, this document explores known theoretical and practical vulnerabilities in the SAE/Dragonfly handshake, specifically "Dragonblood" attacks, including side-channel, downgrade, and resource exhaustion attacks.

### 3. Practical Demonstrations
The conceptual learning is backed by practical, code-based demonstrations.
* **[WPA2 Handshake Detector Demo](demo/readme.md)**: Contains instructions for a Python-based tool (`handshake_detector.py`) that listens on a wireless interface to detect and analyze WPA2 handshake (EAPOL) frames in real-time.
* **[Sample PCAP File](pcaps/sample-handshake.md)**: Provides a reference to a captured `.pcap` file containing a sample WPA2 4-Way Handshake, which can be used for analysis without needing a live wireless monitor mode setup.

## Conceptual Journey
The project is designed to be read sequentially:
1. Understand how WPA2 secures connections (the 4-Way Handshake).
2. Understand the fundamental flaw in WPA2 (offline dictionary attacks via captured handshakes).
3. Learn how WPA3 addresses this flaw using SAE (Dragonfly).
4. Analyze the complexities and new attack surfaces introduced by WPA3.
5. Practically demonstrate WPA2 handshake capture and detection using provided scripts and packet captures.
