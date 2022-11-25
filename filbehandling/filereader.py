import csv
import json
import matplotlib.pyplot as plt
from pathlib import Path

class TextReader:
    def read_csv(filename):
        """Reads a csv file and returns a list of dictionaries"""        
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
        return list(reader)
    
    def read_json(filename):
        """Reads a json file and returns a list of dictionaries"""
        with open(filename, 'r') as jsonfile:
            return json.load(jsonfile)
    



