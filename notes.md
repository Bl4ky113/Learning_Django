# Writing Your First Django App
By Django Team

start: 12/18/2022
end: 

Sessions
1. 12/18/2022
2. 12/19/2022

This notes will include only simple notes about each entry or stuff that I learn about this tool.
Or stuff that I cant search with 2 or 3 googles searches.

## Download

$ pip3 install django

## Simple Development Server Usage
You can change the port and public ip of the runserver by just sending them as an argument

## Conecting Views and Urls
When you connect an App to the project App, you always have to use include()

## Config File 
We can change our timezone by just passing the Contry Code in its variable
We can also add or delete any app from our APP_LIST. And Remember that you can you own 
apps by passing the appname.apps.AppNameConfig Class.

## Migrate Changes to the DB and to Django

We can make any change to the Models, and stuff, but we generally have to make a migration.
We can see this migrations by using:

$ python3 manage.py sqlmigrate app_name num_migration(0001)

Then, it will show the SQL code to do the changes of the migration.

## See Models in the Admin Section
REMEMBER you have to declare, add and select the Models that will be shown on polls.admin file

by importing the model and then passing it to:

admin.site.register(model)

## Extra HttpResponses
We can do json, file and other HttpResponses, mostly the first ones to do a API and not always use Templates and stuff

## DBs Utils or Models
With Django.db.models we can get multiple tools to work directly with our DB, skiping Python in the process. 
Why is this usefull? Sometimes, Python will execute twice or more actions at the same time, affecting the same 
value in a model, the problem? This value might not update or get both of the changes made by the action. 
This is because Python gets the value from the model, does its work and then updates it. Avoiding or not 
refreshing the element at any moment, we could do it by using refresh_from_db() object method. 

Or we could use a tool from django.db.models "F", which will get the latest value of a object from the db directly.
Getting all the available or made changes in the time of getting the object from the DBs. It's less than 1 ms, but 
in big data structures, belive me, racing conditions can happen.
