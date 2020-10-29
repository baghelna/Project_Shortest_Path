# Project_Shortest_Path
This webpage find the shortest between two cities in India, using Dijkstra Algorithm, We have used custom data set and folium in python to display the shortest path.

## Contents - 
- **app.py** : It is the main file, that contains which function to call and page to render.
- **dijkstra.py** : It contains the function of dijkstra that finds the shortest path for a given source and destination.
- **dataRetriever.py** : It contain a utility function to reads the Distacnes.csv and arrange it it the form of graph so that it can be passed on to dijkstra.py .
- **Distances.csv** : This file has the geodesic distance from a city to every other city in the dataset, it is like a adjacency matrix(graph) for dijkstras function.
- **Lat_Long.csv** : This  file has the latitude and longitude data for every city in dataset.
- **templates** : This folder contains the html templates that are rendered on running app.py 
- **static**: This folder contains all the static styling elements like css, img, etc.

## Note -
If you are planning to run this code on your System then here are the Steps - 
1. Python(3.6 or higher).
2. These libraries installed in python.
  - Flask(type `pip install flask` ).
  - Folium( type `pip install folium` ).
  - Pandas( type `pip install pandas` ).
  - numpy( tpye `pip install numpy` ).
  - tkinterHTML (type `pip install tkinterhtml` ).
3. Download this repository.
4. Navigate to the folder where it is downloaded.
5. run app.py file(`python app.py`).
6. Open localhost on web browser [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
