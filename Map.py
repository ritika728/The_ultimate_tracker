from flask import Flask
from flask_googlemaps import GoogleMaps
import folium
import pandas as pd
app = Flask(__name__)

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map")
def index():
    map = folium.Map(
        location=[45.52336, -122.6750]
    )
    return map._repr_html_()
@app.route("/open-street-map")
def open_street_map():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Toner',
        zoom_start=13
    )

    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)
    
    return map._repr_html_()

@app.route("/wild-fire")
def map_marker():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )
    data = pd.DataFrame({
    'lon':[-121.667893746,-120.07159514],
    'lat':[39.092390021,36.082566967],
    'name':['Yuba City','Tulare']
    }, dtype=str)


    for i in range(0,len(data)):
        folium.Marker(
               location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
               popup=data.iloc[i]['name'],
            ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
   app.run()
