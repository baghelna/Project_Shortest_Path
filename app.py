from tkinter import *
from tkinterhtml import HtmlFrame
import folium
import pandas as pd
import os
from flask import Flask, render_template, url_for,request
from dijkstra import dijkstra
from dataRetriever import getGraphPoints

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/",methods = ["POST"])
def getValue():
	graph,points = getGraphPoints()
	source = request.form['source']
	dest = request.form['dest']
	min_dist,path = dijkstra(graph, 100000, source, dest)
	val = dest
	pts = [(points[dest][0], points[dest][1])]
	while path[val] != '-1':
		city = path[val]
		pts.append( (points[city][0], points[city][1]) )
		val = city
	m = folium.Map(location=[20.5937,78.9629],zoom_start = 6 )

	#points marking
	for key,[lat,long] in points.items():
		folium.Marker([lat,long], popup=key ).add_to(m)
	folium.PolyLine(pts).add_to(m)
	m.save('templates/map.html')
	return(render_template('output.html'))


@app.route("/about")
def about():
	return(render_template('about.html'))

app.run(debug = True)


# src = input("Enter src :")
# dest = input("Enter dest :")

# min_dist,path = dijkstra(graph, 100000, src, dest)

# print(min_dist)
# print(path)

# val = dest
# pts = [(points[dest][0], points[dest][1])]
# while path[val] != '-1':
#     city = path[val]
#     pts.append( (points[city][0], points[city][1]) )
#     val = city
    
# print(pts)
    
# m = folium.Map(location=[20.5937, 78.9629], zoom_start=6)

# #points marking
# for key,[lat,long] in points.items():
#     folium.Marker([lat,long], popup=key ).add_to(m)

# folium.PolyLine(pts).add_to(m)
