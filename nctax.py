from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import requests
import math
import errorhandling

app = Flask(__name__)

# ----- 1. Load Counties JSON Data------

with open('counties.json') as f:
  counties = json.load(f)

# --------------------------------------

# ----- 2. Initialize the App route ------

@app.route('/tax', methods=['GET'])
def get():
    # ----- 2-a Parse Parameters ------
    # This allows us to use the url paramaters ( county and amount ) from the request

    parser = reqparse.RequestParser() # 1. Initialize the Parser
    parser.add_argument('county', required=True) # 2. add county argument
    parser.add_argument('amount', required=True) # 3. add sales price argument
    args = parser.parse_args()  # 4. parse arguments to dictionary

    # ------------------------------

    # ----- 2-b Calculate Sales Tax ------
    # We'll check to see if the passed in Parameters are valid, and then uses those paramaters co calculate the sales tax

    county = args['county'] # 1. Set county as variable
    testCounty = errorhandling.handleErrors({"type": "county", "value": county}) # Test to see if county is valid
    if testCounty:
        return testCounty # Return error if not valid
    salesAmt = args['amount'].replace("$", "") # 2. Set Sales Amount as variable, remove $ if exists
    testAmt = errorhandling.handleErrors({"type": "amount", "value": salesAmt}) # Check to see if amount is valid
    if testAmt:
        return testAmt # Return Error if amount is not valid
    countyTaxRate = float([value for key, 
    value in counties.items() 
    if key.lower().startswith(county.lower())][0])/100 # 3. Get County Tax rate from dict based on arguments
    salesTax = round(float(countyTaxRate)*float(salesAmt), 2) # 4. Calculate sales tax on sales amount

    # ------------------------------

    # ----- 2-c Create & Return Data Object and Status ------
    # 

    data = {
        "County": county,
        "Sales Amount": "$"+salesAmt,
        "Tax Rate": str(int(countyTaxRate*100))+"%",
        "Sales Tax Amount": "$"+str(salesTax),
        "Total Sale": "$"+str(float(salesTax+float(salesAmt)))
    }
    print ("DATA::::::: ", data)
    return {'data': data}, 200

    # ------------------------------

if __name__ == '__main__':
    app.run()  # run our Flask app