from application import app, generate, db
from flask import render_template, url_for, redirect, request
from os import getenv

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Home', hostname=getenv('HOSTNAME'))

@app.route('/palette', methods=['GET','POST'])
def get_palette():
    if request.method == 'GET':
        return redirect(url_for('home'))
    palette = generate.palette()
    name = generate.name()
    return render_template('index.html', title=name, palette=palette, hostname=getenv('HOSTNAME'))

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About', hostname=getenv('HOSTNAME'))
