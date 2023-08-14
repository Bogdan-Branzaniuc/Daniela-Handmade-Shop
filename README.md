
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
* [Bug](#bug)
* [Models](#models)
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

![image with Layouts across devices](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692039654/daniela_handmade/readme/layouts_a26qc4_jpg9io.jpg)

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

![navbar versions image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038110/daniela_handmade/readme/navbar_itoeqd.png)
there are 3 states :
* if Logged in as a normal User,
* if Logged out,
* if Logged in as an Admin,
* all three states inherit the collapsible feature from Bootstrap.

### Home Page

![welcome-section image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692039853/daniela_handmade/readme/home_wid34m.jpg)

### Products Page
![Products Page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038108/daniela_handmade/readme/collections_pkl6dr.png)

### Product component flow
![Products Page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038111/daniela_handmade/readme/product-component_c1fr1l.png)
* select configurations from bag to increase  - decrease quantity or delete them     
* add configured product to the bag
* by clicking add product the quantity will increase by 1
* delete configured product from bag

### Admin products crud Page
![Admin Crud Page](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038108/daniela_handmade/readme/admin_crud_page_cpoj3g.png)

### Add new Product flow
![Admin Crud Page Add](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038108/daniela_handmade/readme/add_new_product_category_color_trqxk6.png)

### Edit existing product flow
![Admin Crud Page Edit](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038108/daniela_handmade/readme/admin_edit_product_n7mkgz.png)

### Profile Page
![profile Page](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038111/daniela_handmade/readme/profile_page_hpwmps.png)

* If the user is logged in the website, 
* If the user isn't logged in yet, he will be redirected to the login page
### Social Accounts
![link social accounts](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692045615/daniela_handmade/readme/google_accounts_kelpcx.jpg)
# IMPORTANT
            this is part of a future use case,
            1 - users will be able to log in with google and set a password to their user profile.
            2 - users will be able to create a user profile and link their google accounts to it.
            
### Sign Up page
![signup Page](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038112/daniela_handmade/readme/sign_up_w6af3r.png)

### Log In page
![login Page](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038112/daniela_handmade/readme/sign_in_g7b7l3.png)

### Log Out page
![logout Page](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038111/daniela_handmade/readme/sign-out_w9nhey.png)

### Cart Page
![Cart mechanism image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692044635/daniela_handmade/readme/cart_fgckmh.jpg)

### Checkout
![Checkout flow image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038108/daniela_handmade/readme/checkout_yojfig.png)




### Left to implement
* Google login, as currently you can only connect a google account to your profile, bot you don't have the option of logging in with google
* Contact Page
* Blog Application
* Gsap Library for front end user experience [see my CV as example](https://bogdan-branzaniuc.github.io/CV/)

</br></br></br>
# Bug 
///////////////////////////

- ## Error
  ![error image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038133/daniela_handmade/readme/console_errors_from_unicorn_dptenx.png)
  ![requests](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038133/daniela_handmade/readme/unicorn_error_zplkaw.png)

- ## moment of occurance
    ```
    when clicking any unicorn components buttons from **product** and **item_in_bag** components
    ```

- ## Environments it occures in 
  ```
      Production - Yes
      Localhost - No
  ```
  
- ## Cause
  ```
      Currently Unknown
  ```
- ## Possible causes:
    * Django unicorn implementation - NO, since it is working fine in localhost. 
    * Conflicts with current session that get's handled in the components
    * Conflicts between dependencies - Possible
  
- ## Repercursions:
* Due to this issue, a checksum error might occur. Checksums are strings of characters that django-unicorn uses to identify components, 
* A checksum error could have a lot of sources, but what all of them have in common is when a page get's out of Sync.  
* With the current bug I could not reproduce a checksums error by spamming the buttons for 5 minutes, but as an extra-safety measure for testing If it ever occurs, you have to delete the session_id stored in the browser application storage
  ![checksums error session_id deletion](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038110/daniela_handmade/readme/session_id_e6ffmj.png)
  
- ## Bug type
      NONFATAL
- ## Conclusion
If a button doesn't work, it can be pressed again untill it works, or the checksum error will eventualy kick in, however I couldn't obtain the checksum error by spammin the component template

# /////////////////////////// End of Bug


*     When working with different components as delete_product from admin crud page,
*     no bug is ocurring
![sample button](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692047650/daniela_handmade/readme/Screenshot_2023-08-14_194323_xff2wg.png)
</br></br></br>

# Models
![models image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692038109/daniela_handmade/readme/models_jghqrk.png)

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
* Set *OAuth Redirect URLs* to ```your_heroku_app_domain/accounts/google/login/callback/``` it also supports localhost
  
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
* Edit the site that django generated to point to your heroku app url ex ```https://<your app>.herokuapp.com/```
* click save

* Go to SocialApplications model and create a new instance
  * Provider: ```Google```
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

# // Make extra sure you have ```Debug = False``` in your settings.py \\

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

* Create A Product Test:
    - 01 Pressed on Add new Products content button in admin_crud_products page
    - 02 selected one of the existing categories
    - 03 added a random number as sku '14351234' 9 digits long - maximum allowed by the form
    - 04 wrote the title 'Barrette'
    - 05 wrote the description 'A handmade knitted barrette'
    - 06 set the price to 4
    - 07 uploaded an image from my computer
    - 08 selected crimson darkslateblue and limegreen colors from the selection widget
    - 09 selected size U. universal
    - 10 pressed add product
    - 11 got message 'Successfuly added product'


## Database Testing

* The web app was developed with a Django default database
* Tested with the default database, migrated to a production Database, and tested again with the production Database

## Unit Tests
    # Unchecked

# Validators
* html Validator.w3
  * [Home page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdaniela-handmade-8a9762fab1c1.herokuapp.com%2F)
  * [Profile page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdaniela-handmade-8a9762fab1c1.herokuapp.com%2Fprofile%2F)
  * [Products page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdaniela-handmade-8a9762fab1c1.herokuapp.com%2Fproducts%2FAll)
  * [Bag page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdaniela-handmade-8a9762fab1c1.herokuapp.com%2Fbag%2F)
  * [Checkout out](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdaniela-handmade-8a9762fab1c1.herokuapp.com%2Fcheckout%2F)

* Python Validator
  * As I developed this project in Pycharm, all the code is pep8 complient.

* Lighthouse
    ![Lighthouse immage](https://res.cloudinary.com/dgzv7gan8/image/upload/v1692047556/daniela_handmade/readme/lighthouse_y97a78.jpg)
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
