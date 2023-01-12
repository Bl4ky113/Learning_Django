# Writing Your First Django App
By Django Team

Django Tutorial:
start: 12/18/2022
end: 12/22/2022

User Authentication:
start: 01/04/2022
end: 

Sessions Django Tutorial:
1. 12/18/2022
2. 12/19/2022
3. 12/20/2022
4. 12/21/2022
5. 12/22/2022

Sessions User Authentication:
1. 01/04/2022
2. 01/10/2022

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
We can also add or delete any app from our APP\_LIST. And Remember that you can you own 
apps by passing the appname.apps.AppNameConfig Class.

## Migrate Changes to the DB and to Django

We can make any change to the Models, and stuff, but we generally have to make a migration.
We can see this migrations by using:

$ python3 manage.py sqlmigrate app\_name num\_migration(0001)

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
refreshing the element at any moment, we could do it by using refresh\_from\_db() object method. 

Or we could use a tool from django.db.models "F", which will get the latest value of a object from the db directly.
Getting all the available or made changes in the time of getting the object from the DBs. It's less than 1 ms, but 
in big data structures, belive me, racing conditions can happen.

## Class Based Views 
Using Class Based Views, are a little wierd and non intuitive like function based views.
There's a lot of room and stuff to learn from this, so maybe later. I'll just keep going with the tutorial.

## Testing With the Client 
We can use from  django.test Client which let us test our app as an user were using it.
The simpliest usage would be getting a page, and from the server response do, read, or check something.

This response is just like a request, we can get the context, content, status\_code and other stuff.

## Tools to learn 
Django Testing is a complete worlds of opportunities, which can add different 
libraries to this project, like coverage.py. Which tells us which lines and how much of our code 
are we testing, in order to identify dead or non-used code. 

Finally something new.

## Django Static Files
Django Static File system works just like the template system, taking the files from each app static folder.
And sometimes needing and extra folder for the static file, like the templates: 

app\_name/static/app\_name

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

We can also modify the way of the Questions Lists and Displays, by adding a list\_display tuple attribute, with the 
names of the Model attributes to be shown in order.
Also modify the way of the data is shown in the list by going to the Model Class and adding @admin.display() decorators 
to the properties or methods that we want to change it's display on the Django Admin

To the List of Objects in the Model, we can also add Filters in order to search in the object and field selected filter.
Also we can add search\_fields, max\_objects, ordering and other stuff.

## Creating a New Template for Django Admin

Django Admin lives, its powered and made by Django!!! Wow, right?
We can change the template of the admin by creating one ourselves.

I'm Not doing the whole process, but. We can find the admin templates dir by 
getting from django the django.\_\_path\_\_. There we can find the templates dir in 
django/contrib/admin/templates/

After that you can change it some how, and add others in another way.

With this, this is not over. I still have, and will, learn a lot of Django. But by now, I can relax and see where I'm going to 
focus by now.

## Share, and Export Django Apps

One of Python's main is to do Code that can be reused by anyone who can use it, everyone for that matter. 
So a way to share and reuse our Django Apps could be by using settuptools lib. And create multiple 
files, licences and other stuff that declares what is our Django App, so it can be compressed, shared and 
installed via pip. There's a relative big explication about how to do it.

But I think that would be best to do it on our own with the Setup Tools Docs themselfs.

# Authentication In Django

## Installation

In order to install the minimum part of Auth of Django, we don't have to install any 
extra apps or middleware, since Django Installs them in the normal django app preparation, 
creation and installation.

But if somehow your Django App didn't have install correctly, these are the ones that you need:

Apps:
- django.contrib.auth
- django.contrib.contenttypes

Middleware:
- django.contrib.sessions.middleware.SessionMiddleware
- django.contrib.auth.middleware.AutheticationMiddleware

## User Objects

Django Since it's inits with the Auth and others Apps. In auth module, we can 
use the User model. Which we could modify the options and values of the User.
Which the default are:
- username
- email
- password
- first name
- last name

The default usage of this module is using and creating superusers, admins and staff members 
for the Django Project, which can do stuff, or just use the Django Admin.

We can change the Users password, no via the DB, because every password is stored, is hashed and encrypted.
But with different tools such as a ctl tool: 

$ python3 manage.py changepassword "username"

Or via a Django App, with the set\_password method of a User Instance.
We could also do, create or use one of the premade views and forms for changing the users' password

We can also Authenticate the user by importing the function from auth module, and then passing the username
and password as kargs. The function will return the User if the username and password are correct. Otherwise, None is returned.
The most likely thing, is that You are not going to use that low level of authecation. So you would be better using LoginViews.

## permissions and Authorizations

Django Admin, or you could use it. Or create a permission System in your Django App. Uses permissions 
to do CRUD operations in objects, which could be dbs tables models, dbs objects or rows. objects 
values and so on.

We can modify the permissions on Users individualy. Or we could create groups in order to give them a 
category and order. This could be used to modify permissions in a greater scale, or divide a fancy special 
group of users from the general users.

We can also create custom permissions by getting a content type of a model with ContentType.objects' get\_for\_model method,
and create a Permission object from the Permissions Model, passing the codename, the name, and the ContentType of the Model.

With this, we can check the permissions of the users with has\_perm method, passing the str of the permission.
But if we add or delete a permission from the user, we should re-request the user from its model, so it has the 
updated permissions.

I didn't get what the hell is a proxy, in a Model with different permissions. But it doesnt inherit the permissions.

## Authentication in Web Requests

Django uses Sessions in order to authenticate users. We can 
check this via using the request.user, checking if it is with the property
is\_authenticaded

We can log the user after its authenticated, with athentication(), with login() from auth module.
passing the user authenticated and the http request. Logout is more simple, since we only have to 
pass the request. But be carefull, since everything saved on the session will be deleted. So if you 
want to create a default or Anonymous user, you should set their session data after the 
logout().

We can limit our web pages, so only the logged in users can access and see some views. 
We could do something that redirect us to log in, or trow an error by using is\_authenticaded property.

Or we could use a decorator for our function\_views, or a MixIn for a ClassView.

from auth.decorators
@login\_required is for function\_views. Which redirects the user to a login view, if it's not logged in.
We can change the url of the authentication by setting login\_url parameter.
After the user has been authenticated, it should redirect to the same view. This view url is generally 
stored in the session variable "next", but we can change its name by passing redirect\_field\_name=''.

If we dont set the login\_url, Django will use the default /accounts/login from the settings default LOGIN\_URL

from auth.mixins
LoginRequiredMixin Can be used just like it's decorator counterpart, but as a abstraction, just by passing the custom url and 
redirect as a class parameter.
There's a function that can do this, takes the same kwargs and the next arg, or the url were the user will be redirected after 
the login.

We can add tests to the users to see if they are fit to get the request, we can do it with user\_passes\_test or UserPassesTestMixin.
They both can take the same parameters as login\_required. But it needs the test\_function to be passed as well. In the 
Mixin, you can name a method "test\_func", but this can't be stacked. We could change the get\_test\_func to get another 
function other than test\_func.

There's also a Mixin - Decorator for checking permissions, it takes a permission str, login\_url and raise\_exception:bool
Everything is just like the others, and then some logic for the permission value. 
But the raise\_exception, returns a 403 (Forbidden), if the user doesn't have the permission.

We can combine all of this into one big Mixin AccessMixin, where we have all of the paramters that we saw before, 
and then more. The behaviour is: if user is denied access, trow 403. Is anonymous user is denied, send to login or 403.

Whenever we change an user password, his session will be invalidated, and they would have to log in again. 
In order to avoid doing this. We could use update\_session\_auth\_hash(request, user), from auth module.

Django provides? to us a list of useful Class based Views to test or try the Auth module, which we can include in our 
urlpatterns by just adding django.contrib.auth.urls. We can change the urls by importing each view, and also 
we could change the template as well.
But theres a problemn, It didn't work, while I was trying it. The templates are missing from my python venv.
So an alternative would be changing them or fixing them somehow.
There's some of the views templates saved in the django website.

If we don't want to use Views pre made by Django, we could also use the Premade Forms, in auth.forms

The General Problem of these PreMade Auth stuff, is that they have a lot of assumptions about our User Model.
Which we could change. But we have to set AUTH\_USER\_MODEL

If we opt to use or do our own Templates, we could use authenticated data by using the variable user in 
the templates.

We can check with is_ authenticated, and then access it's values like an object.
We can also check for permissions, by using the variable perms, then we can access each app, and its 
permissions just like an object

We can simple if statements with the variables values, just like a str comparison, or check if 
a value is in a list, etc.
