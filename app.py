from flask import Flask, render_template, request, redirect, url_for, session

import folium

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "hello"


@app.route("/")
def home():
    #start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(zoom_start=14)
    return folium_map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)

