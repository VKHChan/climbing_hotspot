from flask import Flask, render_template, request, redirect, url_for, session

import folium

from src.load_data import load_map

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "hello"


@app.route("/")
def home():
    my_map = load_map()
    
    return my_map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)

