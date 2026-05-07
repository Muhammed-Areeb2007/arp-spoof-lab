# ARP Spoofing Attack Demo + Mitigation Lab

## Overview
Demonstrates a complete ARP cache poisoning → DNS spoofing → 
credential harvesting attack chain in an isolated 3-VM lab, 
followed by implementation and verification of mitigations.

## Lab Architecture
| VM | OS | Role | IP |
|---|---|---|---|
| Attacker | Kali Linux | Runs Ettercap, fake site | 192.168.56.10 |
| Victim | Kali Linux | Target | 192.168.56.20 |
| Gateway | Kali Linux | Simulates router | 192.168.56.1 |

## Attack Chain
1. ARP cache poisoning via Ettercap positions attacker as MitM
2. DNS queries intercepted and redirected via dnsmasq
3. Victim redirected to attacker-hosted fake login page
4. Credentials harvested from form submission

## Results

<img width="700" alt="poisoned_arp_table" src="https://github.com/user-attachments/assets/d82ac189-e2b2-41af-9597-3dd5c459f1dc" />
<br><br>
<img width="700" alt="fake_login_page" src="https://github.com/user-attachments/assets/34f0fc6f-b980-4764-85c0-318e2fbdc770" />
<br><br>
<img width="700" alt="captured_credentials" src="https://github.com/user-attachments/assets/445f4647-01fc-403e-8a5c-fa17e5ce208d" />

## Detection
Real-time ARP spoof detector built with Scapy. Fires an alert 
within seconds of poisoning onset, showing the legitimate vs 
fake MAC address mapping.

<img width="464" height="173" alt="arp_detection" src="https://github.com/user-attachments/assets/bf1f505c-929b-487a-b23b-c4fa0412a076" />


## Mitigations Implemented
| Mitigation | Effective? | Evidence |
|---|---|---|
| Static ARP entry | Yes | <img width="1439" height="528" alt="mitigation_static_arp" src="https://github.com/user-attachments/assets/4d56b711-367b-4596-ae15-3f0425096320" />
|

## Tools Used
- Kali Linux (UTM, Apple Silicon)
- Ettercap: ARP poisoning
- dnsmasq: DNS spoofing
- Apache2 + PHP: fake credential harvesting site
- Scapy: ARP spoof detection
- Wireshark: packet capture

## Environment
3 Kali Linux VMs on an isolated Host-Only network via UTM
