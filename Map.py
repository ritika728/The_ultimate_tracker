from branca.element import Html
from flask import Flask
from flask_googlemaps import GoogleMaps
import folium
import pandas as pd
import urllib
import urllib.request
import json                 
from pprint import pprint
import mysql.connector 
import alert
from flask import request
app = Flask(__name__)

from flask import render_template
url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events"
response = urllib.request.urlopen(url)
text = response.read()
json_data = json.loads(text)
df = pd.json_normalize(json_data['events'])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign-in")
def my_form_post():
    return render_template("sign_in.html")

@app.route('/sign-in', methods=['POST'])
def my_form_post_func():
    em = request.form['email']
    #passw = request.form['password']
    ins = request.form['institution']
    file1=open("city.txt","a")
    file = open("email.txt", "a")
    file.write(em+"\n")
    file1.write(ins+"\n")
    file.close
    file1.close
    alert.funcalert()
    return render_template("index.html")

@app.route("/list")
def func():
    return render_template("content.html")

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

    for i in range(0,len(df)):
        cf=pd.json_normalize(df.geometries[i])
        pf=pd.json_normalize(df.categories[i])
        if pf.id[0]==8:
            for j in range(0,len(df.geometries[i])):
                folium.Marker(
                    icon = folium.Icon(color='red'),
                    popup = (
            "Coordinates: {coord}<br>"
            "Name: {name}<br>"
                ).format(coord=cf.coordinates[j],name=df.title[i]),
                    location=cf.coordinates[j]
                ).add_to(map)

    return map._repr_html_()

@app.route("/volcanoes")
def volcanoes_marker():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )

    for i in range(0,len(df)):
        cf=pd.json_normalize(df.geometries[i])
        pf=pd.json_normalize(df.categories[i])
        if pf.id[0]==12:
            for j in range(0,len(df.geometries[i])):
                folium.Marker(
                    icon = folium.Icon(color='darkred'),
                    popup = (
            "Coordinates: {coord}<br>"
            "Name: {name}<br>"
                ).format(coord=cf.coordinates[j],name=df.title[i]),
                     location=cf.coordinates[j]
                ).add_to(map)

    return map._repr_html_()


@app.route("/severe-storms")
def storm_marker():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )

    for i in range(0,len(df)):
        cf=pd.json_normalize(df.geometries[i])
        pf=pd.json_normalize(df.categories[i])
        if pf.id[0]==10:
            for j in range(0,len(df.geometries[i])):
                folium.Marker(
                    icon = folium.Icon(color='gray'),
                    popup = (
            "Coordinates: {coord}<br>"
            "Name: {name}<br>"
                ).format(coord=cf.coordinates[j],name=df.title[i]),
                     location=cf.coordinates[j]
                ).add_to(map)

    return map._repr_html_()

@app.route("/icebergs")
def iceberg_marker():
    map = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )

    for i in range(0,len(df)):
        cf=pd.json_normalize(df.geometries[i])
        pf=pd.json_normalize(df.categories[i])
        if pf.id[0]==15:
            for j in range(0,len(df.geometries[i])):
                folium.Marker(
                    icon = folium.Icon(color='blue'),
                    popup = (
            "Coordinates: {coord}<br>"
            "Name: {name}<br>"
                ).format(coord=cf.coordinates[j],name=df.title[i]),
                     location=cf.coordinates[j]
                ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
   app.run()
