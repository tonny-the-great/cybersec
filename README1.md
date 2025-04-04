# CyberSec Labs: WiFi & Web Vulnerability Scripts
⚠️ DISCLAIMER: THIS IS FOR EDUCATIONAL PURPOSES ONLY!!!
A collection of tools and scripts demonstrating common WiFi and web-based attack vectors.

## 🔧 Tools Included

- **WiFi AP Scanner** (`wifi_ap_scanner.sh`): Scans for available WiFi Access Points on the local network.
- **LAN Device Enumerator** (`lan_device_enumerator.py`): Identifies devices on your local network by scanning for open ports (e.g., HTTP).
- **Web Path Fuzzer** (`web_fuzzer.py`): A basic script for fuzzing common web paths to discover hidden endpoints.

## 🚀 How to Run

### Prerequisites

- Python 3.x (for Python scripts)
- Linux/MacOS environment (for bash scripts)
- Scapy installed (`pip install scapy` for sniffing)

### Running Scripts

#### WiFi AP Scanner

To scan for WiFi access points:

```bash
chmod +x wifi_tools/wifi_ap_scanner.sh
./wifi_tools/wifi_ap_scanner.sh
