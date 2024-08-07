import os
from dotenv import load_dotenv
from wifi_qrcode_generator import wifi_qrcode

load_dotenv()

ssid = os.getenv('SSID')
password = os.getenv('PASSWORD')
authType = os.getenv('AUTH_TYPE')
isHidden = os.getenv('IS_HIDDEN')

def get_qrcode(ssid, password, auth_type, isHidden):
    qr_code = wifi_qrcode(ssid, hidden=isHidden, authentication_type=auth_type, password=password)

    qr_code_img = qr_code.make_image()

    return qr_code_img

qr_code = get_qrcode(ssid, password, authType, isHidden).save("wifi_code.png")