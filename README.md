# This web page to manage the count the syllables in all verses of a poem. 
# Deploy on pythonanywhere.com

## Steps
1. steps on Consoles' tab
2. steps on Web App's tab
3. Database setup

## Steps on Consoles' tab
- First, we create a new console, and on it,
```
# Download the git project
git clone https://github.com/reynaldocv/cronicos.git
# Create a environment
mkvirtualenv hospital_env --python=/usr/bin/python3.8
# Install Django
pip install django
```
## Steps on Web App's tab
Create a Web app with Manual Config
Head over to the Web tab and create a new web app, choosing the "Manual Configuration" option and the right version of Python (the same one you used to create your virtualenv).
<p align="center">
  <img src="/imgs/django.png">
</p>

Configuring the environment part:

<p align="center">
  <img src="/imgs/env.png">
</p>

Configuring the code part:

<p align="center">
  <img src="/imgs/code.png">
</p>

Configuring the wsgi.py file. 

<p align="center">
  <img src="/imgs/wsgi.png">
</p>

Configuring the static file part:

<p align="center">
  <img src="/imgs/static.png">
</p>

## Database setup 

Go back to console and we execute the following commands: 

```
source .virtualenvs/hospital_env/bin/activate
cd cronicos/cronicos/

# Generate database
python3 manage.py migrate

# Generate the statics files
python3 manage.py collectstatic

```
> [!IMPORTANT]
> Modify the parameter ALLOWED HOST to add our URL **reynaldocv.pythonanywhere.com**, in settings.py file: 
```
ALLOWED_HOSTS = ['192.168.1.12', "localhost", "127.0.0.1","reynaldocv.pythonanywhere.com"]
```

Now, you are done! :tada:

