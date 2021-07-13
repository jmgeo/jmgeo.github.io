#import dependencies
import pandas as pd

#import csv file into pandas
cities_data = pd.read_csv("resources/cities.csv")

#use .to_html to convert
cities_data.to_html("cities.html", index=False)