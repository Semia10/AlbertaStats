import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/http://ridings.domain.com/map/', methods=['GET'])
#?format=json&proxtext=fire

def api_id():

    #Quering for districts that match the given conditions

    #Database
    provincial = cluster["Provincial"]

    #Collections
    riding = provincial["Riding"]

    #Query [Unemployment Rate] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input
    riding.find({"District":{"Unemployment:" {$gte $USERINPUT ==> ?}})

    #Query [Household Income] in terms of REAL INT
    #Users can define percentage which will then be counted as input
    riding.find({"District":{"Household Income":{$gte $USERINPUT ==> ?}})

    #Query [Age Group] in terms of INT RANGE
    #Range will be pre-determined and users can select from a set of age ranges
    riding.find({"District":{$USERINPUT:"Age [20-34]"}})
    riding.find({"District":{$USERINPUT:"Age [35-49]"}})
    riding.find({"District":{$USERINPUT:"Age [50-64]"}})
    riding.find({"District":{$USERINPUT:"Age [65+]"}})

    #Query [Immigrants] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input
    riding.find({"District":{"Immigrants":{$gte $USERINPUT ==> ?}}})

    #Query [Ethnicity] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input
    riding.find({"District":{"White":{$gte $USERINPUT ==> ?}}})
    riding.find({"District":{"Asian":{$gte $USERINPUT ==> ?}}})
    riding.find({"District":{"African":{$gte $USERINPUT ==> ?}}})
    riding.find({"District":{"Hispanic":{$gte $USERINPUT ==> ?}}})
    riding.find({"District":{"Middle Eastern":{$gte $USERINPUT ==> ?}}})

    #Query [Education Level] in terms of 4 DISTINCT CATEGORIES
    #1) NO CERTIFICATE 2) HIGH SCHOOL DIPLOMA 3) Post-Secondary
    #Education levels will be pre-determined and users can select from a set of categories

    riding.find({"District":{$USERINPUT ==> ?}})
    riding.find({"District":{$USERINPUT ==> ?}})
    riding.find({"District":{$USERINPUT ==> ?}})

    #Query [Historical] in terms of DISTRICT
    #Lists the previous 5 parties voted in a specific DISTRICT
    riding.find({"Historical [2003]":{"DISTRICT":{$USERINPUT ==> ?}}})
    riding.find({"Historical [2007]":{"DISTRICT":{$USERINPUT ==> ?}}})
    riding.find({"Historical [2011]":{"DISTRICT":{$USERINPUT ==> ?}}})
    riding.find({"Historical [2015]":{"DISTRICT":{$USERINPUT ==> ?}}})
    riding.find({"Historical [2019]":{"DISTRICT":{$USERINPUT ==> ?}}})

    return jsonify(results)

@app.route('/', methods=['GET'])

def map():

    return "<h1>This is the home path. You can reach this by doing /map</h1>"

app.run()
