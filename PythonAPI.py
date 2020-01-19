import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/http://ridings.domain.com/map/', methods=['GET'])
#?format=json&proxtext=fire
def api_id():

    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = ["Result"]

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # for book in books:
    #    if book['id'] == id:
    #        results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

    #Quering for districts that match the given conditions

    #Database
        #provincial = cluster["Provincial"]

    #Collections
        #riding = provincial["Riding"]

    #Query [Employment Rate] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input

    #Query [Household Income] in terms of REAL INT
    #Users can define percentage which will then be counted as input


    #Query [Crime Rate] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input


    #Query [Age Group] in terms of INT RANGE
    #Range will be pre-determined and users can select from a set of age ranges


    #Query [Immigration Group] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input


    #Query [Ethnicity] in terms of PERCENTAGE
    #Users can define percentage which will then be counted as input


    #Query [Education Level] in terms of 4 DISTINCT CATEGORIES
    #1) NO CERTIFICATE 2) HIGH SCHOOL DIPLOMA 3) UNDERGRADUATE 4) GRADUATE
    #Education levels will be pre-determined and users can select from a set of categories


    #Query [Historical] in terms of YEAR & PARTY
    #Users can define an input for year and can select from a set list of parties

@app.route('/', methods=['GET'])

def map():

    return "<h1>This is the home path. You can reach this by doing /map</h1>"

app.run()
