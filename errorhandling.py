import json

with open('counties.json') as f:
  counties = json.load(f)

def handleErrors(input):
    if input['type'] == 'county':
        if [value for key, 
        value in counties.items() 
        if key.lower().startswith(input['value'].lower())]:
            # Correct county 
            return False
        else:
            return {'error': "Not a valid NC County"}, 200
    if input['type'] == 'amount':
        try:
            int(input['value'])
            print ("INT: ", int(input['value']))
            return False
        except ValueError:
            try:
                print ("FLOAT: ", float(input['value']))
                float(input['value'])
                return False
            except ValueError:
                return {'error': "Not a valid sales amount"}, 200