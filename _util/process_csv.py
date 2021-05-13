#!/bin/env python3
import os
import sys
import csv
import simplekml

if (len(sys.argv) < 2):
    print("Usage: ./process_csv.py nodes.csv")
    os._exit(0)

with open(sys.argv[1], newline='') as csvfile:
    kml = simplekml.Kml()
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['Longitude'] and row['Latitude']):
            kml.newpoint(name=row['Street'], coords=[(round(float(row['Longitude']), 4),round(float(row['Latitude']), 4))])

kml.save(os.path.dirname(os.path.realpath(__file__)) + "/../data/nodes.kml")
