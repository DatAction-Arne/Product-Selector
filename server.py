import os
import numpy as np
import pandas as pd
import json

from flask import Flask, render_template, url_for, request, redirect, session, make_response, send_from_directory
import flask.json
import gevent.pywsgi

subgroups = [
            { 'product' : "Handterminals", 'image' : 'static/handterminal.jpg', 'url' : 'handterminals' },
            { 'product' : "Truckterminals", 'image' : 'static/heftruckterminal.jpg', 'url' : 'heftruck-terminals' },
            { 'product' : "Wearables", 'image' : 'static/wearablecomputer.jpg', 'url' : 'wearable-computers' },

            { 'product' : "Handheld computers (PDA)", 'image' : 'static/pda.jpg', 'url' : 'pda' },
            { 'product' : "Barcodescanners", 'image' : 'static/barcodescanners.jpg', 'url' : 'barcodescanners' },
            ##{ 'product' : "FIXED SCANNERS", 'image' : 'static/scanner.png', 'url' : 'fixed-scanners' },
            { 'product' : "Printers", 'image' : 'static/printer.jpg', 'url' : 'printers' },
            ##{ 'product' : "VOICE PICKING", 'image' : 'static/voice.jpg', 'url' : 'voice' },
            { 'product' : "Robuuste tablet PC's", 'image' : 'static/tablet.jpg', 'url' : 'tablets' },
            { 'product' : "Rugged laptop", 'image' : 'static/ruggedlaptop.jpg', 'url' : 'rugged-laptops' },
            ##{ 'product' : "TOUCH PC'S", 'image' : 'static/touchpc.png', 'url' : 'touch-pc' },
            { 'product' : "RFID", 'image' : 'static/rfid.jpg', 'url' : 'rfid' },
            ]

# Formatting
""""
    Columns: ['release-date', 'supplier', 'product-group', 'product-name', 'product-name-type-only', 'image', 'link', 'accessories',
              'SCANNING', 'WIFI', 'WWAN', 'GPS', 'RESOLUTION', 'BLUETOOTH', 'NFC', 'OTHER', 'FREEZER MODEL', 'RFID', 'OS', 'KEYPAD', 'MEMORY', 'CAMERA', 'IP RATING',
              'BATTERY', 'SCAN RATE', 'SYSTEM INTERFACE', 'CORDLESS', 'MEDIA WIDTH', 'SPEED', 'PRINT MODE', 'PRINT WIDTH', 'new']
"""

def reloadFile(file):
    f = open(file)
    data = json.load(f)
    urlList = [el['url'] for el in subgroups]
    products = pd.DataFrame(data)

    return products, urlList

def get_abslute_path(subfolder, path):
    if subfolder is None:
        return app.root_path
    else:
        return app.root_path + subfolder + path



app = Flask(__name__)
app.jinja_env.globals.update(get_abslute_path=get_abslute_path)
#app.config["SECRET_KEY"] = secrets.token_urlsafe(7)


@app.route("/")

@app.route("/login")
def login():
    return "Not yet implemented."


if __name__ == "__main__":
    #http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    #http_server.serve_forever()
    app.run(debug=True)
