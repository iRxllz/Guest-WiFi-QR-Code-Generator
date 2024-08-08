<h1>WiFi QR Code Generator</h1>
<h6>Easily generate a QR code for your guest WiFi network. This QR code can be printed and shared with guests, making it convenient for them to connect to your WiFi without needing to type in a password.
</h6>

<br>

<h1>Prerequisites:</h1>
<h6>Ensure you have the following:</h6>
<ul>
<li>
<b>Python:</b> Check by running `python --version` in your command prompt or terminal.
</li>
<li>
<b>pip:</b> Check by running `pip --version` in your command prompt or terminal.
</li>
</ul>
<h6>Install the necessary Python packages:</h6>
```bash
pip install wifi-qrcode-generator python-dotenv
```

<br>

<h1>Setup:</h1>
<ol>
<li>
Create a `.env` file in the root directory of the project.
</li>
Add your WiFi credentials to your `.env` file:
```bash
SSID=YOUR-WIFI-NAME
PASSWORD=YOUR-WIFI-PASSWORD
AUTH_TYPE=WPA
IS_HIDDEN=FALSE
```
</ol>
