# Writing Your First Django App
By Django Team

Django Tutorial:
start: 12/18/2022
end: 12/22/2022

User Authentication:
start: 01/04/2023
end: 01/16/2022

Sessions Django Tutorial:
1. 12/18/2022
2. 12/19/2022
3. 12/20/2022
4. 12/21/2022
5. 12/22/2022

Sessions User Authentication:
1. 01/04/2023
2. 01/10/2023
3. 01/11/2023
4. 01/12/2023
5. 01/15/2023
6. 01/16/2023

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

## Password Management

How The Passwords are stored in Django is almost a part where we don't even want to change or 
try something, since everything just works, is secure, and it would be unnecessarily to 
re invent it.

But we can still see how it works and use it in our projects.

Django stores the passwords in this str format:
algorithm$iterations$salt$hash

Which are just the components of a hashing algorithm.
Salt is just random data to hash the password. 
The algorithm is PBKDF2 with a SHA256 hash which could be iterated for over 300k times.

There's a lot of Password management and Hashing theory, so I will skip over this by now. Since
probably my projects test will not use such stuff.

But we can change the algorithms and hash processing in a file called hashers.py
We also have to list first the hash algorithm in the settings variable 
PASSWORD_HASHERS = []

We can test and manually manage the users passwords using:
- check_password (password_str, encoded):
    Auths the user password, with the str version of the password, and 
    how the password is stored in the db.
- make_password (password):
    Creates a password using the hash format that you use in your own app
- is_password_usable (password)
    Checks if the user has a password?

## Password Validation

We can add different Password validators in AUTH_PASSWORD_VALIDATORS
Which is a list of dicts, which can have the NAME of the Validator, and / or 
some settings of that validator, such as length value, options and others. 
 
Django has some of these Validators by default, these are:
- MinimumLengthValidator
- UserAttributeSimilarValidator
- CommonPasswordValidator
- NumericPasswordValidator

We can also add Validation to our code by using some functions from 
auth.password_validation

- validate_password(password)
    Returns None if the password is valid, Raises a Validation Error if it isn't
- password_changed(password)
    Sends an notification to al Validators that that password has been changed.
    Usefull for some validators.
- password_validators_help_text
- password_Validators_help_html:
    Get some help text of the validator
- get_passwords_validators:
    Escencialy, just returns the list of AUTH_PASSWORD_VALIDATORS

We can create our own validator, by just creating a Class and making a validate and get_help_text methods.
The validate method takes, the password, and the user which can be None by default. 
It should return nothing or None if the password is validated, ValidationError if it isn't.
get_help_text, just returns a simple help str

## Auth Deep Customization

We've talked about custom auth backends for our auth system. 
If we need to change the Backend Auth, we can modify the list of 
Auth Backends. AUTHENTICATION_BACKENDS. IF any of the Backends of the 
lists trows a PermissionDenied, auth will fail.

We can create a Backend by inheriting BaseBackend from auth.backends
This class must have a get_user(user_id), which returns an User or None.
And a authenticate method, which takes the http request and the user credentials, ids, passwords, etc.
It must return just like the get_user, the User or None.

In the custom backend we can also set the way how it process our Permissions. By changing the methods
get_user/group/all_permissions(), the checkers has_perm, has_module_perms, and with_perm.

If in the checkers the method raises PermissionDenied. The perm is not granted.

There isn't a way to handle and store the permissions of a AnonymousUser, but we can 
check in our custom backend if the sent user is a AnonymousUser, so we could build a 
structure to handle their permissions.

Alse we should consider if that our Custom Model of User and Custom Backend, we should handle the 
is_active variable in order to check if the acount can or can't authenticate.

## Custom Permissions

We can set custom permissions in models by adding to a sub-class Meta list as a tuple with 
the id and it's name. After adding them, we should run and make migrations in order to 
get the permissions updated.

Then we can use them with the users by checking if they have then with has_perm.

## Extending the User Model

We can avoid Re-Making the hole User Model, by expanding it's functionalities in two ways.

Proxy or Relational Extra Table - Model. If we want to create a extra behaviour in our Users we could 
create a extra Model where we can even store more info about our users by doing a OneToOne Relation.
We can even access this data by getting the User Object, and then accessing the Proxy Model just like an 
inner User module:

user.proxy_model.values

By doing this we could modify our admin views to see the extra user fields in our user view.

But even if we still need to change the user Model, we can do it by making a class from AbstractUser,
then register it to admin.py, and set the AUTH_USER_MODEL to the path of our Custom UserModel.

But there's a problem with all of this, if we do it, changing the Models before the first migration, we might run into 
some problems of general dependency issues, the best is doing it at the beging of the project or we should deal with multiple 
versions of Errors and stuff. So, no good. 
That's why we shouldn't use custom UserModels if we are trying to do a custom or reusable app. So there isn't dependency issues when installing one
or more apps with custom UserModels.

We can still do some of the stuff, and try to change or expand the UserModel, but we should be carefull, and thankfull that we have 
some tricks to implement such as:

Avoiding using the User Model, but a generic 'get_user_model' function or directly getting the model from the 
settings.

Even tho if we want to change our UserModel, we should consider if that's the right thing to do in our project and 
apps. Like we could use a custom model so we don't have to do super special queries and store the data of our app 
in our UserModel. But this very thing can break, and or bother, the functionality of our apps. 
Even if we want, or need, we could add diferent ways to authenticate per app. So we don't have to rule and 
be on one and only auth or backend type on each app of the project.

If after checking and avoiding all of that, we still need or want to do a custom UserModel. 
Some Properties, and methods we should check and create if we inherit from CustomUser or AbstractBaseUser
- USERNAME_FIELD
- EMAIL_FIELD
- EQUIRED_FIELDS: list that has the names of required fields
- is_active: bool that depends if the user is active in the sense that can be used, loged or even auth.
- get_full_name()
- get_short_name()

I'm Getting tired of these custom stuff that we can or should do if we want to do a custom UserModel.
This is the complete List of thing to do In order to Change The UserModel correctly.

- Create a new UserClass with all the parameters, attributes, and methods
- Create a new UserManager with all ...
- Update or Modify the Forms of Login, Change, And others of the User Values: Passwords, Emails, etc.
- Register in the Django Admin View the Changes, extra values, and or tables, and everything.

Set the AUTH_USER_MODEL in the settings to our custom UserClass.

Try to do all of this in the begging of the development of the app, since with the DB Migrations, 
we might run into some nasty reference, and other problems, which need to be fixed manually.

And That Folks, Is the Auth Module of Django!!! It is pretty good, and with a lot 
to do and learn. This should be tought in the tutorials, or begginers courses, since it is 
the base of a User Based Project.

But thankfully there's a good guide and full manual available.
