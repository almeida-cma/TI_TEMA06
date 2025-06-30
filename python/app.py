from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3

app = Flask(__name__)
DB_NAME = 'leads.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO leads (nome, email) VALUES (?, ?)", (nome, email))
    except sqlite3.IntegrityError:
        pass  # Ignora e-mails duplicados por simplicidade
    return redirect(url_for('obrigado'))

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

@app.route('/download')
def download():
    return send_from_directory('pdfs', 'LGPD-Ebook.pdf', as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
