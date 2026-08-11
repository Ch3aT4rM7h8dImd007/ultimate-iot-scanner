# 🌐 Ultimate IoT Device Scanner v6.0

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)](https://kali.org)
[![Version](https://img.shields.io/badge/version-6.0.0-brightgreen)]()

> **Complete IoT, Camera, Printer, Router & Network Device Scanner with Auto-Save & Live Output**

---

## 📖 What is Ultimate IoT Device Scanner?

**Ultimate IoT Device Scanner v6.0** is a comprehensive network reconnaissance tool designed to detect, identify, and catalog a wide range of Internet of Things (IoT) devices, including:

- 📷 **Cameras** - Axis, Hikvision, Dahua, TP-Link, D-Link, Foscam, Vivotek, Panasonic, Sony, Bosch, Pelco, Samsung, LG, GeoVision, ACTi, Arecont, AVTECH, Brunof, Canon
- 🖨️ **Printers** - HP, Brother, Epson, Canon, Lexmark, Samsung, Xerox, Ricoh, Kyocera, Dell
- 📡 **Routers** - MikroTik, Cisco, Huawei, ZTE, Netgear, ASUS, TP-Link, D-Link
- 🤖 **IoT Devices** - Raspberry Pi, Arduino, ESP32, webcamXP, Webcam7, Yawcam
- 💾 **NAS Devices** - Synology, QNAP, Asustor, Buffalo
- 🏠 **Smart Home** - Philips Hue, Google Home, Amazon Echo, Xiaomi, Yeelight
- 🔐 **Security** - Doorbells, Alarm Systems
- 🏭 **Industrial** - Modbus, BACnet, SCADA, Siemens
- 🏥 **Medical** - DICOM, PACS devices
- 📺 **Smart TVs** - Samsung, LG, Sony

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone [https://github.com/yourusername/ultimate-iot-scanner.git](https://github.com/yourusername/ultimate-iot-scanner.git)
cd ultimate-iot-scanner

# Make executable
chmod +x iot_scanner.py

# Run the scanner
python3 iot_scanner.py

# Or run directly
python3 ultimate_device_scanner.py
```

---

## 📚 Table of Contents

- [What is Ultimate IoT Device Scanner?](#-what-is-ultimate-iot-device-scanner)
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Installation](#-installation)
- [Device Database](#-device-database)
- [Usage Guide](#-usage-guide)
- [Scan Methods](#-scan-methods)
- [How It Works](#-how-it-works)
- [Output & Reports](#-output--reports)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Security Tips](#-security-tips)
- [License](#-license)

---

## 🌟 Features

### Core Capabilities

- **✅ 100+ Device Types** - Comprehensive database of IoT devices
- **✅ Live Terminal Output** - Real-time progress with color coding
- **✅ Auto-Save Every 5 IPs** - Never lose scan progress
- **✅ Master Report System** - Append new findings to existing data
- **✅ Multiple Scan Methods** - IP range, CIDR, Google Dorks, Masscan
- **✅ Port Scanning** - Identifies open ports on devices
- **✅ Banner Grabbing** - Collects service banners
- **✅ Path Discovery** - Finds web interfaces and APIs
- **✅ Default Credential Check** - Tests common default credentials
- **✅ Device Type Detection** - Automatic classification
- **✅ CTRL+C Support** - Graceful interruption with partial save

### Device Support

| Category | Count | Examples |
|----------|-------|----------|
| **Cameras** | 18 | Axis, Hikvision, Dahua, TP-Link, D-Link |
| **Printers** | 9 | HP, Brother, Epson, Canon, Lexmark |
| **Routers** | 8 | MikroTik, Cisco, Huawei, Netgear |
| **IoT Devices** | 5 | Raspberry Pi, Arduino, ESP32 |
| **NAS** | 4 | Synology, QNAP, Asustor, Buffalo |
| **Smart Home** | 5 | Philips Hue, Google Home, Amazon Echo |
| **Security** | 2 | Doorbells, Alarm Systems |
| **Industrial** | 4 | Modbus, BACnet, SCADA, Siemens |
| **Medical** | 1 | DICOM/PACS devices |
| **Smart TVs** | 3 | Samsung, LG, Sony |
| **Other** | 4 | UPnP, MQTT, CoAP, Printer Servers |

---

## 📦 Installation

### Prerequisites

```bash
# Required packages
- Python 3.6 or higher
- pip3
- requests library
- Internet connection (for some features)

# Optional for Masscan
- masscan (for large-scale scans)
```

### Step 1: Install Dependencies

```bash
# Ubuntu/Debian/Kali Linux
sudo apt update
sudo apt install -y python3 python3-pip

# Install Python packages
pip3 install requests

# Optional: Install masscan
sudo apt install -y masscan

# macOS
brew install python3 masscan

# Windows
# Download Python from python.org
# Download Masscan from GitHub
```

### Step 2: Clone Repository

```bash
git clone https://github.com/Ch3aT4rM7h8dImd007/ultimate-iot-scanner.git
cd ultimate-iot-scanner
```

### Step 3: Make Executable

```bash
chmod +x ultimate_device_scanner.py
```

### Step 4: Run

```bash
python3 ultimate_device_scanner.py
```

---

## 📂 Device Database

### Camera Brands (18)

| Brand | Ports | Default Credentials | Detection Keywords |
|-------|-------|--------------------|-------------------|
| **Axis** | 80, 443, 554, 8080, 7001, 7002 | root:pass, admin:admin | Axis, AXIS, MJPEG |
| **Hikvision** | 80, 443, 8000, 8080, 554, 37777 | admin:12345, admin:admin | Hikvision, DVR, iVMS |
| **Dahua** | 80, 37777, 8080, 554, 443 | admin:admin, admin:123456 | Dahua, DVR, NVR |
| **TP-Link** | 80, 443, 554 | admin:admin, admin:password | TP-LINK, Tapo, Kasa |
| **D-Link** | 80, 443, 554, 8080 | admin:admin, admin: | D-Link, mydlink |
| **Foscam** | 80, 443, 554, 88, 8080 | admin:, admin:admin | Foscam, FOSCAM |
| **Vivotek** | 80, 443, 554, 8080, 3551 | root:pass, admin:admin | Vivotek, VIVOTEK |
| **Panasonic** | 80, 443, 554, 8080 | admin:admin, root:root | Panasonic, i-Pro |
| **Sony** | 80, 443, 554, 8080 | admin:admin, root:root | Sony, SNC, IPELA |
| **Bosch** | 80, 443, 554, 8080 | admin:admin, service:service | Bosch, VIP, DINION |
| **Pelco** | 80, 443, 554, 8080 | admin:admin, admin:pelco | Pelco, Sarix, Spectra |
| **Samsung** | 80, 443, 554, 8080 | admin:admin, admin:4321 | Samsung, Wisenet |
| **LG** | 80, 443, 554 | admin:admin, root:root | LG, LGE |
| **GeoVision** | 80, 443, 5555, 8080 | admin:admin, admin:1234 | GeoVision, GV |
| **ACTi** | 80, 443, 554, 8080 | admin:admin, admin:12345 | ACTi, Acti |
| **Arecont** | 80, 443, 554 | admin:admin, root:root | Arecont, ARECONT |
| **AVTECH** | 80, 443, 554, 8080, 34567 | admin:admin, admin: | AVTECH, AVtech |
| **Canon** | 80, 443 | admin:admin, root:root | Canon, Network Camera |

### Printer Brands (9)

| Brand | Ports | Detection Keywords |
|-------|-------|-------------------|
| **HP** | 80, 443, 9100, 515, 631, 161, 427 | HP LaserJet, HP OfficeJet |
| **Brother** | 80, 631, 515, 9100, 161 | Brother, BRAdmin |
| **Epson** | 80, 631, 515, 9100, 161 | Epson, WorkForce |
| **Canon** | 80, 631, 515, 9100, 161 | Canon, imageRUNNER |
| **Lexmark** | 80, 443, 9100, 515, 631 | Lexmark, LEXMARK |
| **Samsung** | 80, 443, 9100, 515, 631 | Samsung, Samsung MFP |
| **Xerox** | 80, 443, 9100, 515, 631 | Xerox, WorkCentre |
| **Ricoh** | 80, 443, 9100, 515, 631 | Ricoh, Aficio |
| **Kyocera** | 80, 443, 9100, 515, 631 | Kyocera, ECOSYS |

### Router Brands (8)

| Brand | Ports | Default Credentials | Detection Keywords |
|-------|-------|--------------------|-------------------|
| **MikroTik** | 80, 443, 8291, 8728, 8729, 22, 23 | admin:, admin:admin | MikroTik, RouterOS |
| **Cisco** | 80, 443, 22, 23, 161 | cisco:cisco, admin:admin | Cisco, IOS, Catalyst |
| **Huawei** | 80, 443, 22, 23, 161, 8080 | admin:admin, root:root | Huawei, Quidway |
| **ZTE** | 80, 443, 22, 23, 8080 | admin:admin, root:root | ZTE, ZTE Router |
| **Netgear** | 80, 443, 22, 23 | admin:password, admin:admin | Netgear, Nighthawk |
| **ASUS** | 80, 443, 22, 23, 8080 | admin:admin, admin:password | ASUS, RT-AC, RT-AX |
| **TP-Link** | 80, 443, 22, 23 | admin:admin, admin:password | TP-LINK, Archer |
| **D-Link** | 80, 443, 22, 23 | admin:admin, admin: | D-Link, DIR- |

### IoT Devices (5)

| Device | Ports | Default Credentials | Detection Keywords |
|--------|-------|--------------------|-------------------|
| **Raspberry Pi** | 80, 443, 22, 8123, 1880, 5900 | pi:raspberry, root:root | Raspberry Pi, Home Assistant |
| **Arduino** | 80, 443 | - | Arduino, ESP8266 |
| **ESP32** | 80, 443 | - | ESP32, NodeMCU |
| **webcamXP** | 80, 8080, 8888 | - | webcamXP, webcamXp |
| **Yawcam** | 8080, 8888 | - | Yawcam, yawcam |

---

## 🎯 Usage Guide

### Menu Options

```text
[ Menu ]
1. IP Range Scan (All Devices)
2. Subnet Scan (CIDR)
3. Google Dork Scan
4. Masscan Scan
5. Run All Tools Together
6. Generate Report from Master Data
7. Scan Only Cameras
8. Scan Only Printers
9. Scan Only Routers
10. Scan Only IoT Devices
0. Exit
```

### Example Usage

```bash
$ python3 ultimate_device_scanner.py

======================================================================
     ULTIMATE IoT DEVICE SCANNER v6.0
     Complete Scanner for All Device Types
     🔴 Live Terminal Output Enabled
     💾 Auto-Save Every 5 IPs
======================================================================
[*] Total 83 device types in database
[*] Master report file: scan_master_report.json
[!] Use only on your own network!
======================================================================

📊 Existing data found: 12 unique devices
   (New scans will be appended to this data)

[ Menu ]
1. IP Range Scan (All Devices)
2. Subnet Scan (CIDR)
3. Google Dork Scan
4. Masscan Scan
5. Run All Tools Together
6. Generate Report from Master Data
7. Scan Only Cameras
8. Scan Only Printers
9. Scan Only Routers
10. Scan Only IoT Devices
0. Exit

Your choice (0-10): 2

CIDR (e.g., 192.168.1.0/24): 192.168.1.0/24

🌐 Starting Subnet Scan: 192.168.1.0/24
 ℹ 📊 Found total 254 IPs in subnet
 ════════════════════════════════════════════════════════════

 🔍 Starting scan for IP: 192.168.1.1
    ℹ Scanning mikrotik at 192.168.1.1...
      → Port 80 is OPEN
      → Port 443 is OPEN
      → Port 8291 is OPEN
    ✓ Scan complete for mikrotik at 192.168.1.1
 🎯 Found 1 device(s) at 192.168.1.1
    📱 mikrotik (router) - Ports: [80, 443, 8291]

 🔍 Starting scan for IP: 192.168.1.10
    ℹ Scanning hikvision at 192.168.1.10...
      → Port 80 is OPEN
      → Port 554 is OPEN
    ℹ Checking HTTP paths for hikvision...
      → Found: /login.asp (Status: 200)
    ✓ Scan complete for hikvision at 192.168.1.10
 🎯 Found 1 device(s) at 192.168.1.10
    📱 hikvision (camera) - Ports: [80, 554]

 💾 Auto-saving progress... (2 new devices found)
 ✅ Master report updated: scan_master_report.json

 📈 Progress: 10/254 IPs scanned (3%) - Elapsed: 15.2s
```

### Live Output Features

The scanner provides real-time feedback:

```text
✅ SUCCESS - Green for successful operations
⚠️ WARNING - Yellow for warnings
❌ ERROR - Red for errors
ℹ INFO - Blue for information
📊 Progress tracking
💾 Auto-save notifications
🎯 Device discovery alerts
```

---

## 🔍 Scan Methods

### 1. IP Range Scan
Scans a range of IP addresses for all device types.

```text
Start IP: 192.168.1.1
End IP: 192.168.1.254
```

### 2. Subnet Scan (CIDR)
Scans an entire subnet using CIDR notation.

```text
CIDR: 192.168.1.0/24
CIDR: 10.0.0.0/16
CIDR: 172.16.0.0/12
```

### 3. Google Dork Scan
Uses Google dorks to find publicly exposed devices.

```text
Dorks include:
- intitle:"Live View / - AXIS" inurl:view.shtml
- intitle:"Network Camera" inurl:view.shtml
- inurl:/axis-cgi/mjpg/
- intitle:"WebcamXP 5"
- intitle:"Router Login" inurl:login
- intitle:"MikroTik" inurl:webfig
- intitle:"Brother" inurl:"/etc/headline.html"
```

### 4. Masscan Scan
Uses Masscan for fast, large-scale scanning.

```text
Target: 192.168.1.0/24
Ports: 1-1000 (default)
Rate: 1000 packets/sec
```

### 5. Run All Tools Together
Executes all scan methods in sequence.

### 6. Generate Report
Creates a detailed report from master data.

### 7-10. Device-Specific Scans
- **Cameras** - All 18 camera brands
- **Printers** - All 9 printer brands
- **Routers** - All 8 router brands
- **IoT Devices** - Raspberry Pi, Arduino, ESP32, etc.

---

## 🏗️ How It Works

### Complete Architecture

```text
┌─────────────────────────────────────────────────────────────────────┐
│                     ULTIMATE IoT SCANNER v6.0                       │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   PHASE 1: INITIALIZATION                   │   │
│  │                                                             │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 1. Load Device Database                             │    │   │
│  │  │    - 100+ device types                              │    │   │
│  │  │    - Ports, paths, credentials                      │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  │                          │                                   │   │
│  │                          ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 2. Load Master Report                               │    │   │
│  │  │    - Check for existing data                        │    │   │
│  │  │    - Initialize JSON storage                        │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  │                          │                                   │   │
│  │                          ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 3. Setup Signal Handlers                            │    │   │
│  │  │    - CTRL+C support                                 │    │   │
│  │  │    - Graceful interruption                          │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   PHASE 2: SCAN EXECUTION                   │   │
│  │                                                             │   │
│  │  For Each IP:                                               │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 1. For Each Device Type:                            │    │   │
│  │  │    - Port scan (threaded, 50 workers)               │    │   │
│  │  │    - Detect open ports                              │    │   │
│  │  │    - Grab banners                                   │    │   │
│  │  │    - Check HTTP paths                               │    │   │
│  │  │    - Test default credentials                       │    │   │
│  │  │    - Identify device type                           │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  │                          │                                   │   │
│  │                          ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 2. Progress Tracking                                │    │   │
│  │  │    - Live terminal output                           │    │   │
│  │  │    - Color-coded status                             │    │   │
│  │  │    - Elapsed time display                           │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  │                          │                                   │   │
│  │                          ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 3. Auto-Save (Every 5 IPs)                          │    │   │
│  │  │    - Save partial results                           │    │   │
│  │  │    - Append to master report                        │    │   │
│  │  │    - Update unique devices                          │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   PHASE 3: REPORT GENERATION                │   │
│  │                                                             │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 1. Master Report (JSON)                             │    │   │
│  │  │    - All scans history                              │    │   │
│  │  │    - All unique devices                             │    │   │
│  │  │    - Ports, timestamps                              │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  │                          │                                   │   │
│  │                          ▼                                   │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │ 2. Text Report                                      │    │   │
│  │  │    - Human-readable format                          │    │   │
│  │  │    - Grouped by device type                         │    │   │
│  │  │    - Detailed information                           │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   SCAN COMPLETE                             │   │
│  │                                                             │   │
│  │  📊 Summary Display                                         │   │
│  │  📄 Report Files Generated                                  │   │
│  │  💾 All Data Saved to Master Report                         │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Port Scanning Process

```python
def scan_device_port(self, ip, device_name, device_info):
    # 1. Scan all ports for this device type
    for port in device_info['ports']:
        # 2. Try TCP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            # 3. Port is open - grab banner
            device_result['open_ports'].append(port)
            banner = self.grab_banner(ip, port)
    
    # 4. Check HTTP paths
    if 80 in device_result['open_ports']:
        for path in device_info.get('paths', []):
            response = requests.get(f"http://{ip}{path}")
            if response.status_code < 400:
                device_result['paths_found'].append(path)
    
    # 5. Test default credentials
    for username, password in device_info['default_creds']:
        response = requests.get(f"http://{ip}", auth=(username, password))
        if response.status_code != 401:
            device_result['credentials_found'].append({
                'username': username,
                'password': password
            })
    
    return device_result
```

### Auto-Save System

The scanner automatically saves progress every 5 IPs:

```python
# Auto-save every 5 IPs
if completed % 5 == 0 and batch_results:
    self.print_progress(f"💾 Auto-saving progress...", "INFO", 0)
    self.save_master_report(batch_results)
    batch_results = []
```

### Master Report Structure

```json
{
  "scans": [
    {
      "scan_id": "20260811_143022",
      "scan_time": "2026-08-11T14:30:22",
      "devices_found": 5,
      "results": [...]
    }
  ],
  "all_devices": {
    "192.168.1.1": {
      "device": "mikrotik",
      "type": "router",
      "ports": [80, 443, 8291],
      "first_seen": "2026-08-11T14:30:22",
      "last_seen": "2026-08-11T14:30:22"
    }
  }
}
```

---

## 📁 Output & Reports

### Report Files Generated

```text
scan_master_report.json        # Master report (all scans)
scan_report_YYYYMMDD_HHMMSS.txt # Text report (human-readable)
masscan_YYYYMMDD_HHMMSS.json    # Masscan output (if used)
```

### Master Report (JSON)

```json
{
  "scans": [
    {
      "scan_id": "20260811_143022",
      "scan_time": "2026-08-11T14:30:22",
      "devices_found": 5,
      "results": [
        {
          "device": "hikvision",
          "type": "camera",
          "ip": "192.168.1.10",
          "open_ports": [80, 554],
          "banners": [
            {
              "port": 80,
              "data": {
                "status_code": 200,
                "server": "Hikvision-WebServer",
                "headers": {...}
              }
            }
          ],
          "paths_found": [
            {"path": "/login.asp", "status": 200},
            {"path": "/doc/page/login.asp", "status": 200}
          ],
          "credentials_found": [
            {"username": "admin", "password": "12345"}
          ]
        }
      ]
    }
  ],
  "all_devices": {
    "192.168.1.10": {
      "device": "hikvision",
      "type": "camera",
      "ports": [80, 554],
      "first_seen": "2026-08-11T14:30:22",
      "last_seen": "2026-08-11T14:30:22"
    }
  }
}
```

### Text Report Format

```text
======================================================================
MASTER SCAN REPORT
======================================================================
Total Unique Devices: 12
Total Scans: 3

Device: hikvision (camera)
IP: 192.168.1.10
Ports: [80, 554]
First Seen: 2026-08-11T14:30:22
Last Seen: 2026-08-11T14:30:22
----------------------------------------

Device: mikrotik (router)
IP: 192.168.1.1
Ports: [80, 443, 8291]
First Seen: 2026-08-11T14:30:15
Last Seen: 2026-08-11T14:30:15
----------------------------------------
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Issue 1: "No devices found"

```bash
# Problem: No devices detected
# Solution 1: Check network range
ping 192.168.1.1

# Solution 2: Check firewall
sudo ufw disable  # Temporarily disable firewall

# Solution 3: Increase timeout
# Edit the code and increase socket timeout
```

#### Issue 2: "Permission denied"

```bash
# Problem: Permission issues
# Solution: Run with sudo
sudo python3 ultimate_device_scanner.py

# Or use non-privileged ports
```

#### Issue 3: "Masscan not found"

```bash
# Problem: Masscan not installed
# Solution: Install masscan
sudo apt install masscan

# Or skip masscan, use built-in scanner
```

#### Issue 4: "Connection timeout"

```bash
# Problem: Timeout during scan
# Solution: Increase timeout values
sock.settimeout(5)  # Increase from 2

# Or scan smaller ranges
```

---

## ❓ FAQ

### General Questions

- **Q: What types of devices can this scanner find?**  
  A: Cameras, Printers, Routers, IoT devices, NAS, Smart Home, Industrial, Medical devices, and more.

- **Q: Is this legal?**  
  A: Only scan networks you own or have permission to scan.

- **Q: Does it exploit vulnerabilities?**  
  A: No, it only identifies devices and checks for default credentials.

- **Q: How accurate is the detection?**  
  A: Very accurate, using port signatures, banners, and path detection.

### Technical Questions

- **Q: How many threads does it use?**  
  A: 50 worker threads for IP scanning.

- **Q: How often does it save?**  
  A: Every 5 IPs scanned.

- **Q: What formats are supported for reports?**  
  A: JSON (master report) and Text (human-readable).

- **Q: Can I stop the scan?**  
  A: Yes, CTRL+C saves partial results.

### Performance Questions

- **Q: How long does a /24 scan take?**  
  A: 5-15 minutes depending on network speed.

- **Q: How many devices can it detect?**  
  A: Over 100 device types with 18 camera brands alone.

- **Q: Does it slow down the network?**  
  A: Minimal impact with 50 threads and 2-second timeouts.

---

## 🛡️ Security Tips

### Ethical Guidelines

- ✓ Only scan networks you own or have permission to test
- ✓ Use the tool for security auditing
- ✓ Report vulnerabilities responsibly
- ✓ Protect discovered data
- ✓ Follow all applicable laws

### Best Practices

1. **Get Permission** - Always have written authorization
2. **Test First** - Start with a small range
3. **Monitor Results** - Review findings carefully
4. **Protect Data** - Secure reports (they contain sensitive info)
5. **Stay Legal** - Follow all applicable laws
6. **Be Responsible** - Don't abuse the tool
7. **Keep Learning** - IoT devices evolve constantly

---

## 📊 Example Output

### Full Scan Example

```bash
$ python3 ultimate_device_scanner.py

======================================================================
     ULTIMATE IoT DEVICE SCANNER v6.0
     Complete Scanner for All Device Types
     🔴 Live Terminal Output Enabled
     💾 Auto-Save Every 5 IPs
======================================================================
[*] Total 83 device types in database
[*] Master report file: scan_master_report.json
[!] Use only on your own network!
======================================================================

[ Menu ]
1. IP Range Scan (All Devices)
2. Subnet Scan (CIDR)
3. Google Dork Scan
4. Masscan Scan
5. Run All Tools Together
6. Generate Report from Master Data
7. Scan Only Cameras
8. Scan Only Printers
9. Scan Only Routers
10. Scan Only IoT Devices
0. Exit

Your choice (0-10): 2

CIDR (e.g., 192.168.1.0/24): 192.168.1.0/24

🌐 Starting Subnet Scan: 192.168.1.0/24
 ℹ 📊 Found total 254 IPs in subnet
 ════════════════════════════════════════════════════════════

 🔍 Starting scan for IP: 192.168.1.1
    ℹ Scanning mikrotik at 192.168.1.1...
      → Port 80 is OPEN
      → Port 443 is OPEN
      → Port 8291 is OPEN
    ℹ Checking HTTP paths for mikrotik...
      → Found: / (Status: 200)
      → Found: /webfig (Status: 200)
    ℹ Checking default credentials for mikrotik...
      ✅ Valid credentials found: admin:admin
    ✓ Scan complete for mikrotik at 192.168.1.1
 🎯 Found 1 device(s) at 192.168.1.1
    📱 mikrotik (router) - Ports: [80, 443, 8291]

 🔍 Starting scan for IP: 192.168.1.2
    ℹ Scanning cisco at 192.168.1.2...
      → Port 80 is OPEN
      → Port 443 is OPEN
      → Port 22 is OPEN
    ℹ Checking HTTP paths for cisco...
      → Found: / (Status: 200)
    ✓ Scan complete for cisco at 192.168.1.2
 🎯 Found 1 device(s) at 192.168.1.2
    📱 cisco (router) - Ports: [80, 443, 22]

 🔍 Starting scan for IP: 192.168.1.10
    ℹ Scanning hikvision at 192.168.1.10...
      → Port 80 is OPEN
      → Port 554 is OPEN
      → Port 37777 is OPEN
    ℹ Checking HTTP paths for hikvision...
      → Found: /login.asp (Status: 200)
      → Found: /doc/page/login.asp (Status: 200)
    ℹ Checking default credentials for hikvision...
      ✅ Valid credentials found: admin:12345
    ✓ Scan complete for hikvision at 192.168.1.10
 🎯 Found 1 device(s) at 192.168.1.10
    📱 hikvision (camera) - Ports: [80, 554, 37777]

 🔍 Starting scan for IP: 192.168.1.20
    ℹ Scanning hp_printer at 192.168.1.20...
      → Port 80 is OPEN
      → Port 9100 is OPEN
    ℹ Checking HTTP paths for hp_printer...
      → Found: /hp/device/this.LCDispatcher (Status: 200)
    ✓ Scan complete for hp_printer at 192.168.1.20
 🎯 Found 1 device(s) at 192.168.1.20
    📱 hp_printer (printer) - Ports: [80, 9100]

 🔍 Starting scan for IP: 192.168.1.30
    ℹ Scanning raspberrypi at 192.168.1.30...
      → Port 80 is OPEN
      → Port 22 is OPEN
    ℹ Checking HTTP paths for raspberrypi...
      → Found: / (Status: 200)
    ✓ Scan complete for raspberrypi at 192.168.1.30
 🎯 Found 1 device(s) at 192.168.1.30
    📱 raspberrypi (iot) - Ports: [80, 22]

 💾 Auto-saving progress... (5 new devices found)
 💾 Master report updated: scan_master_report.json

 📈 Progress: 10/254 IPs scanned (3%) - Elapsed: 15.2s
 📈 Progress: 20/254 IPs scanned (7%) - Elapsed: 25.0s
 📈 Progress: 30/254 IPs scanned (11%) - Elapsed: 35.0s
 📈 Progress: 40/254 IPs scanned (15%) - Elapsed: 45.0s

... (continues for all 254 IPs)

 📈 Progress: 250/254 IPs scanned (98%) - Elapsed: 120.0s
 📈 Progress: 254/254 IPs scanned (100%) - Elapsed: 123.0s

 ======================================================================
 ✅ SUBNET SCAN COMPLETE!
 📊 Total IPs scanned: 254
 🎯 Total devices found: 12
 ⏱️  Time taken: 123.0 seconds

 💾 Saving remaining results...
 ✅ Master report updated: scan_master_report.json

[ Menu ]
1. IP Range Scan (All Devices)
2. Subnet Scan (CIDR)
3. Google Dork Scan
4. Masscan Scan
5. Run All Tools Together
6. Generate Report from Master Data
7. Scan Only Cameras
8. Scan Only Printers
9. Scan Only Routers
10. Scan Only IoT Devices
0. Exit

Your choice (0-10): 6

📊 Generating report from master data...
======================================================================
📊 MASTER SCAN REPORT
======================================================================
📱 Total Unique Devices Found: 12
📋 Total Scans Performed: 1

📂 By Device Type:
  • router: 2 devices
  • camera: 6 devices
  • printer: 2 devices
  • iot: 2 devices

📱 All Devices Found:
  • mikrotik (router)
    IP: 192.168.1.1
    Ports: [80, 443, 8291]
    First Seen: 2026-08-11T14:30:15
    Last Seen: 2026-08-11T14:30:15

  • cisco (router)
    IP: 192.168.1.2
    Ports: [80, 443, 22]
    First Seen: 2026-08-11T14:30:18
    Last Seen: 2026-08-11T14:30:18

  • hikvision (camera)
    IP: 192.168.1.10
    Ports: [80, 554, 37777]
    First Seen: 2026-08-11T14:30:20
    Last Seen: 2026-08-11T14:30:20

  • hp_printer (printer)
    IP: 192.168.1.20
    Ports: [80, 9100]
    First Seen: 2026-08-11T14:30:22
    Last Seen: 2026-08-11T14:30:22

  • raspberrypi (iot)
    IP: 192.168.1.30
    Ports: [80, 22]
    First Seen: 2026-08-11T14:30:24
    Last Seen: 2026-08-11T14:30:24

  ... and 7 more devices

======================================================================
✅ Text report saved: scan_report_20260811_143022.txt
```

---

## 📚 Resources

### Related Tools
- **Masscan** - Fast port scanner
- **Nmap** - Network mapping tool
- **Shodan** - IoT search engine

### IoT Security Resources
- OWASP IoT Project
- IoT Security Foundation
- CVE IoT Database

---

## 📝 License

```text
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⭐ Star History

If you find this tool useful, please consider starring the repository on GitHub!

---

## 👨‍💻 Author

**Security Research Team**  
- **GitHub:** [@yourusername](https://github.com/Ch3aT4rM7h8dImd007)  
- **Twitter:** [@yourtwitter](https://twitter.com/yourtwitter)  

---

## 🙏 Acknowledgments

- **Masscan Developers** - For the fast port scanner
- **Security Community** - For testing and feedback
- **All Contributors** - For code and documentation

---

## 📌 Final Notes

### Quick Start Summary

```bash
# 1. Install dependencies
sudo apt install python3 python3-pip
pip3 install requests

# 2. Clone repository
git clone https://github.com/Ch3aT4rM7h8dImd007/ultimate-iot-scanner.git
cd ultimate-iot-scanner

# 3. Run scanner
python3 ultimate_device_scanner.py

# 4. Select option 2 (Subnet Scan)
# 5. Enter CIDR (e.g., 192.168.1.0/24)
# 6. Wait for scan to complete
# 7. Check scan_master_report.json
```

### Pro Tips

- ✅ Use `/24` subnet for home networks
- ✅ Use `/16` for larger networks
- ✅ Auto-save every 5 IPs prevents data loss
- ✅ CTRL+C saves partial results
- ✅ Master report appends new scans
- ✅ Use device-specific scans for speed
- ✅ Check default credentials for security auditing

⚠️ **Remember:** Use this tool responsibly and only on networks you own or have permission to scan.

*⭐ Star this repo if you find it useful!*

*Made with ❤️ for the Security Community*

---

## 📊 Badges

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)](https://kali.org)
[![Version](https://img.shields.io/badge/version-6.0.0-brightgreen)]()

---

## 🎯 Feature Comparison

| Feature | This Scanner | Nmap | Masscan |
|---------|--------------|------|---------|
| **Device Detection** | ✅ Smart | ❌ Manual | ❌ Manual |
| **IoT Database** | ✅ 100+ | ❌ | ❌ |
| **Default Credentials** | ✅ | ❌ | ❌ |
| **Auto-Save** | ✅ | ❌ | ❌ |
| **Live Output** | ✅ Color | ❌ | ❌ |
| **Master Report** | ✅ | ❌ | ❌ |
| **Google Dorks** | ✅ | ❌ | ❌ |
| **Masscan Integration** | ✅ | ❌ | ✅ |
| **CTRL+C Support** | ✅ | ✅ | ✅ |
