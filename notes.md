# Writing Your First Django App
By Django Team

start: 12/18/2022
end: 

Sessions
1. 12/18/2022
2. 12/19/2022
3. 12/20/2022
4. 12/21/2022
5. 12/22/2022

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

## Class Based Views 
Using Class Based Views, are a little wierd and non intuitive like function based views.
There's a lot of room and stuff to learn from this, so maybe later. I'll just keep going with the tutorial.

## Testing With the Client 
We can use from  django.test Client which let us test our app as an user were using it.
The simpliest usage would be getting a page, and from the server response do, read, or check something.

This response is just like a request, we can get the context, content, status_code and other stuff.

## Tools to learn 
Django Testing is a complete worlds of opportunities, which can add different 
libraries to this project, like coverage.py. Which tells us which lines and how much of our code 
are we testing, in order to identify dead or non-used code. 

Finally something new.

## Django Static Files
Django Static File system works just like the template system, taking the files from each app static folder.
And sometimes needing and extra folder for the static file, like the templates: 

app_name/static/app_name

Doing this avoids Django Missing or confusing two different static files, with the same name, for and on a diferent app.

Whenever we want to use an Static file in our Templates, we have to add:
in the beggining.

{% load static %} 

And when we want to use it (css style sheet for example):
file: polls/static/polls/style.css
link rel="stylesheet" href="{% static 'polls/style.css' %}"

If we want to use the static files anywere but in the templates, we have to get their relative URL

## Admin Site Configuration

We can add Models to watch and interact with on our Admin Page, but we can customizise some parts of it.
Like the Forms that appear whenever we want to add some data to our Model. This could be a simple 
way to improve our work and eficency by just adjusting these forms.

Examples:
We can modify the forms by just creating an admin.ModelAdmin subclass, so were we can use fieldsets list to 
add tuples with the changes of our form fields. 
We can cahnge them just the order, or by adding them as a tuple. We can send in the tuple, before the 
field. A title for the field.

Or we can even combine some Models Forms, especially the ones who are related, like Choices to Questions (x:1). 
This way we can save time creating first the question, then each individual choice by adding a new subclass of 
admin.StackedInLine, where we declare our model, and num of options. Then add it to the admin.ModelSubclass 
in the inline property as a list.

If StackedInLine takes a lot of screen space, we can change it. By changing it to TabularInLine

We can also modify the way of the Questions Lists and Displays, by adding a list_display tuple attribute, with the 
names of the Model attributes to be shown in order.
Also modify the way of the data is shown in the list by going to the Model Class and adding @admin.display() decorators 
to the properties or methods that we want to change it's display on the Django Admin

To the List of Objects in the Model, we can also add Filters in order to search in the object and field selected filter.
Also we can add search_fields, max_objects, ordering and other stuff.

## Creating a New Template for Django Admin

Django Admin lives, its powered and made by Django!!! Wow, right?
We can change the template of the admin by creating one ourselves.

I'm Not doing the whole process, but. We can find the admin templates dir by 
getting from django the django.__path__. There we can find the templates dir in 
django/contrib/admin/templates/

After that you can change it some how, and add others in another way.

With this, this is not over. I still have, and will, learn a lot of Django. But by now, I can relax and see where I'm going to 
focus by now.
