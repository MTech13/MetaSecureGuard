from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>MetaSecureGuard</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #0f172a;
                color: #f8fafc;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #1e3a8a;
                padding: 20px;
                text-align: center;
                font-size: 2em;
                font-weight: bold;
            }
            main {
                padding: 40px;
                text-align: center;
            }
            a {
                color: #3b82f6;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
            footer {
                background-color: #1e293b;
                text-align: center;
                padding: 15px;
                position: fixed;
                width: 100%;
                bottom: 0;
                color: #94a3b8;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <header>MetaSecureGuard</header>
        <main>
            <h1>Your Cybersecurity Defense Hub</h1>
            <p>Welcome to MetaSecureGuard, led by Matthew. Explore free code libraries and legal defenses to protect your assets.</p>
            <p><a href="#">Explore the Code Library</a></p>
            <p>Check back soon for more features and security tools.</p>
        </main>
        <footer>© 2025 MetaSecureGuard. All rights reserved.</footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=False)
