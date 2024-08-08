<h1>WiFi QR Code Generator</h1>
<h4>Easily generate a QR code for your guest WiFi network. This QR code can be printed and shared with guests, making it convenient for them to connect to your WiFi without needing to type in a password.
</h4>

<br>

<h1>Prerequisites:</h1>
<h4>Ensure you have the following:</h4>
<ul>
<li>
<b>Python:</b> Check by running `python --version` in your command prompt or terminal.
</li>
<li>
<b>pip:</b> Check by running `pip --version` in your command prompt or terminal.
</li>
</ul>
<h4>Install the necessary Python packages:</h4>
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
```
SSID=YOUR-WIFI-NAME<br>
PASSWORD=YOUR-WIFI-PASSWORD<br>
AUTH_TYPE=WPA<br>
IS_HIDDEN=FALSE
```
</ol>
