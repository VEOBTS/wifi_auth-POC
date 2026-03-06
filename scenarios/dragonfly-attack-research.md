# Dragonfly Handshake and Security Summary

The Dragonfly handshake (also known as SAE) is the security method used in WPA3 Wi-Fi to keep connections safe. It ensures that your password is never sent over the air.

## How it Works
### The Commit Phase: The device and router use the password to agree on a starting point on a mathematical curve. They swap random numbers to create a secret key.

### The Confirm Phase: Both sides check their math. If they match, it proves they both have the correct password. This creates a unique key for that specific session.

## Why it is Secure
Dragonfly provides Forward Secrecy. This means every time you connect, a brand new key is made. If a hacker steals your password later, they still cannot unlock old data you sent in the past.

## Dragonfly Attacks (Dragonblood)
Researchers found some weaknesses in this system called **Dragonblood attacks.** these attacks include :
*Side-Channel Attacks*: A hacker can watch how long a device takes to do the math. These tiny time differences help them guess the password, When the Dragonfly handshake maps a password to a point on an elliptic curve, it uses an iterative loop. The number of iterations or the time taken to find a valid point depends directly on the password string and the specific coordinates on the curve. an attacker using sophisticated means can analyze the whole process from beginning to end and make mathematical deductions based of his inceptions.

Downgrade Attacks: A hacker tricks a device into using an older, weaker security method like WPA2 to make it easier to break.In a WPA3 environment, a downgrade attack occurs when an adversary exploits the transition mode designed for compatibility with older devices. Since many networks allow both WPA2 and WPA3 connections simultaneously, a hacker can interfere with the initial handshake by sending forged management frames that trick your device into believing the router only supports the weaker WPA2 standard.

Resource Attacks: A hacker floods the router with fake requests, making it too busy to let real users connect.leverages the high computational cost of the Dragonfly handshake to overwhelm the network. Because the router must perform complex elliptic curve mathematics to process every commit request, a hacker can flood the Access Point with a massive volume of fake handshake starts.  Since the router consumes significant CPU power trying to solve the math for each "user," it quickly runs out of processing resources and becomes unable to handle legitimate connection attempts from real devices.