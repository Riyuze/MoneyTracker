# MoneyTracker (ManeTorakka)

https://manetorakka.herokuapp.com

A simple web app to track your money, built using **Django** framework and is deployed on **Heroku**. Aesthetics of the web app was made using **Bootstrap**. You can read more about these on:

Django: https://www.djangoproject.com/

Heroku: https://www.heroku.com/home

Bootstrap: https://getbootstrap.com/

## Features

### Login System
Implemented a login system which requires a verification link sent to the user's email to activate their account, as well as a password reset system.

### Charts
Charts are built into the project using javascript and allows the users to visually see their financial data.

### Output Files
User's are able to download their financial data into several file formats, which includes: CSV, Excel, and PDF.

## Preview

![Preview](https://github.com/Riyuze/mane-torakka/blob/main/Preview.gif)

## Pre-requisites

Create a python virtual environment using:
```bash
python -m venv /path/to/new/virtual/environment
```

Then, fork the code and place it in the root folder.

Next, activate the virtual environment using (Windows):
```bash
Scripts/activate
```

Check https://docs.python.org/3/library/venv.html for more details.

After the virtual environment is activated, install the dependencies needed using:

```bash
pip install -r requirements.txt
```

## Development

On the root folder with the **manage.py** file, run:
```bash
python manage.py runserver
```
This will start a lightweight development web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly.
