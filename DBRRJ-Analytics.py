import csv
import pymongo
from pymongo import MongoClient

#Cluster
cluster = MongoClient("mongodb+srv://admin:danielhan@dbrrj-analytics-era6x.gcp.mongodb.net/test?retryWrites=true&w=majority")

#Database
provincial = cluster["Provincial"]

#Collections
riding = provincial["Riding"]

#Read parsed information into dict format
data = open("data_utf.csv")
csv_reader = csv.reader(data)
next(csv_reader)

for line in csv_reader:
    print(line)
    riding_val = {"_id":int(line[0]),
    "District":line[2],
    "Unemployment Rate":float(line[17]),
    "Household Income":float(line[13]),
    "Age [20-34]":float(line[3]),
    "Age [35-49]":float(line[4]),
    "Age [50-64]":float(line[5]),
    "Age [65+]":float(line[6]),
    "Immigrants":float(line[7]),
    "White":float(line[12]),
    "Asian":float(line[8]),
    "Middle Eastern":float(line[11]),
    "African":float(line[9]),
    "Hispanic":float(line[10]),
    "No Certificate":float(line[14]),
    "HS Diploma":float(line[15]),
    "Post-Secondary":float(line[16]),
    "Historical [2019]":line[18]}

    riding.insert_one(riding_val)
