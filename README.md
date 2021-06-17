#  NC Retail Tax Rest API
### Index
1. What this project is
2. Data
3. Processing Data
4. Inputs
5. Calculations
6. Return Data
7. Running the Code Locally
8. Calling the API


## 1. What this project is:
- This is a REST API used to calculate the sales tax on a given sale in North Carolina 

## 2. Data
- Data for the sales tax in each NC county was tken from: https://www.salestaxhandbook.com/north-carolina/rates

## 3. Processing Data
- At the time of this project, the above site did not allow for downloading the data because of site maintenence.  If the data was available in a CSV format, it might have made more sense to download the data, and use Pandas to convert it to a dataframe.  Since that wasn't an option, I just copied the data from the site, and converted it to JSON manually.

## 4. Inputs
- In order to return a sales tax amount, we would need to know two things in advance:  The county where the sale originated, and the sale amount.  If we wanted to make this a more fleshed out project, we could collect this using form data from the front end, and pass to the API as parameters.

## 5. Calculations
- The first calcalation would be to convert the sales tax percentage to a decimal.  If the sales tax is 7%, then it would be 7/100 = .007.  This could be done in the data processing phase, which would probably make the most sense, instead of calculating each one every time the API is called.  However, if we want to return the sales tax rate as part of the API response, we'll have to make the calculation either way.  
- The second calculation is getting the sales tax amount on a given sale.  Using the above example, if the sales tax rate is .007, and the sale amount is $10, then the math is 10*.007 = .07, or 7 cents.
- Finally we'll add the sales tax amount to the sale amount and get a total sale amount.  In this case it would be 10+.07 = 10.07.  

## 6. Return Data

- Because the return data needs to be in JSON format, we could simply return something like { "data" : .07 }.  However, if this were to be usable, it might make more sense to include more information with each API call.  For example, we could return The County, County Tax Rate, Tax Amount, Purchase Amount, and Total Sale Amount.  The return data might look something like this:
- {
    "data": {
        "County": "Lee",
        "Sales Amount": "$10",
        "Tax Rate": "7%",
        "Sales Tax Amount": "$0.7",
        "Total Sale": "$10.7"
    }
}

## 7. Running the Code Locally
- In order to run the code locally, clone the repository into a local environment.
- Create a Python Virtual Environment before installing packages - $ python3 -m venv /path/to/new/virtual/environment
- Activate the virtual environment - $ python3 source env/bin/activate
- Install the libraries needed, flask & requests with pip - $ pip install flask ...
- Run the project. $ python3 nctax.py.  

## 8. Calling the API
- The project should be running on localhost:5000.  Open up Postman, or a similar service, and make a GET request to the /tax endpoint: localhost:5000/tax.  Add paramaters to the request for county and amount.  It should look similar to:  localhost:5000/tax?county=Lee&amount=$10.  The response should be in the format outlined in step #6.

## 9. Error Handling
- errorhandling.py handles the errors for incoming parameters, and returns 200 and a message, if either parameter isn't formatted correctly, or if the provided county doesn't exist.  

## 9. Testing
- Unit tests are using pytest.  To run the tests, use the command py.test test.py
