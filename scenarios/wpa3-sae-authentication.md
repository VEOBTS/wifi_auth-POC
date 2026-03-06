# WPA3 and SAE Authentication

## Introduction

Wireless network security has evolved significantly over the years. Earlier protocols such as WEP and WPA had serious cryptographic weaknesses, which led to the development of WPA2. While WPA2 improved wireless security, it still relied on the **Pre-Shared Key (PSK)** mechanism which allowed certain attacks such as **offline dictionary attacks** once the 4-way handshake was captured.

To address these weaknesses, **WPA3** was introduced by the Wi-Fi Alliance. WPA3 improves wireless authentication and encryption by replacing the traditional PSK authentication process with **Simultaneous Authentication of Equals (SAE)**, a secure password-authenticated key exchange protocol.

This write-up explains how WPA3 works, the concepts behind SAE authentication, and how packet analysis can be performed in a controlled lab environment.

# WPA3 Overview

WPA3 is the latest Wi-Fi security standard designed to provide stronger protection for wireless networks.

Key improvements introduced by WPA3 include:
- Protection against **offline password cracking attacks**
- **Forward secrecy** for session keys **forward Secrecy ensures that if a server's long-term private key is stolen, all past intercepted traffic remains unreadable**
- Stronger cryptographic algorithms
- Improved security for public networks
- Optional **192-bit security suite** ,for enterprise deployments which requires AES-256 Encryption,ECDHE Key exchange as well as other sophisticated protocols with hashing and certificates

WPA3 operates in two primary modes:

- **WPA3-Personal**
- **WPA3-Enterprise**


# WPA3 Personal

WPA3-Personal replaces the WPA2 **Pre-Shared Key (PSK)** authentication with **SAE (Simultaneous Authentication of Equals)**.
In WPA2, an attacker who captures the **4-way handshake** can attempt to crack the password offline using dictionary attacks.

WPA3 solves this problem by using a **Password Authenticated Key Exchange (PAKE)** protocol. This means that even if authentication packets are captured, they **cannot be used for offline password guessing**. With PAKE, you never actually send the password itself. Instead, both sides do some math with the password and exchange those results.This math proves you both know the same password without ever showing it to each other or to anyone watching the connection.

# WPA3 Enterprise

WPA3-Enterprise is designed for **organizational and enterprise networks** that require stronger authentication mechanisms.

It uses **802.1X authentication with a RADIUS server**, similar to WPA2-Enterprise, but introduces an optional **192-bit cryptographic security suite**.
A RADIUS server is a central manager that handles user access for a network. When you try to connect to a VPN or office Wi-Fi, the router asks the RADIUS server if your username and password are correct.

## 192-bit Security Suite

The 192-bit mode provides stronger protection for highly sensitive environments such as government networks and military systems 
This mode enforces stronger cryptographic algorithms and key sizes aligned with modern security standards.

# Simultaneous Authentication of Equals (SAE)
SAE is the core authentication mechanism used in **WPA3-Personal**.

It is based on the **Dragonfly key exchange protocol**, which allows two devices to authenticate each other using a shared password without ever transmitting that password over the network.

The two primary parties involved are:

- **Client (Station / STA)**
- **Access Point (AP)**

Both devices prove knowledge of the password through a cryptographic exchange rather than sending the password directly.
## Dragonfly 
The Dragonfly handshake is the mathematical engine behind WPA3 security. It works in two main phases.

First, both your device and the router use the password to agree on a secret "starting point" on a mathematical curve. This part is called the Commit phase. They each pick a random number, mix it with the password point, and swap the results. 

Second, in the Confirm phase, both sides use the data they just exchanged to run a final calculation. If both sides have the same password, their math results will match perfectly. This creates a unique, temporary session key that is only good for that one connection.

# SAE Handshake Process

The SAE authentication process consists primarily of two phases:

1. **Commit Phase**
2. **Confirm Phase**

### Commit Phase

During this phase:

- Both the client and access point generate **temporary cryptographic values**. based of the concept explained earlier 
- These values are derived from the password and random numbers.
- Each device sends an **SAE Commit message** containing these values.

This establishes the basis for a shared secret.

### Confirm Phase

In the confirm phase:

- Both parties verify that they derived the same secret.
- Each side sends an **SAE Confirm message**.

If verification succeeds, authentication is successful and a secure session can begin.


# Forward Secrecy

One of the most important security improvements introduced by WPA3 is **forward secrecy**.
Forward secrecy means that:

> Even if the network password is discovered later, previously captured traffic cannot be decrypted.
Each session uses **fresh cryptographic keys**, preventing attackers from decrypting older communications.
