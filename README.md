
# Daniela-Handmade-ecommerce

# Handmade Products  

* [view Live Site Here](https://daniela-handmade-8a9762fab1c1.herokuapp.com/)

Description

</br>
</br>
</br>

# Table Of Contents

* [Parties](#all-parties-involved-and-their-goals)
* [Display](#display-and-layout-across-devices)
* [Features](#features)
* [Models](#models)
* [Parts and applications](#parts-and-applications)
* [Technologies used](#technologies)
* [Deploiment](#deployment)
* [Testing](#testing)
* [Vlaidators](#validators)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

# All Parties involved and their goals

### The customer's goals are
* Buying their desired clothes or handmade accessories with just a few clicks
* Making payments online and receiving their products delivered at home.

### The goals for this Ecommerce are
* Providing handmade clothing products to paying customers
* Generating online payments
* Making sure customers get what they paied for

### The administrator goals are
* Being able to add, delete, edit products in the store
* Being able to create and delete colors and categories

### The Ideal Client
* Likes to wear unique clothes

### User Stories

* As User I want to be able to log in with my google or facebook accounts or create a new account on the website
* As User I want to have the option to change my details in my profile page, So the checkout process will be easier every time, or, Once I complete the checkout once, I can save my details on my profile or not.
* As User I want to have a checkout page where I can pay with my credit card, without necessarily having an account
* As User I want to be able to connect my google account to my existing account on the website, so In the future I can login with google
* As a Customer I want to be able to see, filter and navigate through all the available products
* As a User I want to see a product description when I click on a Product
* As User I want to be able to add a product to my bag and go to the checkout or continue shopping
* As User I want to be able to edit the products configuration in my bag before going to the checkout page
* As User I want to be able to adjust the bag by setting a different quantity directly from the products page, and also from my shopping cart list
* As user I want to delete an Item from bag either by pressing a button or setting the quantity to 0
* As User I want to be able to see my profile page and edit my personal details


### Moderator Stories
* As Admin I want to ensure my users will always receive their order information, even when a desync happens in the checkout form.
* As Admin I want to be able to add new categories or delete old ones, As my collections might change in the future,
I also want the categories to be displayed in the navbar
* As Admin I want to be able to add new available colors to the website, by only selecting the color without knowing it's name
* As Admin I want to be able to edit products in the store, As a new color or category was added to the Store
or a "you have to log in" page for suggestions and profile pages
* As an Admin I want to be able to insert new products on the website

</br></br></br></br>

# Display and Layout across devices

![image with Layouts across devices](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685357777/displays_prjsfq.png)

* web large
* web medium
* web small
* tablet
* Surface Duo
* Iphone 12 Portrait
* Iphone 12 landscape

</br></br></br>

# Features

### Nav Bar

![navbar versions image]()
there are 3 states :

* if Logged in as a normal User,
* if Logged out,
* if Logged in as an Admin,
* all three states inherit the collapsible feature from Bootstrap.

### Home Page

* ### Welcome section

![welcome-section image]()


### Products Page

![vods Page image]()

* All Products
* Collection based pages
    
## add configured product to the bag
## delete configured product from bag

### Profile Page

![profile Page image]()

* If the user is logged in the website, 
* If the user isn't logged in yet, he will be redirected to the login page

### Cart Page

![Cart mechanism image]()

* On This Page Django Unicorn was used to send Ajax requests to the backend, meaning everything that happens on this page is instantly rendered without full page reloading
* users can only write or see suggestions if they are logged in, otherwise they will be showed a message telling them to Log in with their twitch account
* Once a suggestion's form is submitted, the suggestion goes into awaiting approval mode, The user can still edit or delete it at this point
* Once a suggestion is approved it can be up voted by it's author or any other user
* At this point the user can still edit or delete the suggestion, after submitting the edit form, if valid, the suggestion will go into approval mode again
![filters image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685366887/filters_ldkiza.png)
* There are 3 sets of filters:
  * All / Mine  
    * renders the list with all Approved Suggestions or just the current logged in User's suggestions.
  * Approved / Awaiting Approval
    * If awaiting approval is on the All/Mine filter will get set on Mine automatically.
    ![filters-wireframe image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685369630/filters-miniwireframe_pfyzrc.png)
  * By votes / by date
    * this filter works the same at all times


### Log in

![sing in image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367865/sign_in_gmsrex.png)

### Log out

![sign out image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367866/sign_out_q6gdpv.png)

### Awaiting Approval

![awaiting approval page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367866/awaiting_approval_page_lmwv0r.png)

* here the admin will approve sugestions that are either newly created or edited by the users

### /// Important Feature left outside this version /// ###

A delete button will be displayed along with any suggestion

### Footer

![footer_image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685368482/footer_knmedl.png)

* Social Media Links

### Django Messages

![django_messages_image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685369870/django-messages_rmckiv.png)

### Left to implement

* Google login, as currently you can only connect a google account to your profile, bot you don't have the option of logging in with google
* Contact Page
* Blog Application
* Gsap Library for front end user experience [see my CV as example](https://bogdan-branzaniuc.github.io/CV/)

</br></br></br>

# Models

[See the models wireframe]()

</br></br></br>

# Applications
## Home App
    responsible for index.html page
## Products App
    responsible for products.html page and unicorn component product
## Bag App
    responsible for bag.html page and unicorn components item_in_bag and bagstatus
## Profiles App
    responsible for Profiles page
## Checkout App
    The checkout app comes from boutiquado walkthrough project from Code Institute Programme and addapted to my project


# Technologies
* JS
* Python and [pycharm](https://www.jetbrains.com/pycharm/) IDE
* [Django framework](https://www.djangoproject.com/)
* Django and Python resources:
  * [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
  * [Django Unicorn](https://www.django-unicorn.com/)
  * [crispy_forms]()
  * [django_countries]()
    [colorfield]()
    [cloudinary_storage]()
    [cloudinary]()
    [crispy_forms]()
    [crispy_bootstrap4]()
    [webcolors]()
* [Gunicorn](https://gunicorn.org/)
* [Jquery](https://jquery.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Elephant SQL](https://www.elephantsql.com/)  
* [Postgres](https://www.postgresql.org/)
* [Heroku](https://dashboard.heroku.com/login)
* [Cloudinary](https://cloudinary.com/)
* [Figma](https://www.figma.com/)
* [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
* [Lottie Files](https://lottiefiles.com/)
* [Google Fonts](https://fonts.google.com/)
* [Fontawesome](https://fontawesome.com/)
</br></br></br></br>

# Deployment
* If you are using Gitpod with Pycharm, run this command in order to be able to install requirements to Django

```
echo 'export PIP_USER=no' >> ~/.bashrc && export PIP_USER=no
```

* [Create a virtual env and install requirements.txt (stack overflow)](https://stackoverflow.com/questions/41427500/creating-a-virtualenv-with-preinstalled-packages-as-in-requirements-txt)

```
pip install virtualenv          //(if you don't already have virtualenv installed)
virtualenv venv to create       //your new environment (called 'venv' here)
source venv/bin/activate        //to enter the virtual environment
pip install -r requirements.txt //to install the requirements in the current environment
```

## Log into your Cloudinary account

  create env.py file in your root directory </br></br>

  env.py

  ```
  import os

  os.environ["CLOUDINARY_URL"] = "your cloudinary url"
  ```

  </br>

  settings.py

  ```
  STATIC_URL = '/static/'
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

## Create an ElephantSql Database

* Log into your elephant Sql account
* click on ```Create New Instance```
* Sellect ```Tiny Turtle(Free)```
* from the main dashboard sellect your new instance</br></br>

  env.py

  ```
  os.environ["DATABASE_URL"] = "Elephant Sql Database Url"
  ```

  </br>

  settings.py

  ```
  DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
  ```

  </br> </br>

## Create a Heroku Application

* Log into your Heroku account
* press ```New``` and ```create new app```
   </br> </br>

## Create your Twitch Application

* go on [https://dev.twitch.tv/console](https://dev.twitch.tv/console) and create or log into your twitch account
* Click on *Register Your Application*
* Set Category to *Website Integration* and then click *create*

* Go to your developer console and click *manage* on your newly created App
* Set *OAuth Redirect URLs* to ```your_heroku_app_domain/accountstwitch/login/callback/``` it also supports localhost
  
* In your settings.py file

  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_unicorn',
    'home',
    'profiles',
    'products',
    'bag',
    'checkout',
    'django_countries',
    'colorfield',
    'cloudinary_storage',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap4',
    'webcolors',
]

  SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'key': ''
        }
    }
}

SOCIALACCOUNT_STORE_TOKENS = True

  ```

* In your project terminal

  ```
    python manage.py makemigrations
    python manage.py migrate
  ```

* run your django Project with

  ```
    python3 manage.py runserver
  ```

* create a superuser with

  ```
    python manage.py createsuperuser
  ```

* log into your django admin panel
* Go to ```Sites``` Model
* Edit the site that django generated to point to your heroku app url ex ```https://tundorul.herokuapp.com/```
* click save

* Go to SocialApplications model and create a new instance
  * Provider: ```Twitch```
  * Name: ```your heroku app and google app would be great to have the same names for consistency reasons```
  * Client id: ``` your google client id ```
  * Secret key: ``` your google secret ```
  * Key: ``` blank ```
  * sites: ```select the site you created previously and click the arrow to move it to the right box```
  * If you click on the site, you can see it's ID in the top url, 
  Use SITE_ID = <that site id number> in you django settings 
* click save

</br>

## Create a procfile

* In your root directory create a file named ```Procfile``` </br>

Procfile

```
  web: gunicorn daniela_handmade.wsgi
```

</br>

# /////////// Make extra sure you have ```Debug = False``` in your settings.py \\\\\\\\\\\\\\\\\\\

## Setup Heroku App for deploiment

* Go on Heroku select your application and click ```settings```
* ```Reveal Config Vars```
* Fill in all the environment variables you have in env.py
* add ```PORT 8000```
* Go to ```Deploy```
* connect your github repository to heroku, sellect the branch and Hit ```deploy branch```
</br>
</br>

## Voilla! if everything went well the app is up and running

</br></br></br>


# Testing

## UX & UI

* I used [BrowserStack](https://live.browserstack.com/dashboard#os=iOS&os_version=14.0&device_browser=safari&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2F8000-bogdanbranzaniuc-cv-xsqhgnyysr5.ws-eu87.gitpod.io%2F%23about-me&speed=1) for testing the application across multiple browsers and devices within the limit of a free trial.
* Also Tested directly on my devices:
* One+ 9 Android Chrome
* Windows Desktop Brave, Chrome, Mozila, Opera

## Manual Testing

* all the features were manualy tested by me during development and by me, friends and family after development

  * Create A suggestion Test:
    * wrote the title '123' while complying with the live form feedback
    * wrote the suggestion body '12345678910' while complying with the live form feedback
    * pressed Send
    * Got a green message saying ('Your suggestion is awaiting approval')

  * Create A suggestion with the same title:
    * wrote the title '123' while complying with the live form feedback
    * wrote the suggestion body '12345678910' while complying with the live form feedback
    * pressed Send
    * Got a red message saying ('There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same')  

  * Upvote Suggestion
    * If logged in, went on suggestions page and clicked the dark arrow up to a suggestion
    * The arrow turned green and the sugegstion votes were updated instantly.

  * Edit Suggestion
    * If logged in, went on suggestions page and clicked the dark pencil icon to edit one of my suggestions
    * a form with two buttons appeared. a green check mark(submit button) and a yellow X
    * if wanted to edit
      * Completed the form with new valid data and submitted by pressing the green check mark button
      * Got a green message with "Your edit is awaiting approval."
      * When trying to use an existing title got a red message with "Sorry!, There is one suggestion with this title Already"
    * if wanted to return
      * pressed the yellow X icon button and returned at the current state of the displayed suggestion

  * Delete Suggestion
    * If logged in, went on suggestions page and clicked on one of my suggestion's red bin icon
    * two more buttons came in , a yellow X and a red check mark,
    * pressed on the red check mark and the suggestion was deleted,
    * pressed on the yellow X icon and returned at the current state of the displayed suggestion.

  * Login
    * If logged in on twitch allready
    * pressed the log in button in the navbar
    * On login page press Sign In
    * Wait for the twitch verification or Authorise Tundorul Website in twitch confirmation pgae,
    * Redirected on the Home page with a green message "Successfuly signed in as 'my username'"

  * Login
    * If not logged in on twitch allready
    * pressed the log in button in the navbar
    * On login page press Sign In
    * Log in with my twitch account in the login form provided by twitch
    * Redirected on the Home page with a green message "Successfuly signed in as 'my username'"

  * Logout
    * Once loged in on Tundorul, pressed the Log out button in the nav,
    * On logout page pressed the Sign Out
    * Redirected to the home page with green message "You have signed out".

## Database Testing

* The web app was developed with a Django default database
* Tested with the default database, migrated to a production Database, and tested again with the production Database

## Unit Tests

![coverage tests report]()

In order to run the tests you need to go in settings.py and use Django default database.

```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}
```

also make sure to start the virtual env

```
. my_env/bin/activate
```

and then run all tests with

```
python manage.py test 
```

# Validators

* html Validator.w3
  * [Home page]()
  * [Vods page]()
  * [Profile page]()
  * [Suggestions page]()
  * [Log out]()
  * [Log in]()

* Css Validator
  * [style.css]()
  * [home.css]()
  * [suggestions.css]()
  * [user-profile.css]()
  * [vods.css]()

* Python Validator
  * As I developed this project in Pycharm, all the code is pep8 complient.

* Js Validator for streamschedule.js file
    ![Streamschedule JS]()

* Lighthouse
    ![Lighthouse immage]()
  * Some accessibility errors are django related, they will be solved in future versions of my project
  
</br></br></br>

# Credits

## Django Developers

## Django Allauth Library Developers

## Django Unicorn Library Developers

## Bootstrap Developers

## Python, Js, Jquery creators
 

* Without this people, my project's current state would have been far from reality in this amount of time.


## Media Files
[background images are from FreePick](https://www.freepik.com/)
  
## Stack Overflow

* I managed to overcome a lot of issues by just going on this amazing resource with a copy paste of my errors.


## Chat GPT

* I used Chat GPT to navigate Django's main concepts, As a beginner I found it the quickest way to see how Django's Lego pieces were coming together.
* I learned to use ChatGPT mainly for general concepts rather than specifics, since it's training consists of lying and deceiving about it's current knowledge.
* Lesson I learned from Chat GPT : ```When you feel like you're chasing your tail around ChatGPT, the answer is elsewhere```

## Code Institute

* For enforcing and encouraging high standards of good practices on my projects
* For compacting and providing valuable information and know-how in their course

## Me
* For designing the architecture of the website
* For creating a decent product that meets the requirements of both Code Institute and Daniela's Business
* For understanding and writing all the code needed to interchange data between all the architectural parts and technologies used

# Acknowledgements

## My mentor Brian Macharia
* Brian Helped me a lot towards the end of the project, knowing how to press the Turbo Button

## Daniela
* for offering me the opportunity to build my project around her future business.

## Student Care Team
* For giving me the needed help and responding quickly to my requests.
