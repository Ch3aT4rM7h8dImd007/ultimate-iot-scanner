#!/bin/bash
# Ultimate IoT Device Scanner - Installation Script

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     ULTIMATE IoT DEVICE SCANNER v6.0                        ║"
echo "║     Complete Scanner for All Device Types                   ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
BLUE='\033[94m'
CYAN='\033[96m'
RESET='\033[0m'

# Step 1: Update system
echo -e "${CYAN}📦 Updating system packages...${RESET}"
sudo apt update -y

# Step 2: Install Python dependencies
echo -e "${CYAN}📦 Installing Python dependencies...${RESET}"
sudo apt install -y python3 python3-pip python3-venv

# Step 3: Install system tools
echo -e "${CYAN}📦 Installing system tools...${RESET}"
sudo apt install -y masscan nmap netcat-openbsd

# Step 4: Install Python packages
echo -e "${CYAN}📦 Installing Python packages...${RESET}"
pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt

# Step 5: Make script executable
echo -e "${CYAN}🔧 Making script executable...${RESET}"
chmod +x ultimate_device_scanner.py

# Step 6: Create results directory
mkdir -p results reports

# Step 7: Check installation
echo -e "${CYAN}🔍 Checking installation...${RESET}"

# Check Python packages
echo -e "${BLUE}Checking Python packages...${RESET}"
python3 -c "import requests; import urllib3" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Python packages installed successfully${RESET}"
else
    echo -e "${YELLOW}⚠️ Some packages may be missing${RESET}"
fi

# Check masscan
if command -v masscan &> /dev/null; then
    echo -e "${GREEN}✅ masscan installed${RESET}"
else
    echo -e "${YELLOW}⚠️ masscan not found${RESET}"
fi

# Check nmap
if command -v nmap &> /dev/null; then
    echo -e "${GREEN}✅ nmap installed${RESET}"
else
    echo -e "${YELLOW}⚠️ nmap not found${RESET}"
fi

echo ""
echo -e "${GREEN}✅ Installation complete!${RESET}"
echo ""
echo -e "${CYAN}🚀 Usage:${RESET}"
echo -e "   python3 ultimate_device_scanner.py"
echo -e "   or"
echo -e "   ./ultimate_device_scanner.py"
echo ""
echo -e "${CYAN}📊 Features:${RESET}"
echo -e "   📱 50+ Device Types (Cameras, Printers, Routers, IoT)"
echo -e "   🔍 Google Dork Integration"
echo -e "   ⚡ Masscan Support (Large Networks)"
echo -e "   💾 Auto-Save Every 5 IPs"
echo -e "   📊 Master Report (JSON + Text)"
echo ""
echo -e "${YELLOW}⚠️ Disclaimer:${RESET}"
echo -e "   Use only on your own network!"
echo -e "   Scanning without permission is illegal!"
echo ""
