# Password generator
Stack:
<li>
    Python 3.10
</li>
<li>
    Django 4.1
</li>
<br>
Absurdly simple project on Django framework without deep usage of its core functions and advantages. But, as someone once said <p style='font-weight:bold'>There is often great beauty in simplicity.'</p>
<br>

### Project allows user to generate a random password with prefered optinos:
```
Length: from 6 up to 14 characters
```
```
Uppercase: whether user would like to have uppercase letters in his password
```
```
numbers: option to add numbers in password
```
```
Special characters: option to add special characters in password
```
## Urls
```
'' - home page with options
'/password' - page with generated password
'oh_my_god' - test of block content in base.html, but you can 'Give it a try' :)
```

# Installation

clone repository:
```
git clone git@github.com:PhilYaren/password_generator.git
```

setup virtual env for project (_tip: don't forget to check your python version, you might want to specify your python version eg._ __python3.10__):
```
python3 -m venv venv
```
Activate your venv(_scripts instead of bin for windows_):
```
source venv/bin/activate
```
Install requirements:
```
pip install -r requirements.txt
```
(Optinal) if you get annoyed about unaplied migrations - make 'em:
```
python3 manage.py makemigrations

then:

python3 manage.py migrate
```
Start your server on local machine:
```
python3 manage.py runserver
```
Your server will be hosted localy and you can reach it via _'localhost:8000'_ or _'127.0.0:8000'_

<br>
Now you are good to go! Enjoy!