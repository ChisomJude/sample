from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Load Balancer Test</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
            }}
            h1 {{
                color: #333;
                margin-bottom: 20px;
            }}
            .info {{
                background: #f0f0f0;
                padding: 20px;
                border-radius: 5px;
                margin: 10px 0;
            }}
            .label {{
                font-weight: bold;
                color: #667eea;
            }}
            .value {{
                color: #333;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Load Balancer Test Server</h1>
            <div class="info">
                <p class="label">Server Hostname:</p>
                <p class="value">{hostname}</p>
            </div>
            <div class="info">
                <p class="label">Server IP Address:</p>
                <p class="value">{ip_address}</p>
            </div>
            <div class="info">
                <p class="label">Status:</p>
                <p class="value">✅ Server is running!</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {'status': 'healthy', 'hostname': socket.gethostname()}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
