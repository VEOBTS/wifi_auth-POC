# Wi-Fi Authentication Security Research

*This project is currently in development.* It serves as a comprehensive exploration of Wi-Fi authentication principles, focusing on the cryptographic mechanisms devices use to establish secure connections with Access Points (APs). The objective is to conceptually demonstrate the evolution of wireless security protocols, emphasizing the transition from legacy standards to modern protections.

## Conceptual Overview

The repository is structured to analyze and document key authentication paradigms in wireless networks. It provides theoretical frameworks and practical scenarios detailing how authentication data is securely exchanged, identifying vulnerabilities in legacy protocols, and exploring the mitigations introduced in newer standards.

### WPA2 Security and Vulnerabilities

WPA2 relies on a four-step cryptographic exchange to establish a secure session. This process, while robust for its time, relies heavily on the strength of the shared password and is susceptible to specific offline attacks if the exchange is intercepted.
- [WPA2 4-Way Handshake Analysis](scenarios/wpa2-handshake-analysis.md): A detailed breakdown of the four-step key negotiation process used in WPA2.
- [Offline Password Attack Analysis](scenarios/offline-password-attack-analysis.md): An exploration of how captured WPA2 handshakes can be subjected to offline dictionary attacks.
- [Sample Handshake Capture](pcaps/sample-handshake.md): An example packet capture (PCAP) demonstrating a real-world WPA2 handshake.

### WPA3 and Advanced Authentication

WPA3 introduces forward secrecy and robust protections against offline guessing attacks through a more complex, interactive authentication process known as Simultaneous Authentication of Equals (SAE).
- [WPA3 and SAE Authentication](scenarios/wpa3-sae-authentication.md): An overview of the Simultaneous Authentication of Equals (SAE) protocol, which replaces the WPA2 Pre-Shared Key (PSK) mechanism.
- [Dragonfly Handshake and Security Summary](scenarios/dragonfly-attack-research.md): An analysis of the Dragonfly cryptographic handshake underpinning SAE and its resilience against offline attacks.

## Proof of Concept (PoC)

To bridge theory and practice, the project includes a functional Proof-of-Concept for detecting wireless authentication events in real-time.
- [WPA2 Handshake Detector (PoC)](demo/readme.md): A practical implementation designed to monitor network traffic and detect the WPA2 4-Way Handshake dynamically.
