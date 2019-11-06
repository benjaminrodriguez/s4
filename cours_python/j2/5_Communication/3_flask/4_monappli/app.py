import os
import hashlib
import shelve
from flask import Flask, render_template, request, flash, redirect, session, url_for

app = Flask(__name__)

SALT_LEN = 16
PBKDF2_ITER = 100000

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/login.html', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['user'], request.form['password']):
            return redirect(url_for('index'))
        else:
            error = 'Pseudo/Mot de passe incorrect'
    # Exécuté si 'GET' ou si le login échoue
    return render_template('login.html', error=error)

@app.route('/register.html', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        if valid_register(request.form['user'], request.form['password'], request.form['password_confirm']):
            flash('Vous avez crée un nouveau compte avec succès, veuillez désormais vous authentifier')
            return redirect(url_for('index'))
        else:
            error = 'Erreur lors de la création du compte'
    # Exécuté si 'GET' ou si le login échoue
    return render_template('register.html', error=error)

@app.route('/forum.html')
def forum():
    if not session.get('username'):
        flash('Vous devez vous authentifer pour accéder au forum !')
        return redirect(url_for('login'))
    return render_template('forum.html')


def valid_login(username, password):
    password_hash = database.get(username.lower())
    if not password_hash:
        return False
    # Vérifie si le password est correct
    salt, password_hash = password_hash[:SALT_LEN], password_hash[SALT_LEN:]
    computed_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf8'), salt, PBKDF2_ITER)
    if password_hash == computed_hash:
        session['username'] = username
        return True
    return False

def valid_register(username, password, password_confirm):
    if password != password_confirm:
        flash('Les mots de passe ne correspondent pas')
        return False
    if username in database.keys():
        flash('Désolé, ce nom d\'utilisateur existe déjà')
        return False
    salt = os.urandom(SALT_LEN)
    password_hash = salt + hashlib.pbkdf2_hmac('sha256', password.encode('utf8'), salt, PBKDF2_ITER)
    database[username.lower()] = password_hash
    database.sync()
    return True

database = shelve.open('users')
app.secret_key = os.urandom(32)
if __name__ == '__main__':
    app.run()

