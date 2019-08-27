#import python package that is used to connect postgres
import psycopg2


def extract_data(specific_contact_id=None, specific_company_id=None, specific_revenue=None, specific_contact_name=None):
	"""
	This functions returns response in JSON format for the given endpoint.
	
	args: 
		specific_contact_id    <String>: Search in contact table for given contact id
		specific_company_id    <String>: Search in company table for given company id
		specific_revenue       <String>: Search in company table for given revenue
		specific_contact_name  <String>: Search in contact table for given contact name
		
	return: output <Dict: If connection is True>
			"InvalidConnection" <String :If connection Fails >
	"""
    exception_flag = 0

    try:
	    #Try connecting from python
        connection = psycopg2.connect(user="postgres",
                                      password="leadbook",
                                      host="localhost",
                                      database="leadbook")

        #If connection is success
		if connection:
            cursor = connection.cursor()
			#Creating a dict to hold output values
            output = {}
			output["status_code"] = "200"
			output["message"] = "successful"
            output['data'] = []

			
            if specific_revenue != None:
				""" 
				SQl query to retreive rows from table company greater than or equal to given specific_revenue. 
				Using Coalesce function to convert String formatted revenue column to Integer.
				"""
                queueSQL = "SELECT * FROM company where CAST((COALESCE(revenue,'0')) AS INTEGER) >=" + specific_revenue + ";"
                cursor.execute(queueSQL)
                company_data = cursor.fetchall()
                for row in company_data:
                    queueSQL = "SELECT * FROM contact where company_id=" + str(row[0]) + ";"
                    cursor.execute(queueSQL)
                    details = cursor.fetchall()
                    company = []
                    for entry in details:
                        company.append({"id": row[0], "name": row[1],
                                        "revenue": row[3], "location": row[2]})

                        output['data'].append({"id": entry[0], "name": entry[1],
                                               "email": entry[2], "company": company})

            else:
                if specific_contact_name != None:
					""" 
					SQl query to retreive rows from table contact equal to given specific_contact_name. 
					"""
                    specific_contact_name = "'" + specific_contact_name + "'"
                    queueSQL = "SELECT id,name,email,company_id FROM contact where name LIKE " + specific_contact_name + ";"
                elif specific_contact_id != None and specific_company_id == None:
					""" 
					SQl query to retreive rows from table contact equal to given specific_contact_id. 
					"""				
                    queueSQL = "SELECT id,name,email,company_id FROM contact where id=" + str(specific_contact_id) + ";"
                elif specific_contact_id == None and specific_company_id != None:
					""" 
					SQl query to retreive rows from table contact equal to given specific_company_id. 
					"""
                    queueSQL = "SELECT id,name,email,company_id FROM contact where company_id=" + str(specific_company_id) + ";"
                else:
					""" 
					SQl query to retreive all rows from table. 
					"""
                    queueSQL = "SELECT id,name,email,company_id FROM contact;"

                cursor.execute(queueSQL)
                contact_data = cursor.fetchall()
                
				for row in contact_data:
					""" 
					To get company details for each above query which was executed 
					"""
                    queueSQL = "SELECT * FROM company where id=" + str(row[3]) + ";"
                    cursor.execute(queueSQL)
                    details = cursor.fetchall()
                    company = []
                    for entry in details:
                        company.append({"id": entry[0], "name": entry[1],
                                        "revenue": entry[3], "location": entry[2]})

                    output['data'].append({"id": row[0], "name": row[1],
                                           "email": row[2], "company": company})

            return output

    except Exception as e:
        exception_flag = e
        pass
    finally:
        # closing database connection.
        if exception_flag == 0 and connection:
            connection.close()

    return "InvalidConnection"

# data = extract_data(specific_contact_name="Brittany Potter")