# WiFi QR Code Generator

Easily generate a QR code for your guest WiFi network. This QR code can be printed and shared with guests, making it convenient for them to connect to your WiFi without needing to type in a password.

<br>

## Prerequisites

Ensure you have the following installed:

- **Python**: Check by running `python --version` in your command prompt or terminal.
- **pip**: Check by running `pip --version` in your command prompt or terminal.

Install the necessary Python packages (if you don't already have them):

```bash
pip install wifi-qrcode-generator python-dotenv
```

<br>

## Setup:

1. Create a `.env` file in the root directory of your project.
2. Add you WiFi credentials to the `.env` file:

```bash
SSID=YOUR-GUEST-WIFI-NAME
PASSWORD=YOUR-GUEST-WIFI-PASSWORD
AUTH_TYPE=WPA
IS_HIDDEN=FALSE
```

<br>

## Usage

To generate the QR Code, run the following command:

```bash
py -u main.py
```

This will create a QR Code image that you can print and share with your guests.

<br>

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

<br>
