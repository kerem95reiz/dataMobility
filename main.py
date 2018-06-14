from folium import Map, Marker
from csv import reader
from pathlib import Path
from time import sleep

def read_csv_data(path):
    data = []
    with open(path, 'r', newline='') as file:
        # reads the opened csv file
        csv_reader = reader(file)
        for line in csv_reader:
            # Don't take the first line 
            if line[2] != 'time':
                # first and second arguments are casted to floats
                data.append([float(line[0]), float(line[1]), line[2]])
    return data

def create_map(start_coords: tuple):
    # creates map instance with the given coordinates
    location = Map(start_coords[:2])
    # scale of the starting map
    location.zoom_start = 15
    return location

def put_marker(coord: list, location: Map):
    # create a marker with a specific coords
    marker = Marker(coord[:2])
    # add the marker to the passed the map
    marker.add_to(location)


if __name__ == '__main__':
    # address where the data is
    data_path = "./data/trajectories_1.csv"
    
    # Extracts the data 
    data = read_csv_data(data_path)
    
    # creates a map
    area = create_map(data[1])

    for data_point in data:
        # For every coords, puts a marker on the map
        put_marker(data_point, area)
        
    # saves the created map with the markers 
    area.save(str(Path.home()) + "/Desktop/map.html")

