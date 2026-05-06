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
[screenshot: poisoned ARP table]
[screenshot: fake login page on victim]
[screenshot: captured credentials]

## Detection
Real-time ARP spoof detector built with Scapy. Fires an alert 
within seconds of poisoning onset, showing the legitimate vs 
fake MAC address mapping.

[screenshot: detector alert]

## Mitigations Implemented
| Mitigation | Effective? | Evidence |
|---|---|---|
| Static ARP entry | Yes | [screenshot] |

## Tools Used
- Kali Linux (UTM, Apple Silicon)
- Ettercap — ARP poisoning
- dnsmasq — DNS spoofing
- Apache2 + PHP — fake credential harvesting site
- Scapy — ARP spoof detection
- Wireshark — packet capture

## Environment
3 Kali Linux VMs on an isolated Host-Only network via UTM
