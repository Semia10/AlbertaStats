import flask
import pymongo
from pymongo import MongoClient
from flask import request, jsonify, redirect

#Connecting to Mongo
cluster = MongoClient("mongodb+srv://admin:danielhan@dbrrj-analytics-era6x.gcp.mongodb.net/test?retryWrites=true&w=majority")

app = flask.Flask(__name__)
app.config["DEBUG"] = True

new_url = 'http://albertastats.web.app'
@app.route('/', methods=['GET'])

def map():

    return redirect(new_url, code=302)

def api_id():

    #Quering for districts that match the given conditions

    #Database
    provincial = cluster["Provincial"]

    #Collections
    riding = provincial["Riding"]

    #User Input from WEB
    user = request.args

    #Query [Unemployment Rate] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input
    #riding.find({"Unemployment Rate":{$gte:user}})

    #Query [Household Income] in terms of REAL INT
    #Users can define percentage which will then be counted as input
    #riding.find({"Household Income":{$gte:user}})

    #Query [Age Group] in terms of INT RANGE
    #Range will be pre-determined and users can select from a set of age ranges
    # riding.find({"Age [20-34]":user})
    # riding.find({"Age [35-49]":user})
    # riding.find({"Age [50-64]":user})
    # riding.find({"Age [65+]":user})
    #
    # #Query [Immigrants] in terms of PERCENTAGE
    # #Users can define percentage which will then be counted as input
    # riding.find({"Immigrants":{$gte:user}})
    #
    # #Query [Ethnicity] in terms of PERCENTAGE
    # #Users can define percentage which will then be counted as input
    # riding.find({"White":{$gte:user}})
    # riding.find({"Asian":{$gte:user}})
    # riding.find({"African":{$gte:user}})
    # riding.find({"Hispanic":{$gte:user}})
    # riding.find({"Middle Eastern":{$gte:user}})
    #
    # #Query [Education Level] in terms of 4 DISTINCT CATEGORIES
    # #1) NO CERTIFICATE 2) HIGH SCHOOL DIPLOMA 3) Post-Secondary
    # #Education levels will be pre-determined and users can select from a set of categories
    #
    # riding.find({"Education Level":user})
    # riding.find({"Education Level":user})
    # riding.find({"Education Level":user})
    #
    # #Query [Historical] in terms of DISTRICT
    # #Lists the previous 5 parties voted in a specific DISTRICT
    # riding.find({"Historical [2003]":user})
    # riding.find({"Historical [2007]":user})
    # riding.find({"Historical [2011]":user})
    # riding.find({"Historical [2015]":user})
    # riding.find({"Historical [2019]":user})

    #return jsonify(something)

app.run()
