# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os, csv

app = Flask(__name__)
app.config.update(dict(DEBUG=True))
DATAFILE = os.path.join(os.path.dirname(__file__), 'static/data/beers_for_rec.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:plotname>')
def placeholder(plotname):
    filename = plotname + ".html"
    return render_template(filename)

if __name__ == '__main__':
    app.run()
