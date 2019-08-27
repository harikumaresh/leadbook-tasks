<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project


This task involves building a backend web API. I have used Flask to integrate PostgresSql with Frontend endpoint.

Here's why:

1. Which database engine you choose and why?

   PostgresSQL: I had some experience in PostgresSql and was simpler to load csv file.
   Easy to create tables and copy the csv content to db.
   
2. Which web framework you choose and why?

   Flask: A web application framework written only in python. It is very easy to call endpoints in Flask by using app.run() and app.route() 
3. Briefly describe the architecture of your application?
   
   --------


<!-- BUILT WITH -->
### Built With

* [Flask](https://www.tutorialspoint.com/flask/index.htm)
* [PostgresSQL](https://www.postgresql.org/)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites



* Installing Flask
```sh
pip install Flask
python -m flask --version
pip install python3-psycopg2
```

* Loading dataset into PostgresSQL schema

1. Login to postgres, create database _leadbook_ and connect to it

2. Create tables contact and company
```sh 
CREATE TABLE company (                                                                               
    id serial PRIMARY KEY,
    name varchar (50) NOT NULL,
    country varchar (50) NOT NULL,
    revenue varchar (50) NOT NULL
);
```
```sh
CREATE TABLE contact (                                                                               
    id integer NOT NULL,
    name varchar (50) NOT NULL,
    email varchar (50) NOT NULL,
    company_id integer REFERENCES company(id), PRIMARY KEY (id, company_id)
)
```

3. Copy datasets to corresponding tables
```sh 
COPY contact(id,name,email,company_id) FROM '/contact.csv' DELIMITER ',' CSV HEADER;
COPY company(id,name,country,revenue) FROM '/company.csv' DELIMITER ',' CSV HEADER;
```

### Running the script

* Clone the repo
```sh
git clone https:://github.com/harikumaresh/leadbook.git
```


## Usage

* Running app.py on terminal should be suffice
```sh
python app.py.
```
This will show link [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
1. [http://127.0.0.1:5000/contacts/](http://127.0.0.1:5000/contacts/)
2. [http://127.0.0.1:5000/contacts/1](http://127.0.0.1:5000/contacts/1)
3. [http://127.0.0.1:5000/contacts?company_id=2](http://127.0.0.1:5000/contacts?company_id=2)
4. [http://127.0.0.1:5000/contacts?revenue_gte=10000](http://127.0.0.1:5000/contacts?revenue_gte=10000)
5. [http://127.0.0.1:5000/contacts?name=Brittany Potter](http://127.0.0.1:5000/contacts?name=Brittany%20Potter) 
 


<!-- CONTACT -->
## Contact

Your Name - Hariharan Kumareshbabu - hariharan701@gmail.com

Project Link: [https:://github.com/harikumaresh/leadbook](https:://github.com/harikumaresh/leadbook)



