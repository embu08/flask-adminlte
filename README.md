# [AdminLTE](https://appseed.us/generator/adminlte/) Flask

Open-source **Flask Dashboard** generated by `AppSeed`. For newcomers, **[AdminLTE](https://adminlte.io/)** is one of the best open-source admin dashboard & control panel theme. Built on top of Bootstrap, `AdminLTE` provides a range of responsive, reusable, and commonly used components.


My name is Yevhen, I'm from Ukraine. I'm hoping to become a junior Python web developer, and this is my first serious project. The goal of the project was to gain some additional experience with Python, Flask, Bootstrap and AdminLTE. For template was taken this project from [AppSeed](https://appseed.us). 

My socials: <br />
[GitHub](https://github.com/embu08)
<br />
[LinkedIn](https://www.linkedin.com/in/yevhen-borysenko-3788a4238/)

<br />

- 👉 [AdminLTE Flask](https://appseed.us/product/adminlte/flask/) - product page
- 👉 [AdminLTE Flask](https://adminlte-flask.appseed-srv1.com/) - LIVE Deployment
- 👉 [Complete documentation](https://docs.appseed.us/products/flask-dashboards/adminlte) - `Learn how to use and update the product`
- ✅ [PRO Version Available](#pro-version) - `enhanced UI` and more `features`

<br />

> Features


- Database: `mysql`
- `DB Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Session-Based authentication (via **flask_login**), Forms validation

<br />

## ✨ Set up the MySql Database

**Note:** Make sure your Mysql server is properly installed and accessible. 

> **Step 1** - Create the MySql Database to be used by the app

- `Create a new MySql` database
- `Create a new user` and assign full privilegies (read/write)

<br />

> **Step 2** - Edit the `.config` to match your MySql DB credentials.

- `DB_ENGINE`  : `mysql+mysqlconnector` 
- `DB_NAME`    : default value = `adminlte`
- `DB_HOST`    : default value = `localhost`
- `DB_PORT`    : default value = `3306`
- `DB_USERNAME`: default value = `appseed_db_usr`
- `DB_PASS`    : default value = `pass`

<br />

Here is a sample:  

```txt
# .config sample

[db_config]
db_engine=mysql+mysqlconnector                                      # Database Driver
db_name=adminlte                                                    # Database Name
db_username=user                                                    # Database User
db_pass=SUPER_SECRET_PASSWORD                                       # Password
db_host=localhost                                                   # Database HOST, default is localhost
db_port=3306                                                        # Database port, default = 3306
secret_key=SUPER_SECRET_KEY                                         # secret key
```

<br />


## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/embu08/flask-adminlte.git
$ cd flask-adminlte
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `flask run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:5000/register`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:5000/login`

<br />

## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                           # Handles home routes (work with db)
   |    |    |-- routes.py                  # Define home routes
   |    |    |-- forms.py                   # Define home forms
   |    |    |-- models.py                  # Define home models
   |    |
   |    |-- authentication/                 # Handles auth routes (login and register)
   |    |    |-- routes.py                  # Define authentication routes  
   |    |    |-- models.py                  # Defines models  
   |    |    |-- forms.py                   # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |    |    |-- includes/                  # HTML chunks and components
   |    |    |    |-- navigation.html       # Top menu component
   |    |    |    |-- sidebar.html          # Sidebar component
   |    |    |    |-- footer.html           # App Footer
   |    |    |    |-- scripts.html          # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- product.html          # product page as index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # App Dependencies
   |
   |-- .config                              # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />
