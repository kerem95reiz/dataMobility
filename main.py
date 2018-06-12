from folium import Map, Marker
from csv import reader
from pathlib import Path
from time import sleep

def read_csv_data(path):
    data = []
    with open(path, 'r', newline='') as file:
        csv_reader = reader(file)
        for line in csv_reader:
            if line[2] != 'time':
                data.append([float(line[0]), float(line[1]), line[2]])

    return data

def create_map(start_coords: tuple):

    location = Map(start_coords[:2])
    location.zoom_start = 15
    return location

def put_marker(coord: list, location: Map):
    marker = Marker(coord[:2])
    marker.add_to(location)


if __name__ == '__main__':
    data_path = "./data/trajectories_1.csv"
    data = read_csv_data(data_path)

    area = create_map(data[1])

    for data_point in data:
        put_marker(data_point, area)
    area.save(str(Path.home()) + "/Desktop/map.html")

