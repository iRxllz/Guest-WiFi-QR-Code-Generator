import os
from dotenv import load_dotenv
from wifi_qrcode_generator import wifi_qrcode

load_dotenv()

ssid = os.getenv('SSID')
password = os.getenv('PASSWORD')
auth_type = os.getenv('AUTH_TYPE', 'WPA')
is_hidden = os.getenv('IS_HIDDEN', 'False').lower() in ('true', '1', 'yes')

def getWiFiQRCode(ssid, password, auth_type='WPA', is_hidden=False, filename="guest_wifi_qrcode.png"):
    qr_code = wifi_qrcode(ssid, hidden=is_hidden, authentication_type=auth_type, password=password)
    qr_code.make_image().save(filename)
    print(f"QR code saved as {filename}")

getWiFiQRCode(ssid, password, auth_type, is_hidden)