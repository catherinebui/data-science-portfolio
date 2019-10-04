from flask import Flask, render_template
import folium

app= Flask(__name__)

@app.route('/')

def home():
    return render_template("mainpage.html")

@app.route('/maps')
def map():
    return render_template("maps.html")

# @app.route('/charts')
# def chart():
#     return render_template("charts.html")

# @app.route('/folium')
# def index():
#     start_coords = (38.9, -77)
#     folium_map = folium.Map(location=start_coords, zoom_start=14)
#     return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
