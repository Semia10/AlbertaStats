import csv
import pymongo
from pymongo import MongoClient

#Cluster
cluster = MongoClient("mongodb+srv://admin:<password>@dbrrj-analytics-era6x.gcp.mongodb.net/test?retryWrites=true&w=majority")

#Database
provincial = cluster["Provincial"]

#Collections
riding = provincial["Riding"]

#Read parsed information into dict format
data = open("data_utf.csv")
csv_reader = csv.reader(data)


for line in csv_reader:
    temp = line[0].split(',')
    print(temp)

    # id = 0
    # riding_val = '{"_id":' + id + ', '
    # + '"District:"' + line[?] + ', '
    # + '"Unemployment Rate:"' + line[?] + ', '
    # + '"Household Income:"' + line[?] + ', '
    # + '"Age [20-34]:"' + line[?] + ', '
    # + '"Age [35-49]:"' + line[?] + ', '
    # + '"Age [50-64]:"' + line[?] + ', '
    # + '"Age [65+]:"' + line[?] + ', '
    # + '"Immigrants:"' + line[?] + ', '
    # + '"White:"' + line[?] + ', '
    # + '"Asian:"' + line[?] + ', '
    # + '"Middle Eastern:"' + line[?] + ', '
    # + '"African:"' + line[?] + ', '
    # + '"Hispanic:"' + line[?] + ', '
    # + '"No Certificate:"' + line[?] + ', '
    # + '"HS Diploma:"' + line[?] + ', '
    # + '"Post-Secondary:"' + line[?] + ', '
    # + '"Historical [2019]:"' + line[?] + '}'

    # riding.insert_one(riding_val)

    # id++


    # + '"Historical [2003]:"' + line[?] + ', '
    # + '"Historical [2007]:"' + line[?] + ', '
    # + '"Historical [2011]:"' + line[?] + ', '
    # + '"Historical [2015]:"' + line[?] + ', '
