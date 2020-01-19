import pymongo
from pymongo import MongoClient

#Cluster
cluster = MongoClient("mongodb+srv://admin:<password>@dbrrj-analytics-era6x.gcp.mongodb.net/test?retryWrites=true&w=majority")

#Database
provincial = cluster["Provincial"]

#Collections
riding = provincial["Riding"]

#Read parsed information into dict format
data = open("data.csv")
for line in data:
    id = 0
    riding_val = '{"_id":' + id + ', '
    + '"Unemployment Rate:"' + line[?] + ', '
    + '"Household Income:"' + line[?] + ', '
    + '"Age [20-34]:"' + line[?] + ', '
    + '"Age [35-49]:"' + line[?] + ', '
    + '"Age [50-64]:"' + line[?] + ', '
    + '"Age [65+]:"' + line[?] + ', '
    + '"Immigrants:"' + line[?] + ', '
    + '"Ethnicity:"' + line[?] + ', '
    + '"No Certificate:"' + line[?] + ', '
    + '"HS Diploma:"' + line[?] + ', '
    + '"Undergraduate:"' + line[?] + ', '
    + '"Graduate:"' + line[?] + ', '
    + '"Historical [2003]:"' + line[?] + ', '
    + '"Historical [2007]:"' + line[?] + ', '
    + '"Historical [2011]:"' + line[?] + ', '
    + '"Historical [2015]:"' + line[?] + ', '
    + '"Historical [2019]:"' + line[?] + '}'

    riding.insert_one(riding_val)

    id++
