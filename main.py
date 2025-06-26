from flask import Flask, render_template_string, send_file, make_response
from io import BytesIO

app = Flask(__name__)

# In-memory code library
code_library = {
    "firewall_rule.py": b"""# Block an IP using iptables
ip_to_block = '192.168.1.100'
print(f"iptables -A INPUT -s {ip_to_block} -j DROP")""",
    "port_scanner.py": b"""import socket

target = '127.0.0.1'
for port in range(20, 1024):
    s = socket.socket()
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()""",
    "legal_notice.txt": b"""All scripts are for educational and legal use only. Unauthorized access is strictly prohibited."""
}

# Reusable layout with custom style
def render_page(title, content_html):
    return render_template_string(f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title} | MetaSecureGuard</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <style>
        body {{
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
        }}
        nav {{
            background-color: #161b22;
            padding: 1em 2em;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #30363d;
        }}
        nav h1 {{
            color: #58a6ff;
            margin: 0;
        }}
        nav ul {{
            list-style: none;
            display: flex;
            gap: 1.5em;
            margin: 0;
        }}
        nav ul li a {{
            color: #c9d1d9;
            text-decoration: none;
        }}
        nav ul li a:hover {{
            color: #58a6ff;
        }}
        main {{
            padding: 2em;
        }}
        footer {{
            text-align: center;
            padding: 1em;
            background-color: #161b22;
            border-top: 1px solid #30363d;
        }}
        .btn {{
            background-color: #238636;
            color: white;
            padding: 0.5em 1em;
            text-decoration: none;
            border-radius: 5px;
            display: inline-block;
            margin-top: 1em;
        }}
        .btn:hover {{
            background-color: #2ea043;
        }}
        pre {{
            background: #161b22;
            padding: 1em;
            border-radius: 6px;
            overflow-x: auto;
        }}
        h2 {{
            color: #58a6ff;
        }}
    </style>
</head>
<body>
    <nav>
        <h1>MetaSecureGuard</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/library">Code Library</a></li>
        </ul>
    </nav>
    <main>
        {content_html}
    </main>
    <footer>
        <p>&copy; 2025 MetaSecureGuard — Built by Matthew</p>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
</body>
</html>
""")

@app.route('/')
def home():
    content = '''
        <h2>Welcome to MetaSecureGuard</h2>
        <p>We build elite, open-access cybersecurity tools for legal and educational use.</p>
        <a href="/library" class="btn">Explore Code Library</a>
    '''
    return render_page("Home", content)

@app.route('/library')
def library():
    content = '<h2>Free Code Library</h2><p>All scripts are secure and ready for use.</p>'
    for filename, content_bytes in code_library.items():
        code = content_bytes.decode('utf-8')
        content += f"""
        <h3>{filename}</h3>
        <a class="btn" href="/download/{filename}">Download</a>
        <pre><code class="language-python">{code}</code></pre>
        <br/>
        """
    return render_page("Library", content)

@app.route('/download/<filename>')
def download(filename):
    if filename in code_library:
        buffer = BytesIO(code_library[filename])
        response = make_response(send_file(buffer, as_attachment=True, download_name=filename))
        return response
    return "File not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
