# Manipulation of mysql database with sql_alchemy and mongodb with pymongo

## All the steps needed to achieve the manipulation
Here, we're going to use mongodb which is located on the cloud via the mongodb website.

1. Create a virtual environnement
```
python -m venv venv
venv/Scripts/active
```
2. Install all the dependencies written in __requirements.txt__
```
pip install -r requirements.txt
```
3. Create a an account on the mongodb website. 
4. provide the correct information in the config.yaml

If you want to test the interaction with the databse, you can use the python CLI. Don't forget to import the necessary variable to do whatever you want.
Regarding the manipulation of the mongodb database you should have a look to the commented code