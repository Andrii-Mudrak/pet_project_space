**pet_project_space current on 28-08-2022**
This pet project framework created for learning how-to-use test tools.


In this case we create test framework for testing NASA API (https://api.nasa.gov/) and 
NASA UI (https://www.nasa.gov/)

It consists of next folders:
1. application folder consists:
	- api folder contains a python file for setting API client.
	- ui folder contains a python file  for setting UI nasa.gov.
2. config folder contains a python file for common setting of the framework such as 
	main url, type of the api, ape key etc.
3. library folder contain all needed library fo framework. Now it consists only logger.
4. models folder consists data about user who can be authorised.
5. providers folder consists:
	- data folder contains a python file for generation of the data.
	- service folder contains a pytho file needed for connection to DataBase.
6. reports folder will be contains reports.
7. test folder consists:
	- api folder with tests for api
	- ui folder with tests for ui
All needed fixtures are described in conftest.py
All needed requirements of the framework are described in requirements.txt
 

 **How to run test**
for run test type in terminal command *python3 -m pytest* from folder 

**How to**
1. **Add a new test**
	-