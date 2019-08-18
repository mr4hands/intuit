# Intuit senior software engineer challenge

In this challenge I was asked to create an awesome aggregation system that can has to following abilities:
scrape web pages, integrate with 3rd party api's and retrieve users statements
the system aggregate the data and return the necessary info back to the user.

## Prerequisites
in order to get the system up and running on your local machine for development and testing purposes, you'll need Dokcer and Docker-compose.

How to install Docker and Docker-compose:
On Linux (CentOs 7):
https://github.com/NaturalHistoryMuseum/scratchpads2/wiki/Install-Docker-and-Docker-Compose-(Centos-7)

On Windows 10 64bit: Pro, Enterprise or Education (Build 15063 or later):
https://docs.docker.com/docker-for-windows/install/

On other Windows versions:
https://docs.docker.com/toolbox/toolbox_install_windows/

On mac:
https://docs.docker.com/docker-for-mac/install/

### Setting up on local machine (Developers and Consumers)
Create a directory to contain the project.
Go into the new directory.
Use git clone to clone the repository:
'git clone https://github.com/mr4hands/intuit'

### Configuring the application
The application is set up to run with containerized selunium-hub and mysql server.
These as well as other parameters, can be configured by changes made to the config.ini file located in the configmodule directory.

### Run docker-compose
From the pulled directory run the following command:
'docker-compose up'

### Using the api
The system uses python's flask ask it's REST api server on port 5000.
In order to use the api on your local machine, go to localhost:5000/api/<desired_path> on your browser.

### Information for Consumers
In order to get the aggregated data from the api, there are two api calls to use:
'/api/demand_data/', methods=['post']:
    receives the following json:
        { "user_id" : <string>, "username" : <string>, "last_aggregation" : <%Y-%m-%d %H:%M:%S>, "channel" : <string> }
        example json:
            { "user_id" : "061509949", "username" : "erez", "last_aggregation" : "2019-08-9 20:34:56", "channel" : "https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test" }
    returns:
        {"balance" : <float>, "transactions" : <list>}

'/api/get_user_data/', methods=['post']:
    receives the following json:
         { "user_id" : <string>, "username" : <string>, "last_aggregation" : <%Y-%m-%d %H:%M:%S> }
         example json:
            { "user_id" : "061509949", "username" : "erez", "last_aggregation" : "2019-08-9 20:34:56" }
    returns:
        {"balance" : <float>, "transactions" : <list>}

### Infromation for developers
If you with to run the system from your local machine without docker-compose you'll need:
Install python 3.7
Manually install packages from requirement.txt
on windows, open cmd and go to the project's root directory.
enter the following commands:
'set FLASK_APP=api_server.py'
'flask run'
do the equivalent in mac or linux.

### Deploying on live machines
Create a directory to contain the project.
Go into the new directory.
Use git clone to clone the repository:
'git clone https://github.com/mr4hands/intuit'
change configuration if needed in configmodule/config.ini
While in the newly created directory, in terminal, run the following command:
'docker-compose up'
Go to live machine's ip to access the api

#### Disclaimer: known issues and missing features.
As to this moment, there is no concurrent limit on accessing websites and api.

#### Assumptions made for this project
Giving the fact that every data source had different structure of data,
I assumed that transactions are to be saved the same way the are delivered, so i saved them as json format in the db.project
Regarding statements, I assumed by the description that these are scanned or photographed document, so i lay down the structure to pull these as documents from the db.