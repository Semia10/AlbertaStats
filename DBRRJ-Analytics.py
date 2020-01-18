import pymongo
from pymongo import MongoClient

#Cluster
cluster = MongoClient("mongodb+srv://admin:<password>@dbrrj-analytics-era6x.gcp.mongodb.net/test?retryWrites=true&w=majority")

#Database
provincial = cluster["Provincial"]

#Collections
riding = db["Riding"]
age = db["Age"]
imm = db["Immigration Status"]
eth = db["Ethnicity"]
edu = db["Education Level"]
hist = db["Historical"]

#Read parsed information into dict format
with open("UNKNOWN.csv") as file
    for line in file:
        id = 0
        riding_val = '{"_id":' + id + ', ' + '"Employment Rate:"' + line[?] + ', ' + '"Household Income:"' + line[?] + ', ' + '"Crime Rate:"' + line[?] + '}'
        age_val = '{"_id":' + id + ', ' + '"Age:"' + line[?] + '}'
        imm_val = '{"_id":' + id + ', ' + '"Immigration Status:"' + line[?] + '}'
        eth_val = '{"_id":' + id + ', ' + '"Ethnicity:"' + line[?] + '}'
        edu_val = '{"_id":' + id + ', ' + '"Education Level:"' + line[?] + '}'
        hist_val = '{"_id":' + id + ', ' + '"Historical:"' + line[?] + '}'
        riding.insert_one(riding_val)
        riding.insert_one(age_val)
        riding.insert_one(imm_val)
        riding.insert_one(eth_val)
        riding.insert_one(edu_val)
        riding.insert_one(hist_val)
        id++
