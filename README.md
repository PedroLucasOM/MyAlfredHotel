<h1 align="center">Welcome to MyAlfredHotel 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/Python-3.8.2-blue.svg" />
  <img src="https://img.shields.io/badge/Flask-1.1.1-blue.svg" />
  <img src="https://img.shields.io/badge/FlaskRESTful-0.3.8-blue.svg" />
  <a href="https://github.com/PedroLucasOM/MyAlfredHotel#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-green.svg" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/maintained-yes-green.svg" />
  </a>
  <a href="https://github.com/PedroLucasOM/MyAlfredHotel/blob/master/LICENSE.rst" target="_blank">
    <img alt="License: FLASK" src="https://img.shields.io/github/license/PedroLucasOM/MyAlfredHotel" />
  </a>
  <a href="https://twitter.com/PedroLucasOM" target="_blank">
    <img alt="Twitter: PedroLucasOM" src="https://img.shields.io/twitter/follow/PedroLucasOM.svg?style=social" />
  </a>
</p>

> API for handling hotels with user control - including email confirmation - and hotel sites for advertisements. It has security with OAUTH and SQLite database.

### 🏠 [Homepage](https://github.com/PedroLucasOM/MyAlfredHotel)

## Prerequisites

- aniso8601==8.0.0
- api==0.0.7
- certifi==2019.11.28
- chardet==3.0.4
- Click==7.0
- Flask==1.1.1
- Flask-JWT-Extended==3.24.1
- Flask-RESTful==0.3.8
- Flask-SQLAlchemy==2.4.1
- idna==2.9
- itsdangerous==1.1.0
- Jinja2==2.11.1
- MarkupSafe==1.1.1
- nose==1.3.7
- PyJWT==1.7.1
- pytz==2019.3
- requests==2.23.0
- six==1.14.0
- SQLAlchemy==1.3.13
- urllib3==1.25.8
- Werkzeug==1.0.0

## Install

```sh
pip3 install virtualenv
```

## Usage

#### Creating the virtual environment

```sh
virtualenv myalfred
```

#### Activating the virtual environment

###### For Linux / Mac distributions

```sh
source myalfred/bin/activate
```

###### For Windows

```sh
myalfred\Scripts\activate.bat
```

#### Installing the requirements

```sh
pip3 install -r requirements.txt
```

## Mailgun API

To use the confirmation e-mail service when registering, create an account at:

https://www.mailgun.com/

After that, create this file with the following directory:

```sh
keys/mailgun.py
```

Now place the following content in the file:

```sh
MAILGUN_DOMAIN = 'YOUR-MAILGUN-SANDBOX-DOMAIN'
MAILGUN_API_KEY = 'YOUR-MAILGUN-API-KEY'
FROM_TITLE = 'NO-REPLY'
FROM_EMAIL = 'YOUR-EMAIL'
```

## Run

```sh
python3 app.py
```

## Author

👤 **Pedro Lucas**

* Twitter: [@PedroLucasOM](https://twitter.com/PedroLucasOM)
* Github: [@PedroLucasOM](https://github.com/PedroLucasOM)
* LinkedIn: [@PedroLucasOM](https://linkedin.com/in/PedroLucasOM)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/PedroLucasOM/MyAlfredHotel/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Pedro Lucas](https://github.com/PedroLucasOM).<br />
This project is [FLASK](https://github.com/PedroLucasOM/MyAlfredHotel/blob/master/LICENSE.rst) licensed.
