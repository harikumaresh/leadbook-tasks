#Import required python packages
from flask import Flask, request
import json
#Import the program which connects to postgres database
from extract_data import extract_data

#Create object
app = Flask(__name__)

#Creating endpoints
@app.route("/contacts")
def get_contacts():
	"""
	This functions returns response in JSON format for the given endpoint.
	
	args: None
		Variables used: name, revenue_gte,company_id 
	return:  response <Json>
	"""
    name="{}".format(request.args.get('name','none'))
    revenue_gte="{}".format(request.args.get('revenue_gte', 'none'))
    company_id="{}".format(request.args.get('company_id', 'none'))
	# Filter based on name
    if name != 'none':
        data = json.dumps(extract_data(specific_contact_name=name), indent=2)
	# Filter based on greater than or equal to revenue given
    elif revenue_gte != 'none':
        data = json.dumps(extract_data(specific_revenue=revenue_gte), indent=2)
	# Filter based on company id
    elif company_id != 'none':
        data = json.dumps(extract_data(specific_company_id=company_id), indent=2)
	# Else fetch all contacts
    else:
        data = json.dumps(extract_data(), indent=2)

    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/contacts/<id>")
def specific_contact(id):
	"""
	This functions returns response in JSON format for the given endpoint.
	
	args: id  <String>: Fetch based on given emp id on the endpoint
		
	return: response <Json>
	"""
    specific_id = '{0}'.format(id)
    response = app.response_class(
        response=json.dumps(extract_data(specific_contact_id=specific_id), indent=2),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)