import requests
import socket
import json
import time
import threading
import ipaddress
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import urllib3
from urllib.parse import urljoin, urlparse
import subprocess
import os
import sys
import signal

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class UltimateDeviceScanner:
    def __init__(self):
        self.results = []
        self.lock = threading.Lock()
        self.scan_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.total_scanned = 0
        self.total_found = 0
        self.start_time = None
        self.scanning = False
        self.partial_report_saved = False
        self.master_report_file = "scan_master_report.json"
        
        # Signal handler for CTRL+C
        signal.signal(signal.SIGINT, self.signal_handler)
        
        # Load existing master report if exists
        self.master_data = self.load_master_report()
        
        # ============== Complete Device Database ==============
        self.devices = {
            # ===== Camera Brands =====
            'axis': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080, 7001, 7002],
                'paths': ['/view/index.shtml', '/axis-cgi/mjpg/', '/view.shtml', '/axis-cgi/view/index.shtml', 
                         '/axis-cgi/video.cgi', '/axis-cgi/mjpg/video.cgi', '/axis-cgi/stream/video'],
                'default_creds': [('root', 'pass'), ('admin', 'admin'), ('root', 'admin'), ('root', 'root')],
                'banner_keywords': ['Axis', 'AXIS', 'MJPEG', 'Network Camera']
            },
            'hikvision': {
                'type': 'camera',
                'ports': [80, 443, 8000, 8080, 554, 37777],
                'paths': ['/login.asp', '/doc/page/login.asp', '/system/deviceInfo', '/ISAPI/Security/',
                         '/onvif', '/web/Login.html', '/api/v1/auth'],
                'default_creds': [('admin', '12345'), ('admin', 'admin'), ('admin', '123456'), ('admin', '123')],
                'banner_keywords': ['Hikvision', 'DVR', 'iVMS', 'Hik-Connect']
            },
            'dahua': {
                'type': 'camera',
                'ports': [80, 37777, 8080, 554, 443],
                'paths': ['/login', '/cgi-bin/login', '/web/login', '/cgi-bin/magicBox.cgi',
                         '/cgi-bin/general.cgi', '/onvif', '/config/'],
                'default_creds': [('admin', 'admin'), ('admin', '123456'), ('admin', '888888')],
                'banner_keywords': ['Dahua', 'DVR', 'NVR', 'XVR']
            },
            'tp-link': {
                'type': 'camera',
                'ports': [80, 443, 554],
                'paths': ['/', '/login', '/cgi-bin/login', '/web', '/stream', '/snapshot'],
                'default_creds': [('admin', 'admin'), ('admin', 'password'), ('admin', '1234')],
                'banner_keywords': ['TP-LINK', 'TP-Link', 'Tapo', 'Kasa']
            },
            'dlink': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/cgi-bin/', '/config/', '/video', '/image', '/cgi-bin/video.cgi'],
                'default_creds': [('admin', 'admin'), ('admin', ''), ('user', 'user'), ('Admin', 'Admin')],
                'banner_keywords': ['D-Link', 'Dlink', 'mydlink']
            },
            'foscam': {
                'type': 'camera',
                'ports': [80, 443, 554, 88, 8080],
                'paths': ['/', '/cgi-bin/CGIProxy.cgi', '/cgi-bin/gw.cgi', '/video'],
                'default_creds': [('admin', ''), ('admin', 'admin'), ('guest', 'guest')],
                'banner_keywords': ['Foscam', 'FOSCAM']
            },
            'vivotek': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080, 3551],
                'paths': ['/', '/cgi-bin/', '/view', '/live.shtml'],
                'default_creds': [('root', 'pass'), ('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Vivotek', 'VIVOTEK']
            },
            'panasonic': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/ViewerFrame?', '/cgi-bin/'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '12345')],
                'banner_keywords': ['Panasonic', 'i-Pro', 'Network Camera']
            },
            'sony': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/view', '/cgi-bin/'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '')],
                'banner_keywords': ['Sony', 'SNC', 'IPELA']
            },
            'bosch': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/video', '/cgi-bin/'],
                'default_creds': [('admin', 'admin'), ('service', 'service'), ('root', 'root')],
                'banner_keywords': ['Bosch', 'BOSCH', 'VIP', 'DINION']
            },
            'pelco': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('admin', 'pelco'), ('root', 'root')],
                'banner_keywords': ['Pelco', 'PELCO', 'Sarix', 'Spectra']
            },
            'samsung': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '4321')],
                'banner_keywords': ['Samsung', 'Wisenet', 'Samsung Techwin']
            },
            'lg': {
                'type': 'camera',
                'ports': [80, 443, 554],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['LG', 'LGE', 'LG Network Camera']
            },
            'geovision': {
                'type': 'camera',
                'ports': [80, 443, 5555, 8080],
                'paths': ['/', '/login', '/cgi-bin/'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '1234')],
                'banner_keywords': ['GeoVision', 'GeoVision', 'GV']
            },
            'acti': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '12345')],
                'banner_keywords': ['ACTi', 'Acti', 'ACTi Camera']
            },
            'arecont': {
                'type': 'camera',
                'ports': [80, 443, 554],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Arecont', 'ARECONT']
            },
            'avtech': {
                'type': 'camera',
                'ports': [80, 443, 554, 8080, 34567],
                'paths': ['/', '/cgi-bin/', '/view', '/videostream.cgi'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '')],
                'banner_keywords': ['AVTECH', 'AVtech']
            },
            'brunof': {
                'type': 'camera',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Brunof', 'BRUNOF']
            },
            'canon': {
                'type': 'camera',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/view'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Canon', 'CANON', 'Network Camera']
            },
            
            # ===== Printer Brands =====
            'hp_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631, 161, 427],
                'paths': ['/hp/device/this.LCDispatcher', '/hp/device/', '/', '/cgi-bin/',
                         '/web/guest/en/webservices/status', '/Info', '/DevMgmt'],
                'default_creds': [],
                'banner_keywords': ['HP LaserJet', 'HP', 'Hewlett-Packard', 'HP OfficeJet', 'HP DeskJet',
                                   'HP Printer', 'HP Color', 'HP MFP', 'HP DesignJet']
            },
            'brother_printer': {
                'type': 'printer',
                'ports': [80, 631, 515, 9100, 161],
                'paths': ['/etc/headline.html', '/', '/cgi-bin/', '/net/', '/print'],
                'default_creds': [],
                'banner_keywords': ['Brother', 'BRAdmin', 'Brother Printer']
            },
            'epson_printer': {
                'type': 'printer',
                'ports': [80, 631, 515, 9100, 161],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Epson', 'EPSON', 'Epson Printer', 'WorkForce']
            },
            'canon_printer': {
                'type': 'printer',
                'ports': [80, 631, 515, 9100, 161],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Canon', 'CANON', 'Canon Printer', 'imageRUNNER']
            },
            'lexmark_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status', '/network'],
                'default_creds': [],
                'banner_keywords': ['Lexmark', 'LEXMARK', 'Lexmark Printer']
            },
            'samsung_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Samsung', 'Samsung Printer', 'Samsung MFP']
            },
            'xerox_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Xerox', 'XEROX', 'Xerox Printer', 'WorkCentre']
            },
            'ricoh_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Ricoh', 'RICOH', 'Ricoh Printer', 'Aficio']
            },
            'kyocera_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Kyocera', 'KYOCERA', 'Kyocera Printer', 'ECOSYS']
            },
            'dell_printer': {
                'type': 'printer',
                'ports': [80, 443, 9100, 515, 631],
                'paths': ['/', '/cgi-bin/', '/print', '/status'],
                'default_creds': [],
                'banner_keywords': ['Dell', 'DELL', 'Dell Printer']
            },
            
            # ===== Router/Network Devices =====
            'mikrotik': {
                'type': 'router',
                'ports': [80, 443, 8291, 8728, 8729, 22, 23],
                'paths': ['/', '/webfig', '/winbox', '/cgi-bin/', '/rest'],
                'default_creds': [('admin', ''), ('admin', 'admin'), ('admin', 'password')],
                'banner_keywords': ['MikroTik', 'RouterOS', 'MikroTik Router', 'winbox']
            },
            'cisco': {
                'type': 'router',
                'ports': [80, 443, 22, 23, 161],
                'paths': ['/', '/cgi-bin/', '/login', '/web'],
                'default_creds': [('cisco', 'cisco'), ('admin', 'admin'), ('root', 'root'), 
                                ('cisco', 'password')],
                'banner_keywords': ['Cisco', 'CISCO', 'IOS', 'Catalyst', 'Linksys']
            },
            'huawei': {
                'type': 'router',
                'ports': [80, 443, 22, 23, 161, 8080],
                'paths': ['/', '/cgi-bin/', '/login', '/web'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '')],
                'banner_keywords': ['Huawei', 'HUAWEI', 'Quidway', 'HG']
            },
            'zte': {
                'type': 'router',
                'ports': [80, 443, 22, 23, 8080],
                'paths': ['/', '/cgi-bin/', '/login'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', '')],
                'banner_keywords': ['ZTE', 'ZTE', 'ZTE Router']
            },
            'netgear': {
                'type': 'router',
                'ports': [80, 443, 22, 23],
                'paths': ['/', '/cgi-bin/', '/login', '/web'],
                'default_creds': [('admin', 'password'), ('admin', 'admin'), ('admin', '1234')],
                'banner_keywords': ['Netgear', 'NETGEAR', 'Nighthawk']
            },
            'asus': {
                'type': 'router',
                'ports': [80, 443, 22, 23, 8080],
                'paths': ['/', '/cgi-bin/', '/login'],
                'default_creds': [('admin', 'admin'), ('root', 'root'), ('admin', 'password')],
                'banner_keywords': ['ASUS', 'Asus', 'RT-AC', 'RT-AX']
            },
            'tplink_router': {
                'type': 'router',
                'ports': [80, 443, 22, 23],
                'paths': ['/', '/cgi-bin/', '/login', '/web'],
                'default_creds': [('admin', 'admin'), ('admin', 'password')],
                'banner_keywords': ['TP-LINK', 'TP-Link', 'TL-WR', 'Archer']
            },
            'dlink_router': {
                'type': 'router',
                'ports': [80, 443, 22, 23],
                'paths': ['/', '/cgi-bin/', '/login', '/web'],
                'default_creds': [('admin', 'admin'), ('admin', ''), ('user', 'user')],
                'banner_keywords': ['D-Link', 'Dlink', 'DIR-']
            },
            
            # ===== Other IoT Devices =====
            'raspberrypi': {
                'type': 'iot',
                'ports': [80, 443, 22, 8123, 1880, 5900],
                'paths': ['/', '/cgi-bin/', '/web', '/homeassistant', '/node-red'],
                'default_creds': [('pi', 'raspberry'), ('root', 'root'), ('admin', 'admin')],
                'banner_keywords': ['Raspberry', 'Raspberry Pi', 'Home Assistant', 'Node-RED']
            },
            'arduino': {
                'type': 'iot',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/web'],
                'default_creds': [],
                'banner_keywords': ['Arduino', 'ESP8266', 'ESP32', 'Arduino WiFi']
            },
            'esp32': {
                'type': 'iot',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/web'],
                'default_creds': [],
                'banner_keywords': ['ESP32', 'ESP8266', 'ESP', 'NodeMCU']
            },
            'webcamxp': {
                'type': 'webcam',
                'ports': [80, 8080, 8888],
                'paths': ['/view/view.shtml', '/view/index.shtml', '/'],
                'default_creds': [],
                'banner_keywords': ['webcamXP', 'webcamXp', 'WebcamXP']
            },
            'webcam7': {
                'type': 'webcam',
                'ports': [80, 8080],
                'paths': ['/', '/view', '/cgi-bin/'],
                'default_creds': [],
                'banner_keywords': ['Webcam7', 'webcam7']
            },
            'yawcam': {
                'type': 'webcam',
                'ports': [8080, 8888],
                'paths': ['/', '/view', '/cgi-bin/'],
                'default_creds': [],
                'banner_keywords': ['Yawcam', 'yawcam']
            },
            
            # ===== Network Attached Storage (NAS) =====
            'synology': {
                'type': 'nas',
                'ports': [80, 443, 5000, 5001, 22, 21],
                'paths': ['/', '/cgi-bin/', '/web', '/download', '/photo'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Synology', 'DSM', 'DiskStation']
            },
            'qnap': {
                'type': 'nas',
                'ports': [80, 443, 8080, 22, 21],
                'paths': ['/', '/cgi-bin/', '/web', '/login', '/nas'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['QNAP', 'Qnap', 'Turbo NAS']
            },
            'asustor': {
                'type': 'nas',
                'ports': [80, 443, 8000, 8001, 22],
                'paths': ['/', '/cgi-bin/', '/web', '/login'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['ASUSTOR', 'Asustor']
            },
            'buffalo': {
                'type': 'nas',
                'ports': [80, 443, 21],
                'paths': ['/', '/cgi-bin/', '/web'],
                'default_creds': [('admin', 'admin'), ('root', 'root')],
                'banner_keywords': ['Buffalo', 'BUFFALO', 'NAS', 'LinkStation']
            },
            
            # ===== Smart Home Devices =====
            'philips_hue': {
                'type': 'smart_home',
                'ports': [80, 443, 8080],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Philips Hue', 'Hue', 'Philips']
            },
            'google_home': {
                'type': 'smart_home',
                'ports': [80, 443, 8080, 8009],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Google Home', 'Chromecast', 'Google Cast']
            },
            'amazon_echo': {
                'type': 'smart_home',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Amazon Echo', 'Alexa', 'Amazon']
            },
            'xiaomi': {
                'type': 'smart_home',
                'ports': [80, 443, 8080],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Xiaomi', 'MI', 'Mi', 'XiaoMi', 'Mi Home']
            },
            'yeelight': {
                'type': 'smart_home',
                'ports': [80, 443, 554],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Yeelight', 'YeeLight']
            },
            
            # ===== Security Devices =====
            'doorbell': {
                'type': 'security',
                'ports': [80, 443, 554],
                'paths': ['/', '/cgi-bin/', '/api', '/video'],
                'default_creds': [],
                'banner_keywords': ['Ring', 'Doorbell', 'SkyBell', 'Nest Hello']
            },
            'alarm': {
                'type': 'security',
                'ports': [80, 443],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Honeywell', 'ADT', 'Alarm', 'Security']
            },
            
            # ===== Industrial IoT =====
            'modbus': {
                'type': 'industrial',
                'ports': [502, 20000],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['Modbus', 'MODBUS']
            },
            'bacnet': {
                'type': 'industrial',
                'ports': [47808, 47809],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['BACnet', 'bacnet']
            },
            'scada': {
                'type': 'industrial',
                'ports': [4911, 44818, 502],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['SCADA', 'PLC', 'Rockwell', 'Siemens']
            },
            'siemens': {
                'type': 'industrial',
                'ports': [102, 502, 443],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Siemens', 'SIMATIC', 'S7']
            },
            
            # ===== Medical Devices =====
            'medical': {
                'type': 'medical',
                'ports': [80, 443, 104, 11112],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['DICOM', 'PACS', 'Medical', 'Patient', 'Monitor']
            },
            
            # ===== Printer Servers =====
            'cups': {
                'type': 'printer_server',
                'ports': [631, 80],
                'paths': ['/', '/cgi-bin/', '/printers', '/admin'],
                'default_creds': [],
                'banner_keywords': ['CUPS', 'Common Unix Printing System']
            },
            'ipp': {
                'type': 'printer_server',
                'ports': [631],
                'paths': ['/', '/ipp', '/printers'],
                'default_creds': [],
                'banner_keywords': ['IPP', 'Internet Printing Protocol']
            },
            
            # ===== Smart TVs =====
            'samsung_tv': {
                'type': 'tv',
                'ports': [80, 443, 8001, 8002, 8080],
                'paths': ['/', '/cgi-bin/', '/api', '/ws'],
                'default_creds': [],
                'banner_keywords': ['Samsung TV', 'Smart TV', 'Samsung Smart']
            },
            'lg_tv': {
                'type': 'tv',
                'ports': [80, 443, 8080, 9999],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['LG TV', 'Smart TV', 'webOS']
            },
            'sony_tv': {
                'type': 'tv',
                'ports': [80, 443, 8080],
                'paths': ['/', '/cgi-bin/', '/api'],
                'default_creds': [],
                'banner_keywords': ['Sony TV', 'BRAVIA', 'Sony Bravia']
            },
            
            # ===== Other Devices =====
            'upnp': {
                'type': 'network',
                'ports': [1900, 5000],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['UPnP', 'Universal Plug and Play']
            },
            'mqtt': {
                'type': 'network',
                'ports': [1883, 8883],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['MQTT', 'mosquitto', 'EMQ']
            },
            'coap': {
                'type': 'network',
                'ports': [5683, 5684],
                'paths': [],
                'default_creds': [],
                'banner_keywords': ['CoAP', 'CoAP']
            }
        }
        
        # ===== Google Dorks =====
        self.dorks = [
            'intitle:"Live View / - AXIS" inurl:view.shtml',
            'intitle:"Network Camera" inurl:view.shtml',
            'inurl:/axis-cgi/mjpg/',
            'inurl:/mjpg/video.mjpg',
            'intitle:"iVMS-4200" OR intitle:"DVR Web Client"',
            'inurl:/login.asp intitle:"DVR"',
            'intitle:"WebcamXP 5"',
            '"Server: webcamxp"',
            'intitle:"Home Camera" inurl:/cgi-bin/',
            'intitle:"Network Printer Status" inurl:hp/device/this.LCDispatcher',
            'intitle:"Brother" inurl:"/etc/headline.html"',
            'intitle:"Printer Status"',
            'inurl:hp/device/this.LCDispatcher',
            'intitle:"Router Login" inurl:login',
            'intitle:"Login" ext=asp OR ext=php inurl:/login.asp',
            'intitle:"MikroTik" inurl:webfig',
            'product:"MikroTik" port:80',
            'intitle:"Live View - " inurl:view.shtml',
            'inurl:/view/index.shtml',
            'inurl:/cgi-bin/',
            'inurl:/cgi-bin/login',
            'intitle:"Webcam" inurl:/cgi-bin/'
        ]

    def load_master_report(self):
        """Load existing master report if exists"""
        if os.path.exists(self.master_report_file):
            try:
                with open(self.master_report_file, 'r') as f:
                    return json.load(f)
            except:
                return {'scans': [], 'all_devices': {}}
        return {'scans': [], 'all_devices': {}}

    def save_master_report(self, scan_results):
        """Save to master report (append mode)"""
        current_time = datetime.now().isoformat()
        
        # Update master data
        self.master_data['scans'].append({
            'scan_id': self.scan_id,
            'scan_time': current_time,
            'devices_found': len(scan_results),
            'results': scan_results
        })
        
        # Update all_devices (unique IPs)
        for device in scan_results:
            ip = device.get('ip')
            if ip:
                if ip not in self.master_data['all_devices']:
                    self.master_data['all_devices'][ip] = {
                        'device': device.get('device'),
                        'type': device.get('type'),
                        'ports': device.get('open_ports', []),
                        'first_seen': current_time,
                        'last_seen': current_time
                    }
                else:
                    # Update existing device
                    self.master_data['all_devices'][ip]['last_seen'] = current_time
                    # Merge ports (add new ones)
                    existing_ports = set(self.master_data['all_devices'][ip]['ports'])
                    new_ports = set(device.get('open_ports', []))
                    self.master_data['all_devices'][ip]['ports'] = list(existing_ports | new_ports)
        
        # Save to file
        try:
            with open(self.master_report_file, 'w') as f:
                json.dump(self.master_data, f, indent=2, default=str)
            self.print_progress(f"💾 Master report updated: {self.master_report_file}", "SUCCESS", 0)
            return True
        except Exception as e:
            self.print_progress(f"❌ Error saving master report: {str(e)}", "ERROR", 0)
            return False

    def signal_handler(self, sig, frame):
        """Handle CTRL+C gracefully"""
        self.print_progress(f"\n⚠️ CTRL+C detected! Saving partial results...", "WARNING", 0)
        if self.results:
            self.save_master_report(self.results)
            self.print_progress(f"✅ Partial results saved! Found {len(self.results)} devices so far.", "SUCCESS", 0)
        else:
            self.print_progress(f"ℹ️ No devices found yet. Nothing to save.", "INFO", 0)
        self.scanning = False
        sys.exit(0)

    def print_progress(self, message, status="INFO", indent=0):
        """Print live progress with colors"""
        colors = {
            "INFO": "\033[94m",    # Blue
            "SUCCESS": "\033[92m", # Green
            "WARNING": "\033[93m", # Yellow
            "ERROR": "\033[91m",   # Red
            "RESET": "\033[0m",    # Reset
            "BOLD": "\033[1m"      # Bold
        }
        
        indent_spaces = "    " * indent
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if status == "INFO":
            print(f"{colors['INFO']}[{timestamp}] {indent_spaces}ℹ {message}{colors['RESET']}")
        elif status == "SUCCESS":
            print(f"{colors['SUCCESS']}[{timestamp}] {indent_spaces}✅ {message}{colors['RESET']}")
        elif status == "WARNING":
            print(f"{colors['WARNING']}[{timestamp}] {indent_spaces}⚠️  {message}{colors['RESET']}")
        elif status == "ERROR":
            print(f"{colors['ERROR']}[{timestamp}] {indent_spaces}❌ {message}{colors['RESET']}")
        else:
            print(f"{colors['BOLD']}[{timestamp}] {indent_spaces}{message}{colors['RESET']}")
        
        sys.stdout.flush()

    def scan_device_port(self, ip, device_name, device_info):
        """Scan a device's ports with live output"""
        self.print_progress(f"Scanning {device_name} at {ip}...", "INFO", 1)
        
        device_result = {
            'device': device_name,
            'type': device_info['type'],
            'ip': ip,
            'open_ports': [],
            'banners': [],
            'credentials_found': [],
            'paths_found': []
        }
        
        # Port scanning
        for port in device_info['ports']:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip, port))
                sock.close()
                
                if result == 0:
                    device_result['open_ports'].append(port)
                    self.print_progress(f"  → Port {port} is OPEN", "SUCCESS", 2)
                    banner = self.grab_banner(ip, port)
                    if banner:
                        device_result['banners'].append({'port': port, 'data': banner})
                        self.print_progress(f"  → Banner grabbed from port {port}", "SUCCESS", 2)
            except Exception as e:
                pass
        
        if not device_result['open_ports']:
            self.print_progress(f"No open ports found for {device_name} at {ip}", "WARNING", 1)
            return device_result
        
        # HTTP path checking
        if any(port in device_result['open_ports'] for port in [80, 443, 8080, 8000]):
            self.print_progress(f"Checking HTTP paths for {device_name}...", "INFO", 1)
            for path in device_info.get('paths', []):
                try:
                    protocol = 'https' if 443 in device_result['open_ports'] else 'http'
                    port = next(p for p in [443, 80, 8080, 8000] if p in device_result['open_ports'])
                    url = f"{protocol}://{ip}:{port}{path}"
                    response = requests.get(url, timeout=3, verify=False)
                    if response.status_code < 400:
                        device_result['paths_found'].append({'path': path, 'status': response.status_code})
                        self.print_progress(f"  → Found: {path} (Status: {response.status_code})", "SUCCESS", 2)
                except Exception as e:
                    pass
        
        # Default credentials check
        if device_info.get('default_creds'):
            self.print_progress(f"Checking default credentials for {device_name}...", "INFO", 1)
            for username, password in device_info['default_creds']:
                try:
                    if 80 in device_result['open_ports']:
                        url = f"http://{ip}"
                        response = requests.get(url, auth=(username, password), timeout=3)
                        if response.status_code != 401:
                            device_result['credentials_found'].append({
                                'username': username,
                                'password': password,
                                'valid': True
                            })
                            self.print_progress(f"  ✅ Valid credentials found: {username}:{password}", "SUCCESS", 2)
                except Exception as e:
                    pass
        
        self.print_progress(f"✓ Scan complete for {device_name} at {ip}", "SUCCESS", 1)
        return device_result

    def grab_banner(self, ip, port):
        """Grab service banner"""
        try:
            if port in [80, 443, 8080, 8000, 8888]:
                protocol = 'https' if port == 443 else 'http'
                url = f"{protocol}://{ip}:{port}"
                response = requests.get(url, timeout=5, verify=False, allow_redirects=True)
                return {
                    'status_code': response.status_code,
                    'headers': dict(response.headers),
                    'content_preview': response.text[:500] if response.text else '',
                    'server': response.headers.get('Server', '')
                }
            elif port in [9100, 515, 631]:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((ip, port))
                if port == 9100:
                    sock.send(b"\x00\x00\x00\x01")
                data = sock.recv(1024)
                sock.close()
                return {'raw_banner': data.decode('utf-8', errors='ignore')}
            elif port in [22, 23]:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((ip, port))
                data = sock.recv(1024)
                sock.close()
                return {'raw_banner': data.decode('utf-8', errors='ignore')}
            return None
        except:
            return None

    def scan_ip_all_devices(self, ip):
        """Scan a single IP for all devices"""
        self.print_progress(f"\n🔍 Starting scan for IP: {ip}", "BOLD", 0)
        found_devices = []
        
        for device_name, device_info in self.devices.items():
            result = self.scan_device_port(ip, device_name, device_info)
            if result['open_ports']:
                found_devices.append(result)
                with self.lock:
                    self.total_found += 1
        
        if found_devices:
            self.print_progress(f"🎯 Found {len(found_devices)} device(s) at {ip}", "SUCCESS", 0)
            for device in found_devices:
                self.print_progress(f"  📱 {device['device']} ({device['type']}) - Ports: {device['open_ports']}", "SUCCESS", 1)
        else:
            self.print_progress(f"❌ No devices found at {ip}", "WARNING", 0)
        
        return found_devices

    def scan_network_cidr(self, cidr):
        """Scan subnet with auto-save every 5 IPs"""
        self.scanning = True
        self.start_time = datetime.now()
        self.print_progress(f"\n🌐 Starting Subnet Scan: {cidr}", "BOLD", 0)
        
        try:
            network = ipaddress.IPv4Network(cidr, strict=False)
            ips = [str(ip) for ip in network.hosts()]
            
            self.print_progress(f"📊 Found total {len(ips)} IPs in subnet", "INFO", 0)
            self.print_progress("=" * 70, "BOLD", 0)
            
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(self.scan_ip_all_devices, ip) for ip in ips]
                
                completed = 0
                batch_results = []
                
                for future in as_completed(futures):
                    completed += 1
                    with self.lock:
                        self.total_scanned += 1
                    
                    try:
                        results = future.result()
                        if results:
                            with self.lock:
                                self.results.extend(results)
                                batch_results.extend(results)
                                for result in results:
                                    self.total_found += 1
                    except Exception as e:
                        self.print_progress(f"Error: {str(e)}", "ERROR", 1)
                    
                    # AUTO-SAVE every 5 IPs
                    if completed % 5 == 0 and batch_results:
                        self.print_progress(f"💾 Auto-saving progress... ({len(batch_results)} new devices found)", "INFO", 0)
                        self.save_master_report(batch_results)
                        batch_results = []  # Clear batch after saving
                    
                    if completed % 10 == 0:
                        elapsed = (datetime.now() - self.start_time).total_seconds()
                        self.print_progress(f"📈 Progress: {completed}/{len(ips)} IPs scanned ({completed*100//len(ips)}%) - Elapsed: {elapsed:.1f}s", "INFO", 0)
            
            # Save remaining results
            if batch_results:
                self.print_progress(f"💾 Saving remaining results...", "INFO", 0)
                self.save_master_report(batch_results)
                    
        except KeyboardInterrupt:
            self.print_progress(f"\n⚠️ Scan interrupted by user!", "WARNING", 0)
            if batch_results:
                self.print_progress(f"💾 Saving partial results...", "INFO", 0)
                self.save_master_report(batch_results)
            self.print_progress(f"✅ Partial results saved! Found {len(self.results)} devices so far.", "SUCCESS", 0)
            return
        
        except Exception as e:
            self.print_progress(f"Error: {str(e)}", "ERROR", 0)
        
        # Final summary
        elapsed = (datetime.now() - self.start_time).total_seconds()
        self.print_progress("=" * 70, "BOLD", 0)
        self.print_progress(f"✅ SUBNET SCAN COMPLETE!", "SUCCESS", 0)
        self.print_progress(f"📊 Total IPs scanned: {self.total_scanned}", "INFO", 0)
        self.print_progress(f"🎯 Total devices found: {self.total_found}", "SUCCESS", 0)
        self.print_progress(f"⏱️  Time taken: {elapsed:.1f} seconds", "INFO", 0)
        
        # Final save
        if self.results:
            self.save_master_report(self.results)

    def google_dork_scan(self):
        """Scan using Google Dorks"""
        self.print_progress(f"\n🔎 Starting Google Dork scan...", "BOLD", 0)
        self.print_progress(f"📊 Total {len(self.dorks)} dorks will be used", "INFO", 0)
        self.print_progress("=" * 70, "BOLD", 0)
        
        for idx, dork in enumerate(self.dorks):
            self.print_progress(f"📌 Dork {idx+1}/{len(self.dorks)}: {dork}", "INFO", 0)
            try:
                self.print_progress(f"  🔍 Searching...", "INFO", 1)
                time.sleep(0.5)
                self.print_progress(f"  ⏳ Results would appear here (use Google API)", "WARNING", 1)
            except Exception as e:
                self.print_progress(f"  Error: {str(e)}", "ERROR", 1)
        
        self.print_progress(f"✅ Google Dork scan completed!", "SUCCESS", 0)

    def masscan_scan(self, target, ports="1-1000"):
        """Use Masscan for large scans"""
        self.print_progress(f"\n⚡ Starting Masscan scan: {target}", "BOLD", 0)
        self.print_progress(f"📊 Port range: {ports}", "INFO", 0)
        self.print_progress("=" * 70, "BOLD", 0)
        
        try:
            self.print_progress(f"🔧 Running masscan command...", "INFO", 0)
            cmd = f"masscan {target} -p{ports} --rate=1000 -oJ masscan_{self.scan_id}.json"
            self.print_progress(f"  💻 Command: {cmd}", "INFO", 1)
            
            subprocess.run(cmd, shell=True, timeout=120)
            self.print_progress(f"✅ Masscan completed!", "SUCCESS", 0)
            
            if os.path.exists(f"masscan_{self.scan_id}.json"):
                self.print_progress(f"📄 Processing masscan results...", "INFO", 0)
                with open(f"masscan_{self.scan_id}.json", 'r') as f:
                    data = json.load(f)
                    self.print_progress(f"  📊 Found {len(data)} hosts", "INFO", 1)
                    for host in data:
                        ip = host.get('ip')
                        if ip:
                            self.print_progress(f"  🔍 Scanning host: {ip}", "INFO", 1)
                            self.scan_ip_all_devices(ip)
            else:
                self.print_progress(f"❌ Masscan output file not found!", "ERROR", 0)
                
        except subprocess.TimeoutExpired:
            self.print_progress(f"⏰ Masscan timed out after 120 seconds!", "ERROR", 0)
        except Exception as e:
            self.print_progress(f"❌ Masscan error: {str(e)}", "ERROR", 0)

    def generate_report(self):
        """Generate and display report from master data"""
        self.print_progress(f"\n📊 Generating report from master data...", "BOLD", 0)
        
        if not self.master_data['all_devices']:
            self.print_progress(f"⚠️ No devices found in master report!", "WARNING", 0)
            return
        
        total_devices = len(self.master_data['all_devices'])
        total_scans = len(self.master_data['scans'])
        
        self.print_progress("=" * 70, "BOLD", 0)
        self.print_progress(f"📊 MASTER SCAN REPORT", "BOLD", 0)
        self.print_progress("=" * 70, "BOLD", 0)
        self.print_progress(f"📱 Total Unique Devices Found: {total_devices}", "SUCCESS", 0)
        self.print_progress(f"📋 Total Scans Performed: {total_scans}", "INFO", 0)
        
        # Group by type
        devices_by_type = {}
        for ip, data in self.master_data['all_devices'].items():
            dtype = data.get('type', 'unknown')
            if dtype not in devices_by_type:
                devices_by_type[dtype] = []
            devices_by_type[dtype].append(ip)
        
        self.print_progress(f"\n📂 By Device Type:", "BOLD", 0)
        for dtype, ips in devices_by_type.items():
            self.print_progress(f"  • {dtype}: {len(ips)} devices", "INFO", 0)
        
        # Show all devices with ports
        self.print_progress(f"\n📱 All Devices Found:", "BOLD", 0)
        for ip, data in self.master_data['all_devices'].items():
            device = data.get('device', 'unknown')
            dtype = data.get('type', 'unknown')
            ports = data.get('ports', [])
            first_seen = data.get('first_seen', 'unknown')
            last_seen = data.get('last_seen', 'unknown')
            self.print_progress(f"  • {device} ({dtype})", "SUCCESS", 0)
            self.print_progress(f"    IP: {ip}", "INFO", 1)
            self.print_progress(f"    Ports: {ports}", "INFO", 1)
            self.print_progress(f"    First Seen: {first_seen}", "INFO", 1)
            self.print_progress(f"    Last Seen: {last_seen}", "INFO", 1)
            self.print_progress("", "INFO", 0)
        
        self.print_progress("=" * 70, "BOLD", 0)
        
        # Save a formatted text report
        text_report = f"scan_report_{self.scan_id}.txt"
        try:
            with open(text_report, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("MASTER SCAN REPORT\n")
                f.write("=" * 70 + "\n")
                f.write(f"Total Unique Devices: {total_devices}\n")
                f.write(f"Total Scans: {total_scans}\n\n")
                
                for ip, data in self.master_data['all_devices'].items():
                    f.write(f"Device: {data.get('device', 'unknown')} ({data.get('type', 'unknown')})\n")
                    f.write(f"IP: {ip}\n")
                    f.write(f"Ports: {data.get('ports', [])}\n")
                    f.write(f"First Seen: {data.get('first_seen', 'unknown')}\n")
                    f.write(f"Last Seen: {data.get('last_seen', 'unknown')}\n")
                    f.write("-" * 40 + "\n")
            
            self.print_progress(f"✅ Text report saved: {text_report}", "SUCCESS", 0)
        except Exception as e:
            self.print_progress(f"❌ Error saving text report: {str(e)}", "ERROR", 0)

    def main(self):
        """Main function"""
        print("\n" + "="*70)
        print("     ULTIMATE IoT DEVICE SCANNER v6.0")
        print("     Complete Scanner for All Device Types")
        print("     🔴 Live Terminal Output Enabled")
        print("     💾 Auto-Save Every 5 IPs")
        print("="*70)
        print(f"[*] Total {len(self.devices)} device types in database")
        print(f"[*] Master report file: {self.master_report_file}")
        print("[!] Use only on your own network!")
        print("="*70)
        
        # Show existing data
        if self.master_data['all_devices']:
            print(f"\n📊 Existing data found: {len(self.master_data['all_devices'])} unique devices")
            print(f"   (New scans will be appended to this data)")
        
        while True:
            print("\n[ Menu ]")
            print("1. IP Range Scan (All Devices)")
            print("2. Subnet Scan (CIDR)")
            print("3. Google Dork Scan")
            print("4. Masscan Scan")
            print("5. Run All Tools Together")
            print("6. Generate Report from Master Data")
            print("7. Scan Only Cameras")
            print("8. Scan Only Printers")
            print("9. Scan Only Routers")
            print("10. Scan Only IoT Devices")
            print("0. Exit")
            
            choice = input("\nYour choice (0-10): ")
            
            if choice == '1':
                self.total_scanned = 0
                self.total_found = 0
                start = input("Start IP: ")
                end = input("End IP: ")
                # For IP range, we'll use a similar approach
                self.print_progress(f"\n🌐 Starting IP Range Scan: {start} - {end}", "BOLD", 0)
                # Convert to CIDR or handle range
                self.scan_network_cidr(f"{start}/24")  # Simplified
            elif choice == '2':
                self.total_scanned = 0
                self.total_found = 0
                cidr = input("CIDR (e.g., 192.168.1.0/24): ")
                self.scan_network_cidr(cidr)
            elif choice == '3':
                self.google_dork_scan()
            elif choice == '4':
                self.total_scanned = 0
                self.total_found = 0
                target = input("Target (IP/Range): ")
                ports = input("Ports (default 1-1000): ") or "1-1000"
                self.masscan_scan(target, ports)
            elif choice == '5':
                self.total_scanned = 0
                self.total_found = 0
                self.print_progress("\n🚀 Running all tools together...", "BOLD", 0)
                self.scan_network_cidr("192.168.1.0/24")
                self.google_dork_scan()
                self.masscan_scan("192.168.1.0/24", "1-1000")
            elif choice == '6':
                self.generate_report()
            elif choice == '7':
                self.total_scanned = 0
                self.total_found = 0
                cameras = {k:v for k,v in self.devices.items() if v['type'] == 'camera'}
                self.print_progress(f"📷 Found total {len(cameras)} camera brands", "INFO", 0)
                cidr = input("CIDR: ")
                self.scan_network_cidr(cidr)
            elif choice == '8':
                self.total_scanned = 0
                self.total_found = 0
                printers = {k:v for k,v in self.devices.items() if v['type'] == 'printer'}
                self.print_progress(f"🖨️  Found total {len(printers)} printer brands", "INFO", 0)
                cidr = input("CIDR: ")
                self.scan_network_cidr(cidr)
            elif choice == '9':
                self.total_scanned = 0
                self.total_found = 0
                routers = {k:v for k,v in self.devices.items() if v['type'] == 'router'}
                self.print_progress(f"📡 Found total {len(routers)} router brands", "INFO", 0)
                cidr = input("CIDR: ")
                self.scan_network_cidr(cidr)
            elif choice == '10':
                self.total_scanned = 0
                self.total_found = 0
                iot = {k:v for k,v in self.devices.items() if v['type'] in ['iot', 'smart_home', 'security']}
                self.print_progress(f"🤖 Found total {len(iot)} IoT devices", "INFO", 0)
                cidr = input("CIDR: ")
                self.scan_network_cidr(cidr)
            elif choice == '0':
                self.print_progress("\n👋 Goodbye! Check scan_master_report.json for all results!", "SUCCESS", 0)
                break
            else:
                print("Invalid input!")

if __name__ == "__main__":
    scanner = UltimateDeviceScanner()
    scanner.main()